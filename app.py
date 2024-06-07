import streamlit as st
import whisper

st.title("Speech to Text")
st.text("""
Whisper is an automatic speech recognition model trained on 680,000 hours of multilingual data collected from the web.  
As per OpenAI, this model is robust to accents, background noise and technical language.  
In addition, it supports 99 different languages’ transcription and translation from those languages into English.
""")


# upload audio file with streamlit
audio_file = st.file_uploader("Upload Audio", type=["wav", "mp3", "m4a"])

model = whisper.load_model("base")



if st.sidebar.button("Transcribe Audio"):
    if audio_file is not None:
        st.text("Text is :")
        st.sidebar.success("Transcribing Audio")
        transcription = model.transcribe(audio_file.name)
        st.sidebar.success("Transcription Complete")
        st.success(transcription["text"])
       
    else:
        st.sidebar.error("Please upload an audio file")


st.sidebar.header("Play Original Audio File")
st.sidebar.audio(audio_file)
