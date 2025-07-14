import streamlit as st

# Inject custom CSS for styling
st.markdown("""
    <style>
        /* Style for the entire app background */
    .stApp {
        background-color: #000000; /* Light gray background for the app */
    }
    /* Center heading with responsive width */
    .centered-heading {
        text-align: center;
        color: #ffffff;
        font-family: 'Arial', sans-serif;
        margin-bottom: 20px;
        width: 100%; /* Full width of parent container */
        max-width: 80%; /* Limits width to 90% of parent for smaller screens */
        margin-left: auto;
        margin-right: auto;
    }

    /* Custom label styling */
    .custom-label {
        font-size: 18px;
        font-weight: 600;
        color: #ffffff;
        margin-bottom: 10px;
    }

    /* Note styling */
    .note-red {
        font-size: 14px;
        color: #e74c3c;
        font-weight: 500;
    }
    .note {
        font-size: 14px;
        color: #7f8c8d;
    }

    /* Updated text area styling with white text and darker background */
    .stTextArea textarea {
        border: 2px solid #3498db;
        border-radius: 8px;
        padding: 10px;
        font-size: 16px;
        background-color: #2c3e50; /* Darker background for contrast */
        color: #ffffff; /* White text color */
        transition: border-color 0.3s ease;
    }
    .stTextArea textarea:focus {
        border-color: #2980b9;
        outline: none;
        box-shadow: 0 0 5px rgba(52, 152, 219, 0.3);
    }
    .stTextArea textarea::placeholder {
        color: #bdc3c7; /* Lighter placeholder text for visibility */
    }

    /* Button styling */
    .stButton > button {
        background: linear-gradient(45deg, #3498db, #2980b9);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 12px 24px;
        font-size: 16px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
        width: 200px;
        margin: 10px auto;
        display: block;
    }
    .stButton > button:hover {
        background: linear-gradient(45deg, #2980b9, #3498db);
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
    }
    .stButton > button:active {
        transform: translateY(0);
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }

    /* Container styling */
    .main-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 80px;
        background-color: #000000;
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Main container
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Centered heading
st.markdown('<h2 class="centered-heading">Grammatical Error Corrector using Self-Reflection</h2>', unsafe_allow_html=True)

# Custom label with note
st.markdown("""
    <div class="custom-label">Enter your grammatically incorrect statement:</div>
    <span class="note-red">Note: </span> <span class="note">Only grammatically incorrect statements are allowed</span>
""", unsafe_allow_html=True)

# Text area for input
user_input = st.text_area(
    "Enter your statement to be corrected grammatically:",
    value="",
    key='input',
    height=100,
    placeholder='Enter a grammatically incorrect sentence, e.g., "She go to store yesterday."',
    disabled=False,
    label_visibility="collapsed"
)

# Submit button
if st.button("Correct Grammar"):
    if user_input:
        st.write("Processing your input: " + user_input)
        # Add your grammar correction logic here
        st.success("Correction will appear here (logic to be implemented).")
    else:
        st.error("Please enter a sentence to correct.")

st.markdown('</div>', unsafe_allow_html=True)