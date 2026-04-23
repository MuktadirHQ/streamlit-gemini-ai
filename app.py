import streamlit as st
from api_calling import note_generator, audio_transcription, quiz_generator
from PIL import Image


st.header("Notes Summary and Quiz Generator", anchor=False)
st.markdown("Upload upto 3 images to generate Note summarray and Quizzes")
st.divider()


with st.sidebar:
    st.header("Controls")
    
    images = st.file_uploader(
        "Upload The photos of your note",
        type=['jpg', 'jpeg', 'png'],
        accept_multiple_files=True
    )
    st.subheader("Your uploaded Images")
    
    pill_images = [Image.open(x) for x in images]
    
    if images:
        if len(images) > 3:
            st.error("Upload at max 3 images")
        else:
            col = st.columns(len(images))
            
            
            
            for i, img in enumerate(images):
                with col[i]:
                    st.image(img)
                    
                    
    selected = st.selectbox("Enter the difficulty of your quiz", 
                 ("Easy", 'Medium', "Hard"),
                 index=None
                 )
    
    ini_button = st.button("Initiate", type="primary")
    
if ini_button:
    if not images:
        st.error("You must upload at least 1 Image")
    if not selected:
        st.error("You must select a difficulty")
        
    if images and selected:
        
        with st.container(border=True):
            st.subheader("Your Note's Summary", anchor=False)
            
            with st.spinner("AI is writing notes for you"):
                generated_notes = note_generator(pill_images)
                st.markdown(generated_notes)

        with st.container(border=True):
            st.subheader("Audio Transcription", anchor=False)
            
            with st.spinner("AI is transcriptioning Audio for you"):
                generated_notes = generated_notes.replace("#", "")
                generated_notes = generated_notes.replace("*", "")
                generated_notes = generated_notes.replace("-", "")
                generated_notes = generated_notes.replace("`", "")
                
                generated_audio = audio_transcription(generated_notes)
                st.audio(generated_audio)
       
            
        with st.container(border=True):
            st.subheader(f"Quiz ({selected})", anchor=False)
            
            with st.spinner("AI is making Quizzes for you"):
                generated_quiz = quiz_generator(pill_images, selected)
                st.markdown(generated_quiz)
    
    