# Grammatical Error Corrector using Self-Reflection

This is a Streamlit web application that corrects grammatical errors in user-provided sentences using a LangGraph-based iterative process powered by the Google Gemini 2.5 Flash model. The application displays each iteration of the correction process in styled bounding boxes, with arrows indicating transitions between iterations, and shows the final corrected sentence and its grammatical score.

## Features
- **User-Friendly Interface**: A clean, responsive Streamlit GUI with a text area for input, a submit button, and styled output boxes.
- **Iterative Correction**: Uses LangGraph to iteratively correct one grammatical error at a time until the sentence achieves a grammatical score of 0.95 or higher.
- **Visual Feedback**: Displays each iteration's corrected sentence and score in a bounding box, with arrows connecting iterations to show progression.
- **Custom Styling**: Includes a dark-themed design with a responsive heading, blue accents, and hover effects on buttons.
- **Error Handling**: Provides clear error messages for invalid inputs or processing issues.

## Project Structure
- `app.py`: The Streamlit application handling the GUI and user interaction. It imports the grammar correction logic from `grammar_corrector.py`.
- `grammar_corrector.py`: Contains the LangGraph implementation for iterative grammar correction using the Google Gemini model.
- `.env`: Stores the `GOOGLE_API_KEY` for accessing the Google Gemini API (not included in the repository).

## Prerequisites
- Python 3.8 or higher
- Google Cloud account with API access and a valid `GOOGLE_API_KEY`
- Installed dependencies (listed in `requirements.txt`)

## Installation
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd grammatical-error-corrector
   ```

2. **Set Up a Virtual Environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   Required packages:
   - `streamlit`
   - `langchain-core`
   - `langchain-google-genai`
   - `langgraph`
   - `python-dotenv`

4. **Configure Google Cloud**:
   - Authenticate with Google Cloud:
     ```bash
     gcloud auth application-default login
     gcloud auth application-default set-quota-project YOUR_PROJECT_ID
     ```
   - Create a `.env` file in the project root and add your Google API key:
     ```env
     GOOGLE_API_KEY=your-api-key-here
     ```

## Usage
1. **Run the Application**:
   ```bash
   streamlit run app.py
   ```
   This starts the Streamlit server, typically accessible at `http://localhost:8501`.

2. **Interact with the App**:
   - Enter a grammatically incorrect sentence in the text area (e.g., "She go to store yesterday.").
   - Click the "Correct Grammar" button.
   - View the input sentence, followed by each iteration's corrected sentence and score in styled boxes, connected by arrows.
   - The final corrected sentence and score are displayed at the bottom.

## Example
**Input**: "He go to store yesterday."
**Output**:
```
Input: He go to store yesterday.
[Iteration 1]
Corrected Sentence: He goes to store yesterday.
Score: 0.90
↓
[Iteration 2]
Corrected Sentence: He goes to the store yesterday.
Score: 0.95
Final Corrected Sentence: He goes to the store yesterday.
Final Score: 0.95
```

## Notes
- The app uses a black background for both the app and main container. To make the container stand out, consider changing the `.main-container` background color in `app.py` (e.g., to `#ffffff`).
- The LangGraph process stops when the grammatical score reaches 0.95 or higher, as defined in `grammar_corrector.py`.
- Ensure a stable internet connection, as the Google Gemini API requires online access.

## Troubleshooting
- **API Key Errors**: Verify that your `GOOGLE_API_KEY` is correct and that your Google Cloud project has the necessary quotas enabled.
- **Dependency Issues**: Ensure all required packages are installed. Use `pip list` to check versions.
- **LLM Response Errors**: If the Gemini model returns invalid JSON, the app will display an error message with the original input.

## Future Improvements
- Add support for batch processing multiple sentences.
- Enhance the arrow design with SVG graphics for a more polished look.
- Include a history of past corrections for user reference.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
