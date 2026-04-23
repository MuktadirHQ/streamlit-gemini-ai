from gtts import gTTS
import streamlit as st
import io

text = "Hello, Welcome to this course a;sdjfhdadisljhlpadfhsoi;ahsdfopadsflih"
speech = gTTS(text, lang='en', slow=False)


audio_buffer = io.BytesIO()
speech.write_to_fp(audio_buffer)
st.audio(audio_buffer)