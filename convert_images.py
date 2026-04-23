import streamlit as st
from google import genai
from dotenv import load_dotenv
import os
from PIL import Image

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)

images = st.file_uploader("enter your image:", ['jpg', 'jpeg', 'png'], accept_multiple_files=True)

if images:
    pill_images = [Image.open(x) for x in images]
    promt = """
    Summarize the picture in note formate at max 100 words, 
    add necessary markdown too
    """
    
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[pill_images, promt]
    )
    st.markdown(response.text)
