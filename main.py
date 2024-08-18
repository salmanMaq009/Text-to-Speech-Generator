import streamlit as st
import pyttsx3
import platform

# Set up the page configuration
st.set_page_config(page_title="Text-to-Speech Generator", layout="centered")

# Title and description
st.title("Text-to-Speech Generator")
st.write("Convert your text into speech using pyttsx3.")

# Conditional TTS engine initialization based on OS
if platform.system() == "Windows":
    engine = pyttsx3.init(driverName='sapi5')
else:
    engine = pyttsx3.init(driverName='espeak')

# Input text box
text = st.text_area("Enter the text you want to convert to speech:", "", height=150)

# Voice selection
voices = engine.getProperty('voices')
voice_options = [voice.name for voice in voices]
selected_voice = st.selectbox("Select voice:", voice_options, index=0)

# Speed of speech
speech_speed = st.slider("Select speech speed (100 to 200, default 150):", min_value=100, max_value=200, value=150)

# Generate speech button
if st.button("Generate Speech"):
    if text:
        try:
            # Set the selected voice
            for voice in voices:
                if voice.name == selected_voice:
                    engine.setProperty('voice', voice.id)
                    break

            # Set speech rate
            engine.setProperty('rate', speech_speed)

            # Save speech to a file
            output_file = "output.mp3"
            engine.save_to_file(text, output_file)
            engine.runAndWait()
            st.audio(output_file, format="audio/mp3")

            # Display success message
            st.success("Speech generated successfully!")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please enter some text to generate speech.")

# Footer with developer credit
st.markdown(
    """
    <div style="text-align: center; padding: 10px;">
        <hr>
        <p style="font-size: 14px; color: gray;">Developed by Salman Maqbool ❤️</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Styling and UI Customization
st.markdown(
    """
    <style>
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 12px 30px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 18px;
        margin: 10px 0;
        transition-duration: 0.4s;
        cursor: pointer;
        border-radius: 5px;
    }
    .stButton button:hover {
        background-color: white;
        color: #4CAF50;
        border: 2px solid #4CAF50;
    }
    .stTextInput textarea {
        border: 2px solid #4CAF50;
        border-radius: 5px;
        padding: 10px;
    }
    .stSelectbox, .stSlider {
        margin-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
