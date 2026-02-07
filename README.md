Virtual Assistant
A lightweight, Python-based voice automation tool designed to streamline your workflow from the moment you boot up. This assistant listens for a specific wake phrase, executes your predefined application shortcuts, and then gracefully exits—alongside its visual interface—to ensure zero impact on system resources once its job is done.

⚙️ How It Works
Auto-Boot: The script is configured to launch automatically upon Windows startup.

Visual Feedback: Upon launching, it triggers a Rainmeter skin (Voice Bar) to provide a visual indication that the assistant is active and listening.

Voice Activation: Using speech_recognition, the script stays in a low-power listening state waiting for your unique wake phrase.

Task Execution: Once triggered, it opens your designated applications (Chrome, Notepad, etc.) using the direct file paths provided in the code.

Self-Termination: To keep your PC running at peak performance, the script kills its own process and the Rainmeter skin immediately after the apps are launched.

🛠️ Built With
The project leverages the following Python libraries:

speech_recognition: To capture and interpret your voice commands.

pyttsx3: For text-to-speech feedback (offline support).

os & sys: For system-level operations and path handling.

time: To manage delays and synchronization during the boot sequence.

🚀 Getting Started
Prerequisites
Python 3.x installed.

installed (for the visual voice bar).

Microphone access enabled.

Installation
Clone the repository:

Install dependencies:

Configuration: Open the main script and update the apps dictionary with your specific paths:

🖥️ Setting up Auto-Start
To ensure the assistant starts when your PC boots:

Press Win + R, type shell:startup, and hit Enter.

Create a shortcut of your Python script (or a compiled .exe) in this folder.

Note: Ensure your Rainmeter skin path is correctly referenced in the code so the script knows which process to kill upon exit.

📝 License
Distributed under the MIT License. See LICENSE for more information.
