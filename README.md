# Virtual Assistant

A voice-activated automation tool that launches your applications automatically when you say a wake phrase. This lightweight assistant runs in the background with a Rainmeter skin visualization and exits after completing its task to free up system resources.

## Features

- 🎤 **Voice Recognition**: Listens continuously for custom wake phrases using Google's speech recognition API
- 🚀 **Auto-Startup**: Runs automatically when your PC boots up
- 📊 **Rainmeter Integration**: Visual voice bar skin shows when the assistant is listening
- 🎯 **Smart App Launcher**: Opens custom applications (Chrome, Code, Notepad, Calculator, etc.) based on your setup
- ⚡ **Performance Optimized**: Automatically exits and kills background processes after completing tasks
- 🔇 **Text-to-Speech Feedback**: Voice feedback using TTS engine to confirm actions

## Requirements

- Python 3.6+
- Microphone/Audio input device
- [Rainmeter](https://www.rainmeter.net/) (optional, for voice bar visualization)
- Internet connection (for Google Speech Recognition API)

## Dependencies

```
SpeechRecognition
pyttsx3
```

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Virtual-Assistant
   ```

2. **Install required packages**
   ```bash
   pip install SpeechRecognition pyttsx3
   ```

3. **Configure paths** (edit `daddy.pyw`)
   - Update `RAINMETER_PATH` if your Rainmeter installation is in a different location
   - Update `CHROME_PATH` to your Chrome installation path
   - Update `PROJECT_FOLDER` to your desired code editor project location
   - Modify the apps launched to match your preferences

4. **Set up auto-startup**
   - Edit `daddy.bat` to include the correct path to your Python installation
   - Add the batch file shortcut to your Windows Startup folder: `C:\Users\<YourUsername>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`

## Configuration

### Wake Phrases
Edit the `WAKE_PHRASES` list in `daddy.pyw` to customize trigger words:

```python
WAKE_PHRASES = [
    "wake up daddy is home",
    "wake up daddy",
    "daddy is home"
]
```

### Application Paths
Modify these variables to launch your preferred applications:

```python
RAINMETER_PATH = r"C:\Program Files\Rainmeter\Rainmeter.exe"
CHROME_PATH = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
PROJECT_FOLDER = r"C:\xampp\htdocs\Corona Admin Panel"
```

### Audio Settings
Adjust microphone sensitivity and speech recognition parameters:

```python
recognizer.energy_threshold = 120  # Lower = more sensitive
engine.setProperty('rate', 170)    # Speech speed
engine.setProperty('volume', 1.0)  # Volume level
```

## How It Works

1. **Startup**: The application starts with your PC via the batch file
2. **Listening**: Continuously listens through your microphone for the wake phrase
3. **Recognition**: When the wake phrase is detected, triggers the action sequence
4. **Launch**: Opens all configured applications
5. **Cleanup**: Exits the assistant and terminates Rainmeter to optimize system performance

## Usage

Simply say your configured wake phrase (e.g., "wake up daddy is home") when the application is running.

**Example workflow:**
```
You: "Wake up daddy is home"
Assistant: "Daddy's home. Launching everything now."
→ Opens Chrome
→ Opens VS Code with your project
→ Opens Notepad
→ Opens Calculator
→ Closes Rainmeter
Assistant: "All done. Going offline."
→ Application exits
```

## System Requirements

- Windows 10/11
- Python 3.6 or higher
- Microphone access permissions
- Administrator rights (for auto-startup feature)

## Performance Notes

- The application is lightweight and designed to minimize system resource usage
- It automatically terminates after completing tasks
- Rainmeter is closed after launching to free up memory
- Audio processing runs asynchronously to prevent blocking

## Troubleshooting

**"Microphone not detected"**
- Check Windows Settings → Privacy → Microphone permissions
- Ensure your microphone is working in other applications

**"Wake phrase not recognized"**
- Speak clearly and naturally
- Check your internet connection (required for Google Speech Recognition)
- Adjust `recognizer.energy_threshold` value
- Verify the wake phrase matches your configuration

**"Auto-startup not working"**
- Check that the batch file is in the Startup folder
- Verify paths in `daddy.bat` are correct
- Run as Administrator

## License

This project is open source and available under the MIT License.

## Author

Created as a personal voice automation assistant.

---

**Note**: This application requires active internet connection for Google Speech Recognition API. Keep your microphone clean and positioned correctly for best results.
