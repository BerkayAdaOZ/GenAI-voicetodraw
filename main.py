import streamlit as st
import threading
import draw
import transcript
import record
import os

if "recordActive" not in st.session_state:

    st.session_state.recordActive = threading.Event()
    st.session_state.recordingStatus = "Ready to start!"
    st.session_state.recordingCompleted = False
    st.session_state.latestImage = ""
    st.session_state.messages = []
    st.session_state.frames = []


def startRecording():
    st.session_state.recordActive.set()  
    st.session_state.frames = []
    st.session_state.recordingStatus = "Recording your voice.."
    st.session_state.recordingCompleted = False

    threading.Thread(target=record.record, args=(st.session_state.recordActive, st.session_state.frames)).start()

def stopRecording():
    st.session_state.recordActive.clear()
    st.session_state.recordingStatus = "Recording completed!"
    st.session_state.recordingCompleted = True

st.set_page_config(page_title="VoicetoDrawGenAI", layout="wide", page_icon="./icons/title.png")
st.image(image="./icons/genai.png", width=300)
st.title("VoicetoDraw with GenAI")
st.divider()

colAuido, colImage = st.columns([1,4])

with colAuido:
    st.subheader("Auido Record")
    st.divider()
    statusMessage = st.info(st.session_state.recordingStatus)
    st.divider()

    subcolLeft, subcolRight = st.columns([1,2])

    with subcolLeft:
        startButton = st.button(label="Start", on_click=startRecording, disabled=st.session_state.recordActive.is_set())
        stopButton = st.button(label="Stop", on_click=stopRecording, disabled=not st.session_state.recordActive.is_set())
    with subcolRight:
        recordedAudio = st.empty()  

        if st.session_state.recordingCompleted:
            recordedAudio.audio(data="voice_prompt.wav")

    st.divider()
    latestImageUse = st.checkbox(label="Use Latest Image")

with colImage:
    st.subheader("Image Outputs")
    st.divider()

    for message in st.session_state.messages:

        if message["role"] == "assistant":
            with st.chat_message(name=message["role"], avatar="./icons/assistant.png"):
                st.warning("Here is the image I created for you! ")
                st.image(image=message["content"], width=300)
        elif message["role"] == "user":
            with st.chat_message(name=message["role"], avatar="./icons/user.png"):
                st.success(message["content"])

    if stopButton:
        with st.chat_message(name="user", avatar="./icons/user.png"):
            with st.spinner("Processing..."):
                voicePrompt = transcript.transcribeWithWhisper(audioFileName="voice_prompt.wav")
            st.success(voicePrompt)

        st.session_state.messages.append({"role":"user", "content": voicePrompt})

        with st.chat_message(name ="assistant", avatar= "./icons/assistant.png"):
            st.warning("Here is the image I created for you! ")
            with st.spinner("Processing..."):

                if latestImageUse:
                    imageFileName = draw.generateImage(imagePath=st.session_state.latestImage, prompt=voicePrompt)
                else:
                    imageFileName = draw.generateImageWithDalle(prompt=voicePrompt)

            st.image(image=imageFileName, width=300 )
            
            with open(imageFileName, "rb") as file:
                st.download_button(
                    label="Download Image",
                    data=file,
                    file_name=imageFileName,
                    mime="image/png"

                )


        st.session_state.messages.append({"role":"assistant", "content": imageFileName})
        st.session_state.latestImage = imageFileName

