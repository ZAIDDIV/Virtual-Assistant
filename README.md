# Voice-Activated Desktop Assistant

A Python-based voice assistant that responds to custom wake phrases and automatically opens your favorite applications.

## Features
- 🎤 Voice-activated with customizable wake phrases
- 🚀 Auto-launches multiple applications
- 🔊 Text-to-speech feedback
- ⚙️ Fully configurable via JSON

## Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

**Note:** PyAudio installation on Windows may require additional steps. If you encounter issues:
```bash
pip install pipwin
pipwin install pyaudio
```

### 2. Configure Your Paths
```bash
# Copy the example configuration
cp config.example.json config.json

# Edit config.json with your actual file paths
```

Update `config.json` with:
- Your application paths (Chrome, VS Code, etc.)
- Desktop shortcut locations
- Preferred wake phrases
- Spotify song URL (optional)

### 3. Run the Assistant
```bash
python assistant.py
```

## Configuration

The `config.json` file contains:
- **paths**: File paths for applications and shortcuts
- **wake_phrases**: Phrases that trigger the assistant
- **spotify_song_url**: URL to open in browser
- **speech**: Voice settings (rate, volume, energy threshold)

## Usage

1. Run the script
2. Say one of your configured wake phrases
3. The assistant will open all configured applications
4. Confirmation via text-to-speech

## Troubleshooting

- **Microphone not detected**: Check your default input device
- **Recognition errors**: Adjust `energy_threshold` in config
- **App won't open**: Verify paths in `config.json`

## Security Note

Never commit your `config.json` file to version control as it contains personal file paths.

## License

MIT License - Feel free to modify and distribute!
```

5. Save and close

---

### **File 6: LICENSE**

1. Right-click → New → Text Document
2. Name it: `LICENSE` (no extension)
3. Open with Notepad
4. Paste this:
```
MIT License

Copyright (c) 2025 [Your Name or GitHub Username]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.