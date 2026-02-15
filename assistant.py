import speech_recognition as sr
import os
import pyttsx3
import sys
import time
import webbrowser
import json

# Load configuration


def load_config():
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("ERROR: config.json not found!")
        print("Please copy config.example.json to config.json and update with your paths.")
        sys.exit(1)


config = load_config()

# Initialize text-to-speech
engine = pyttsx3.init()
engine.setProperty('rate', config['speech']['rate'])
engine.setProperty('volume', config['speech']['volume'])


def speak(text):
    engine.say(text)
    engine.runAndWait()


# Initialize speech recognizer
recognizer = sr.Recognizer()
recognizer.dynamic_energy_threshold = False
recognizer.energy_threshold = config['speech']['energy_threshold']

# Load settings from config
WAKE_PHRASES = config['wake_phrases']
PATHS = config['paths']
SPOTIFY_SONG_URL = config['spotify_song_url']

print("Virtual Assistant Started!")
print("Listening for wake phrases...")
print(f"Say one of: {WAKE_PHRASES}")
print("-" * 50)

while True:
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.8)
            audio = recognizer.listen(source, timeout=4, phrase_time_limit=6)

        try:
            spoken = recognizer.recognize_google(audio).lower().strip()
            print("Heard:", spoken)

            if any(phrase in spoken for phrase in WAKE_PHRASES):
                print("✓ Wake phrase detected!")
                speak("Daddy's home.")

                # Open Chrome
                print("Opening Chrome...")
                if os.path.exists(PATHS['chrome']):
                    os.startfile(PATHS['chrome'])
                else:
                    print("Chrome path not found - skipping")

                # Open VS Code with project folder
                print("Opening VS Code...")
                if os.path.exists(PATHS['project_folder']):
                    os.system(f'code "{PATHS["project_folder"]}"')
                else:
                    print("Project folder not found - skipping")

                # Open ChatGPT
                print("Opening ChatGPT...")
                if os.path.exists(PATHS['chatgpt_shortcut']):
                    os.startfile(PATHS['chatgpt_shortcut'])
                else:
                    print("ChatGPT shortcut not found - skipping")

                # Open WhatsApp
                print("Opening WhatsApp...")
                if os.path.exists(PATHS['whatsapp_shortcut']):
                    os.startfile(PATHS['whatsapp_shortcut'])
                else:
                    print("WhatsApp shortcut not found - skipping")

                # Open Instagram
                print("Opening Instagram...")
                if os.path.exists(PATHS['instagram_shortcut']):
                    os.startfile(PATHS['instagram_shortcut'])
                else:
                    print("Instagram shortcut not found - skipping")

                # Open Spotify song
                print("Opening Spotify song...")
                webbrowser.open(SPOTIFY_SONG_URL)

                time.sleep(2)

                # Terminate Rainmeter
                print("Terminating Rainmeter...")
                os.system('taskkill /F /IM Rainmeter.exe')

                time.sleep(0.5)

                speak("All done. Going offline.")
                print("Exiting script...")
                sys.exit(0)

        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            time.sleep(2)

    except sr.WaitTimeoutError:
        pass
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(1)
