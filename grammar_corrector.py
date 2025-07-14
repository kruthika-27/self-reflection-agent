from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import List, TypedDict, Annotated, Literal
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define the State for LangGraph
class State(TypedDict):
    messages: Annotated[List[BaseMessage], add_messages]
    current_score: float
    iterations: List[dict]  # New field to store iteration results

# Initialize the LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.0)

# Define the chatbot node function
def chatbot(state: State) -> State | Literal[END]:
    user_message = state["messages"][-1].content
    prompt = f"""You are a highly accurate grammar correction and scoring assistant.
    Your task is to:
    1. Grammatically correct the provided sentence, ensuring it is natural and fluent.
    2. Assign a grammatical score to the *corrected* sentence. The score must be a float between 0.0 and 1.0, where 1.0 indicates perfect grammatical correctness and 0.0 indicates completely incorrect grammar. The score should reflect the grammatical quality of the *output* sentence.
    3. Make only one correction at once in one iteration.

    Respond ONLY with a JSON object. Do not include any other text or explanation. Do not include any markdown formatting or code blocks.
    The JSON object must have the following two keys:
    - `corrected_sentence`: The grammatically corrected version of the input sentence.
    - `score`: A float (e.g., 0.95, 1.0) representing the grammatical score of the corrected sentence.
    

    Example Input: 'He go to school.'
    Example Output:
    {{
    "corrected_sentence": "He goes to school.",
    "score": 0.98
    }}

    Example Input: 'The cat sits on the mat.'
    Example Output:
    {{
    "corrected_sentence": "The cat sits on the mat.",
    "score": 1.0
    }}

    Input sentence to correct and score: '{user_message}'
    """
    try:
        raw_response = llm.invoke(prompt).content
        response_data = json.loads(raw_response)
        corrected_sentence = response_data.get("corrected_sentence", user_message)
        score = float(response_data.get("score", 0.0))
    except json.JSONDecodeError:
        print(f"Warning: Could not parse LLM response as JSON. Raw response: {raw_response}")
        corrected_sentence = f"Error: Could not process grammar. Original input: '{user_message}'. Please try rephrasing."
        score = 0.0
    except Exception as e:
        print(f"An unexpected error occurred during LLM invocation: {e}")
        corrected_sentence = f"Error: An unexpected error occurred. Original input: '{user_message}'. Please try again."
        score = 0.0

    # Append the iteration result to the iterations list
    iterations = state.get("iterations", [])
    iterations.append({"corrected_sentence": corrected_sentence, "score": score})

    return {
        "messages": [AIMessage(content=corrected_sentence)],
        "current_score": score,
        "iterations": iterations
    }

# Define the conditional function for LangGraph
def should_continue(state: State) -> Literal["chatbot"] | Literal[END]:
    score = state.get("current_score", 0.0)
    score_threshold = 0.95
    if score >= score_threshold:
        print(f"Grammatical score {score:.2f} >= {score_threshold}. Ending process.")
        return END
    else:
        print(f"Grammatical score {score:.2f} < {score_threshold}. Re-processing...")
        return "chatbot"

# Build and compile the LangGraph
builder = StateGraph(State)
builder.add_node("chatbot", chatbot)
builder.add_edge(START, "chatbot")
builder.add_conditional_edges("chatbot", should_continue, {"chatbot": "chatbot", END: END})
app = builder.compile()

# Function to correct grammar using LangGraph
def correct_grammar(input_sentence: str) -> tuple[str, float, List[dict]]:
    """
    Takes an input sentence, processes it through LangGraph, and returns the final corrected sentence,
    its score, and all iteration results.
    
    Args:
        input_sentence (str): The sentence to correct.
    
    Returns:
        tuple[str, float, List[dict]]: The final corrected sentence, its score, and a list of all iterations
        (each iteration is a dict with 'corrected_sentence' and 'score').
    """
    try:
        result = app.invoke({"messages": [HumanMessage(content=input_sentence)], "iterations": []})
        corrected_sentence = result["messages"][-1].content
        score = result["current_score"]
        iterations = result["iterations"]
        return corrected_sentence, score, iterations
    except Exception as e:
        return f"Error: {str(e)}", 0.0, [{"corrected_sentence": f"Error: {str(e)}", "score": 0.0}]