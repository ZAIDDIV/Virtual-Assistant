**Virtual Assistant**

A simple Python-based voice-controlled launcher that starts on boot, listens for a wake phrase, opens configured apps (Chrome, Notepad, VS Code, Calculator, etc.), and then exits to save resources. The project also launches and later quits a Rainmeter voice-bar skin for visual feedback.

**Files**:
- **Repository**: Virtual Assistant
- **Script**: [daddy.pyw](daddy.pyw)
- **Startup helper**: [daddy_assistant.bat](daddy_assistant.bat)

**Features**:
- **Wake phrase**: Listens for phrases like "wake up daddy is home", "wake up daddy", or "daddy is home" and then performs the configured actions.
- **Auto-start**: Intended to run automatically when Windows boots (via Startup folder or Task Scheduler).
- **Launch apps**: Opens configured application paths (Chrome, VS Code project folder, Notepad, Calculator, etc.).
- **Rainmeter**: Starts a Rainmeter skin (voice bar) and quits it after launching apps to reduce background resource usage.
- **Graceful exit**: After launching the apps, the script stops itself (exits) to avoid running in the background.

**Requirements**
- Windows OS (script uses Windows app paths and Rainmeter commands).
- Python 3.8+ recommended.
- Microphone and permission to use it.

**Python dependencies**
Install the required packages (on Windows you may need PyAudio; use `pipwin` if `pip install pyaudio` fails):

```bash
pip install SpeechRecognition pyttsx3
pip install pyaudio  # or: pip install pipwin && pipwin install pyaudio
```

**Quick setup**
1. Place the repository files in a folder on your PC.
2. Edit `daddy.pyw` to update any paths (Chrome, Rainmeter, project folder) to match your system.
   - The script uses variables such as `CHROME_PATH`, `RAINMETER_PATH`, and `PROJECT_FOLDER` in `daddy.pyw`.
3. Test the script manually first by running:

```bash
python daddy.pyw
```

**Auto-start on boot (Windows)**
- Option A — Startup folder: create or place `daddy_assistant.bat` into your Windows Startup folder (`shell:startup`). The `.bat` can simply call `python "C:\path\to\daddy.pyw"`.
- Option B — Task Scheduler: create a scheduled task that runs at logon with highest privileges and points to the `.bat` or the Python executable and script.

**Usage**
- Ensure your microphone is available and not blocked by another app.
- On boot (or when you start the script), it listens for ambient noise briefly, then waits for the wake phrase.
- Say one of the wake phrases (case-insensitive):
  - "wake up daddy is home"
  - "wake up daddy"
  - "daddy is home"
- Once heard, the script will announce it is launching the apps, open the configured programs, tell Rainmeter to quit for performance, announce completion, and then exit.

**Permissions & privacy**
- This script requires microphone access. On Windows, grant microphone permission to Python or the Python launcher.
- The script uses Google Speech Recognition via the `speech_recognition` library by default (online). If you want offline recognition, adapt the recognizer accordingly.

**Customization**
- To change which apps open, edit the paths in `daddy.pyw` (e.g., `CHROME_PATH`, `PROJECT_FOLDER`, or add other `os.startfile()` / `os.system()` calls).
- To change wake phrases, edit the `WAKE_PHRASES` list in `daddy.pyw`.

**How the script reduces background load**
- After launching configured apps the script calls `os.system(f'"{RAINMETER_PATH}" !Quit')` to stop the Rainmeter skin, and then calls `sys.exit(0)` to stop itself from running in the background.

**Troubleshooting**
- If speech is not recognized:
  - Check microphone volume and permissions.
  - Increase/decrease `recognizer.energy_threshold` in `daddy.pyw` or leave `dynamic_energy_threshold=True`.
- If PyAudio fails to install on Windows, try `pip install pipwin && pipwin install pyaudio`.
- If an app path is incorrect, update it in `daddy.pyw` and re-run.

**Security note**
- The script runs commands and starts programs using configured paths. Only add trusted programs and paths to avoid executing unwanted binaries.

**License**
- Add your preferred license (e.g., MIT) if you plan to share the repository publicly.

If you want, I can: update `daddy.pyw` to make wake phrases configurable via a small config file, or add a sample `daddy_assistant.bat` for the Startup folder. Which should I do next?
