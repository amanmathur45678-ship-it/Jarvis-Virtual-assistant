# Jarvis — AI Voice Assistant

**Developed by Aman**

Jarvis is a Python-based voice assistant that allows users to interact with their computer using voice commands. It can open websites, access music links, retrieve news headlines, and answer general questions using Google's Gemini AI.

The project combines speech recognition, text-to-speech, web automation, and AI-powered responses to provide a simple hands-free assistant experience.

## Features

- **Voice Activation:** Listens for the wake word `Jarvis`.
- **Website Automation:** Opens Google, Facebook, and YouTube using voice commands.
- **Music Playback:** Opens configured YouTube links or song search results.
- **News Updates:** Retrieves news articles and reads their headlines aloud.
- **Gemini AI Integration:** Processes general questions using Google's Gemini API.
- **Text-to-Speech:** Uses `pyttsx3` to speak responses.
- **Speech Recognition:** Converts spoken commands into text.
- **Modular Code:** Keeps the music library and Gemini API example in separate Python files.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| SpeechRecognition | Speech recognition |
| PyAudio | Microphone audio input |
| pyttsx3 | Text-to-speech |
| Google Gemini API | AI-generated responses |
| Requests | HTTP requests for news |
| Web Browser | Opens websites and music links |

## Project Structure

```text
Jarvis/
├── main.py             # Main voice assistant
├── client.py           # Standalone Gemini API example
├── musicLibrary.py     # Song names and YouTube URLs
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── .gitignore          # Files excluded from Git
```

## Prerequisites

Before running the project, make sure you have:

- Python installed
- A working microphone
- An active internet connection
- A Google Gemini API key
- A valid news API endpoint and API key
- The required Python packages

## Installation

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

```powershell
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install SpeechRecognition pyttsx3 requests google-genai PyAudio
```

If PyAudio installation fails, follow the installation instructions for your operating system.

### 4. Configure API Keys

The Gemini API and news feature require valid credentials and configuration.

For Windows PowerShell, set your Gemini API key:

```powershell
$env:GEMINI_API_KEY="your_gemini_api_key"
```

Update your Python code to read the key from the environment:

```python
import os
from google import genai

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)
```

Configure the news API endpoint and authentication according to your chosen news provider.

**Security note:** Never commit real API keys, passwords, or private credentials to a public GitHub repository.

## Music Library

The `musicLibrary.py` file stores song identifiers and their corresponding YouTube URLs.

Current configured entries:

| Song Identifier | Action |
|---|---|
| `aman` | Opens the configured YouTube video |
| `aag` | Opens the configured YouTube video |
| `skyfall` | Opens YouTube search results for Skyfall |

Example usage:

```python
music = {
    "aman": "YOUR_YOUTUBE_URL",
    "aag": "YOUR_YOUTUBE_URL",
    "skyfall": "YOUR_YOUTUBE_SEARCH_URL"
}
```

The actual URLs are maintained in `musicLibrary.py`.

To play a configured entry, use a command such as:

- `Play aman`
- `Play aag`
- `Play skyfall`

The current command parser expects the song identifier to be the second word in the command. Music links open in the web browser rather than being played by a built-in audio player.

## Running the Assistant

Run the main application:

```bash
python main.py
```

Jarvis announces its initialization and begins listening for the wake word.

### Available Voice Commands

| Voice Command | Action |
|---|---|
| `Jarvis` | Activates command listening |
| `Open Google` | Opens Google |
| `Open Facebook` | Opens Facebook |
| `Open YouTube` | Opens YouTube |
| `Play aman` | Opens the configured music link |
| `Play aag` | Opens the configured music link |
| `Play skyfall` | Opens YouTube search results |
| `News` | Retrieves and reads news headlines |
| Ask a general question | Sends the question to Gemini AI |

Speech recognition uses Google's online recognition service, so an internet connection is required.

## Gemini AI Integration

The project includes a `client.py` file demonstrating how to use the Google Gen AI SDK to generate a response.

The example uses:

```python
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

response = client.models.generate_content(
    model="YOUR_SUPPORTED_GEMINI_MODEL",
    contents="Enter your question here"
)

print(response.text)
```

Replace the placeholders with a valid API key configuration, a model ID supported by your account, and the desired prompt before running the example.

**Note:** The standalone `client.py` example prints the response to the terminal. The main assistant's AI workflow is handled separately in `main.py` unless you explicitly integrate the two files.

## News Integration

The main application uses the `requests` library to retrieve news articles from a configured API endpoint.

When a news response is successful, the program reads article headlines using text-to-speech.

To enable this feature:

1. Choose a news API provider.
2. Configure its valid endpoint and API credentials.
3. Ensure the response contains an `articles` list with article titles.
4. Handle HTTP errors, missing fields, and API limits appropriately.

The news feature will not work until the placeholder request URL is replaced with a valid endpoint.

## How It Works

1. Jarvis initializes its speech recognition and text-to-speech components.
2. The microphone listens for the wake word.
3. Once the wake word is recognized, Jarvis captures the next voice command.
4. The command processor checks for predefined actions.
5. Website, music, and news commands trigger their respective operations.
6. Unrecognized commands are sent to Gemini AI for a response.
7. The response is spoken aloud using text-to-speech.

## Troubleshooting

**Microphone problems**
- Check microphone permissions and connections.
- Verify that PyAudio is installed correctly.

**Speech recognition errors**
- Check your internet connection.
- Speak clearly and adjust the listening timeout if necessary.

**Gemini API errors**
- Verify your API key and account access.
- Ensure the model ID is supported.
- Check your API quota and network connection.

**News feature errors**
- Verify the API endpoint and credentials.
- Check the HTTP response status and JSON structure.

**Music command errors**
- Ensure the requested identifier exists in `musicLibrary.py`.
- Verify that the corresponding URL is valid.

## Security

- Store API keys in environment variables instead of hardcoding them.
- Add `.env`, `venv/`, `__pycache__/`, and `*.pyc` to `.gitignore`.
- Never publish real credentials in source code or documentation.
- Review all project files before pushing them to a public repository.

## Current Limitations

- Online speech recognition requires internet access.
- Only predefined website commands are supported directly.
- The music command parser supports simple, single-word song identifiers.
- Music links open in a browser.
- News retrieval depends on a correctly configured external API.
- Gemini responses require valid API credentials and an available model.
- The standalone Gemini example is separate from the main assistant workflow.

## Future Improvements

- Dedicated offline wake-word detection
- Support for multiword song names
- Improved natural-language command handling
- Better error handling and logging
- More website automation commands
- Configurable news categories
- Continuous conversational interaction

## Author

**Aman**

Python Developer | AI and Automation Enthusiast

## License

No license has been specified for this project yet. Add a `LICENSE` file if you intend to distribute it under an open-source license.

---

*Built with Python, Speech Recognition, Text-to-Speech, and Google Gemini AI.*
