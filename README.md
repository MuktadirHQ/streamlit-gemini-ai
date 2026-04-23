# Notes Summary and Quiz Generator

A Streamlit web application that uses Google's Gemini AI to analyze images of your handwritten or typed notes, generate a concise summary, provide an audio transcription of the summary, and create customized quizzes to test your knowledge.

## Features

- **Image Upload:** Upload up to 3 images (JPG, JPEG, PNG) of your notes.
- **AI Note Summarization:** Utilizes the `gemini-3-flash-preview` model to generate a markdown-formatted summary of the uploaded notes (max 100 words).
- **Audio Transcription:** Converts the generated summary into speech using Google Text-to-Speech (`gTTS`), allowing you to listen to your notes.
- **Quiz Generation:** Generates 3 quiz questions based on the content of your notes and your selected difficulty level (Easy, Medium, or Hard).

## Technologies Used

- **Python 3**
- **Streamlit:** For the interactive web interface.
- **Google GenAI SDK:** To interact with the Gemini AI models.
- **gTTS (Google Text-to-Speech):** For converting the text summary to audio.
- **Pillow (PIL):** For image processing.
- **python-dotenv:** For environment variable management.

## Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Create a Virtual Environment (Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: Ensure `streamlit`, `google-genai`, `gTTS`, `python-dotenv`, and `pillow` are in your `requirements.txt`)*

4. **Set up Environment Variables:**
   Create a `.env` file in the root directory and add your Gemini API Key:
   ```env
   GEMINI_API_KEY="your_api_key_here"
   ```

## Running the Application

To start the Streamlit application, run the following command in your terminal:

```bash
streamlit run app.py
```

The application will open in your default web browser.

## How to Use

1. Use the sidebar to upload your note images (maximum of 3).
2. Select the desired difficulty level for the quiz (Easy, Medium, or Hard).
3. Click the **"Initiate"** button.
4. The application will display:
   - A concise summary of your notes.
   - An audio player to listen to the summary.
   - A 3-question quiz based on the notes.

## File Structure

- `app.py`: The main Streamlit application script containing the UI and logic flow.
- `api_calling.py`: Contains functions to interact with the Gemini API (`note_generator`, `quiz_generator`) and Google TTS (`audio_transcription`).
- `audio.py` / `convert_images.py`: Helper/testing scripts for audio and image functionalities.
- `.env`: (Not included in version control) Stores your sensitive API keys.

## License

[MIT License](LICENSE) (Optional - you can add a license if needed)
"# streamlit-gemini-ai" 
