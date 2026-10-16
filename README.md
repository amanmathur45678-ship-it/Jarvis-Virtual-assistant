# Jarvis — AI Voice Assistant

**Developed by Aman**

A Python-based AI voice assistant designed to perform tasks through voice commands. Jarvis recognizes a wake word, opens websites, plays music, retrieves news headlines, and answers general questions using Google's Gemini AI.

## Features

- **Voice Recognition:** Activates when the wake word "Jarvis" is recognized.
- **Web Automation:** Opens Google, Facebook, and YouTube through voice commands.
- **Music Playback:** Opens configured music links using a custom music library.
- **News Updates:** Retrieves news articles and reads headlines aloud.
- **AI Integration:** Uses Google's Gemini API to generate responses to general questions.
- **Text-to-Speech:** Speaks responses using the `pyttsx3` library.
- **Hands-Free Operation:** Provides voice-based interaction for supported tasks.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| SpeechRecognition | Speech-to-text processing |
| pyttsx3 | Text-to-speech conversion |
| Google Gemini API | AI-powered responses |
| Requests | HTTP requests for news |
| Web Browser | Opening websites |
| musicLibrary | Music URL management |
| PyAudio | Microphone input support |

## Project Structure

```text
Jarvis/
├── main.py
├── musicLibrary.py
├── requirements.txt
├── README.md
└── .gitignore
```

*Note: Replace `main.py` with your actual Python filename if it differs.*

## Requirements

Before running Jarvis, ensure you have:

- Python installed
- A working microphone
- An active internet connection
- A Google Gemini API key
- A valid news API key and endpoint
- The required Python packages

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/jarvis.git
cd jarvis
```

Replace `your-username` and `jarvis` with your GitHub username and repository name.

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install SpeechRecognition pyttsx3 requests google-genai PyAudio
```

### 4. Configure API Keys

Set your Gemini API key as an environment variable in Windows PowerShell:

```powershell
$env:GEMINI_API_KEY="your_gemini_api_key"
```

Initialize the Gemini client securely in Python:

```python
import os
from google import genai

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)
```

Configure your news API credentials and endpoint according to your chosen news provider.

**Security:** Never upload real API keys or other credentials to a public repository.

## Music Library Setup

Create a `musicLibrary.py` file containing a dictionary of song names and their URLs.

```python
music = {
    "song1": "https://example.com/song1",
    "song2": "https://example.com/song2"
}
```

Replace the example URLs with valid links. The current command parser expects a song identifier as the second word in a command such as `Play song1`.

## Running the Project

Start the assistant using:

```bash
python main.py
```

Jarvis will announce its initialization and begin listening for the wake word.

## Available Voice Commands

| Command | Description |
|---|---|
| `Jarvis` | Activates command listening |
| `Open Google` | Opens Google |
| `Open Facebook` | Opens Facebook |
| `Open YouTube` | Opens YouTube |
| `Play song1` | Opens the configured music link |
| `News` | Retrieves and reads news headlines |
| Ask a question | Sends the question to Gemini AI |

## How It Works

1. Jarvis initializes the speech recognition and text-to-speech engines.
2. It listens through the microphone for the wake word.
3. Once activated, it captures the user's voice command.
4. The command processor checks for predefined actions.
5. Supported commands trigger the relevant website, music, or news functionality.
6. Other commands are forwarded to Gemini AI.
7. The generated response is converted into speech.

## Troubleshooting

**Microphone issues**
- Check microphone permissions and connectivity.
- Verify that PyAudio is installed correctly.

**Speech recognition errors**
- Ensure a stable internet connection for Google's online speech recognition.
- Adjust the listening timeout and phrase duration when necessary.

**Gemini API errors**
- Verify your API key and account access.
- Confirm that the configured model ID is available.
- Check network connectivity and API quotas.

**News or music issues**
- Verify the news endpoint, API credentials, and response format.
- Ensure the requested song exists in `musicLibrary.py` and has a valid URL.

## Current Limitations

- Online speech recognition requires an internet connection.
- Only predefined website commands are supported directly.
- Music links open in a web browser rather than being played by a dedicated media engine.
- News retrieval depends on the configured API.
- General AI responses require access to Google's Gemini API.

## Future Enhancements

- Offline wake-word detection
- Improved natural-language command processing
- Support for multiword song titles
- More website and desktop automation features
- Improved error handling and logging
- Configurable news categories
- Continuous conversational interaction

## Contributing

Suggestions, bug reports, and improvements are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Implement and test your changes.
4. Submit a pull request with a clear description.

## Author

**Aman**

Python Developer | AI and Automation Enthusiast

## License

No license has been specified yet. Add a `LICENSE` file before distributing this project under an open-source license.

---

*Developed by Aman using Python, Speech Recognition, Text-to-Speech, and Google Gemini AI.*
