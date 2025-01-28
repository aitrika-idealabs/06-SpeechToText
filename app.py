import streamlit as st
import pyaudio
import wave
import io
from google.cloud import speech
from google.oauth2 import service_account

# Set up Google Cloud credentials
client_file = "client__file_stt.json"  # Change this to your actual service account file
credentials = service_account.Credentials.from_service_account_file(client_file)
client = speech.SpeechClient(credentials=credentials)

# Streamlit app title
st.title("🎙️ Speech-to-Text Converter using Google Cloud")
st.write("Click the button below to record audio from your microphone and get the transcription.")

# Audio recording function
def record_audio(file_path, record_seconds=5):
    chunk = 1024  # Record in chunks of 1024 samples
    format = pyaudio.paInt16  # 16-bit audio format
    channels = 1  # Mono audio
    rate = 44100  # Sample rate in Hz

    audio = pyaudio.PyAudio()

    st.info("Recording... Speak now!")

    # Open stream
    stream = audio.open(format=format, channels=channels,
                        rate=rate, input=True,
                        frames_per_buffer=chunk)

    frames = []

    # Record for a specified number of seconds
    for _ in range(0, int(rate / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save recorded audio to a WAV file
    with wave.open(file_path, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(format))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))

    st.success("Recording completed!")

# Transcribe audio using Google Cloud
def transcribe_audio(file_path):
    with io.open(file_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)

    # Extract transcription text
    transcriptions = [result.alternatives[0].transcript for result in response.results]
    return " ".join(transcriptions)

# File path for recorded audio
audio_file_path = "recorded_audio.wav"

# Record Button
if st.button("🎤 Start Recording"):
    record_audio(audio_file_path, record_seconds=5)

# Transcribe Button
if st.button("📜 Transcribe Audio"):
    if audio_file_path:
        st.info("Transcribing audio...")
        transcription = transcribe_audio(audio_file_path)
        if transcription:
            st.success("Transcription complete!")
            st.write("**Transcribed Text:**")
            st.text_area("Transcription", transcription, height=150)
        else:
            st.warning("No speech detected. Try recording again.")
    else:
        st.error("No audio recorded. Please record first.")

