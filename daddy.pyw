import speech_recognition as sr
import os
import pyttsx3
import sys
import time

# ------------------ TTS SETUP ------------------
engine = pyttsx3.init()
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)


def speak(text):
    engine.say(text)
    engine.runAndWait()


recognizer = sr.Recognizer()
recognizer.dynamic_energy_threshold = False
recognizer.energy_threshold = 120

WAKE_PHRASES = [
    "wake up daddy is home",
    "wake up daddy",
    "daddy is home"
]


RAINMETER_PATH = r"C:\Program Files\Rainmeter\Rainmeter.exe"

CHROME_PATH = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
PROJECT_FOLDER = r"C:\xampp\htdocs\Corona Admin Panel"


while True:
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.8)
            audio = recognizer.listen(source, timeout=4, phrase_time_limit=6)

        try:
            spoken = recognizer.recognize_google(audio).lower().strip()
            print("Heard:", spoken)

            if WAKE_PHRASE in spoken:
                speak("Daddy's home. Launching everything now.")

                os.startfile(CHROME_PATH)
                os.system(f'code "{PROJECT_FOLDER}"')
                os.system("notepad")
                os.system("calc")

                time.sleep(1)

                os.system(f'"{RAINMETER_PATH}" !Quit')

                speak("All done. Going offline.")

                sys.exit(0)

        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            time.sleep(2)

    except sr.WaitTimeoutError:
        pass
    except Exception as e:
        time.sleep(1)
