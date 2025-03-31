# 🎙️ Streamlit Speech-to-Text App (Google Cloud)

A powerful **speech-to-text application** built with Streamlit and Google Cloud Speech-to-Text API. It allows users to record audio, transcribe it into text in real-time, and supports multiple languages. Perfect for demos, accessibility solutions, and speech analysis projects.

---

## 🌟 What the Code Does

1. **Records audio** from your microphone using Streamlit’s interface.  
2. **Processes the audio** and sends it to Google Cloud’s Speech-to-Text API.  
3. **Transcribes speech into text** in real-time.  
4. **Supports multiple languages** with customizable options for recognition.  
5. Provides an **interactive UI** for starting/stopping recordings and viewing transcriptions.

---

## 🚀 How to Use It (Step by Step)

### 1. Clone the Repository
```bash
git clone https://github.com/aitrika-idealabs/streamlit-speech-to-text.git
cd streamlit-speech-to-text
```

### 2. Set Up the Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate      # For Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Google Cloud Speech-to-Text API
1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project and enable the **Speech-to-Text API**.
3. Generate a **Service Account** and download the JSON key file.
4. Set the environment variable for your system:
   - On macOS/Linux:
     ```bash
     export GOOGLE_APPLICATION_CREDENTIALS="path/to/your-key-file.json"
     ```
   - On Windows (PowerShell):
     ```powershell
     $env:GOOGLE_APPLICATION_CREDENTIALS="path\to\your-key-file.json"
     ```

### 5. Run the App
```bash
streamlit run app.py
```

### 6. Use the App
1. Click **"Start Recording"** to record audio (default: 5 seconds).
2. Click **"Transcribe Audio"** to process the recording and convert speech into text.
3. Copy or use the transcribed text as needed.

---

## ⚙️ What Happens in Each Step

### Step 1: **Record Audio**
- The `record_audio()` function uses the system microphone to record audio and saves it in `.wav` format for processing.

### Step 2: **Send to Google Cloud API**
- The `.wav` file is sent to Google Cloud Speech-to-Text API using the `speech.RecognitionConfig` parameters for encoding, sample rate, and language.

### Step 3: **Transcription**
- Google Cloud processes the audio and returns the transcription in text format, which is displayed on the Streamlit interface.

### Step 4: **Interactive UI**
- Streamlit's UI updates dynamically, providing buttons to start/stop recording, initiate transcription, and show real-time results.

---

## 🖼️ Screenshots

### Main UI
![Main Interface](https://github.com/user-attachments/assets/a7fdbcb3-ac88-478b-8a25-b69fb0beb987)

---
---

## 📂 Role of Each File

### `app.py`
- The main application script that contains the Streamlit UI and logic for recording, processing, and transcribing audio.

### `requirements.txt`
- Contains all necessary Python dependencies to run the app (e.g., Streamlit, Google Cloud libraries).

### `recorded_audio.wav`
- Temporary file created during the recording process. Automatically overwritten for each new recording.

### `your-service-account.json`
- Google Cloud credentials file for authenticating API requests. **(Do not share or commit this file)**.

---

## 🛠️ Customization Options

### 1. Change Recording Duration
In `app.py`, modify the `record_audio()` function:
```python
record_audio(file_path, record_seconds=10)  # Record for 10 seconds
```

### 2. Add Support for More Languages
Update the `RecognitionConfig`:
```python
config = speech.RecognitionConfig(
    language_code="es-ES",  # Change language code to Spanish
)
```

### 3. Enable MP3 Format
Install `pydub` for format conversion:
```bash
pip install pydub
```
Modify the `app.py` script to convert MP3 to WAV:
```python
from pydub import AudioSegment

audio = AudioSegment.from_mp3("input.mp3")
audio.export("output.wav", format="wav")
```

---

## 📝 License
This project is open-source and available under the **MIT License**.

---

## 💡 Contributing
Found an issue or have an idea?  
1. Fork this repository.  
2. Create a new branch.  
3. Submit a pull request.

---

## 📧 Contact
🔹 **Aitrika Chakraborty**  
🔹 **GitHub:** [aitrika-idealabs](https://github.com/aitrika-idealabs)  
🔹 **Email:** aitrika@idealabs.fyi  

---

Let me know if you’d like to refine this further! 🚀
