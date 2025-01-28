---

# 🎙️ Streamlit Speech-to-Text App (Google Cloud)  
🚀 A simple yet powerful **speech-to-text app** that records audio from your **microphone** and transcribes it using **Google Cloud Speech-to-Text API**.

---

## 🌟 Features
✅ **Record audio** from your PC microphone  
✅ **Transcribe speech to text** using Google Cloud Speech API  
✅ **Interactive Streamlit UI** with buttons for recording & transcribing  
✅ **Supports multiple languages** (can be extended)  
✅ **Real-time processing**  

---

## 📌 Demo Screenshot
![Speech-to-Text App Demo](![image](https://github.com/user-attachments/assets/ad923ae2-3096-4dbe-8dc5-4ce8277e7fc4)
)  

---

## 📦 Installation

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/streamlit-speech-to-text.git
cd streamlit-speech-to-text
```

### **2. Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate      # For Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Set Up Google Cloud Speech-to-Text API**
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project and **enable Speech-to-Text API**.
3. Create a **Service Account** and download the **JSON key file**.
4. Set the environment variable:
   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="path/to/your-key-file.json"
   ```
   On Windows (PowerShell):
   ```powershell
   $env:GOOGLE_APPLICATION_CREDENTIALS="path\to\your-key-file.json"
   ```

---

## 🎤 How to Use

### **1. Run the Streamlit App**
```bash
streamlit run app.py
```

### **2. Using the App**
- Click **"Start Recording"** to record audio (default: **5 seconds**).
- Click **"Transcribe Audio"** to convert the speech into text.
- View and copy your transcribed text.

---

## 🛠️ Project Structure
```
streamlit-speech-to-text/
│── app.py                     # Main Streamlit app
│── requirements.txt            # Dependencies
│── README.md                   # Documentation
│── recorded_audio.wav          # Temporary audio file (generated)
│── your-service-account.json   # Google Cloud credentials (DO NOT commit)
```

---

## 🔧 Customization

### **1. Change Recording Duration**
Modify the `record_audio()` function in `app.py`:
```python
record_audio(file_path, record_seconds=10)  # Change to 10 seconds
```

### **2. Support for Multiple Languages**
Modify the `language_code` in `RecognitionConfig`:
```python
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=44100,
    language_code="es-ES",  # Spanish
)
```

### **3. Convert MP3 to WAV for More Formats**
Install `pydub`:
```bash
pip install pydub
```
Modify `app.py`:
```python
from pydub import AudioSegment

audio = AudioSegment.from_mp3("input.mp3")
audio.export("output.wav", format="wav")
```

---

## 📝 License
This project is **open-source** and available under the **MIT License**.

---

## 💡 Contributing
Got an idea or found a bug? Feel free to:
- **Fork this repository**
- **Create a new branch**
- **Submit a pull request**

---

## 📧 Contact
🔹 **Aitrika Chakraborty**  
🔹 **GitHub:** [aitrika-idealabs](https://github.com/aitrika-idealabs)  
🔹 **Email:** aitrika@idealabs.fyi

---

Copy and paste this into your `README.md`, and you're all set! Let me know if you need further assistance! 🚀
