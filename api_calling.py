from google import genai
from gtts import gTTS
from dotenv import load_dotenv
import os, io

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)


def note_generator(images):
    prompt = """
    Summarize the picture in note format at max 100 words, 
    add necessary markdown too
    """
    
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images, prompt]
    )

    return response.text


def audio_transcription(text):
    
    speech = gTTS(text, lang='en', slow=False)
    audio_buffer = io.BytesIO() # RAM STORAGE
    speech.write_to_fp(audio_buffer)
    
    return audio_buffer


def quiz_generator(images, difficulty):
    prompt = f"Generate 3 quizzes based on the {difficulty}. Make sure to add markdown to differntiate the options"
    
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images, prompt]
    )

    return response.text