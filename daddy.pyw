import speech_recognition as sr
import os
import pyttsx3
import sys
import time
import webbrowser


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
    "wake up that is home",
    "daddy is home",
    "wake up there is home"
]


RAINMETER_PATH = r"I:\Rainmeter"
CHROME_PATH = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
PROJECT_FOLDER = r"C:\Users\AL KARAM COMPUTER\Desktop\Project"
CHATGPT_PATH = r"C:\Users\AL KARAM COMPUTER\Desktop\ChatGPT - Shortcut.lnk"
SPOTIFY_SONG_URL = "https://open.spotify.com/track/0vmFuEhyHR8SbOhDFq021Y?si=e57fe30f3e814c72"
WHATSAPP_PATH = r"C:\Users\AL KARAM COMPUTER\Desktop\WhatsApp - Shortcut.lnk"
INSTAGAM_PATH = r"C:\Users\AL KARAM COMPUTER\Desktop\Instagram - Shortcut.lnk"


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
                print(" Wake phrase detected!")
                speak("Daddy's home. ")

                print("Opening Chrome...")
                os.startfile(CHROME_PATH)

                print("Opening VS Code...")
                os.system(f'code "{PROJECT_FOLDER}"')

                print("Opening ChatGPT...")
                try:
                    os.startfile(CHATGPT_PATH)
                except:
                    print("ChatGPT path not found - skipping")

                print("Opening WhatsApp...")
                try:
                    os.startfile(WHATSAPP_PATH)
                  #  os.system(WHATSAPP_PATH)
                except:
                    print("WhatsApp path not found - skipping")

                print("Opening Instagram...")
                try:
                    os.startfile(INSTAGAM_PATH)
                except:
                    print("Instagram path not found - skipping")

                print("Opening Spotify song...")
                webbrowser.open(SPOTIFY_SONG_URL)

                time.sleep(2)

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
