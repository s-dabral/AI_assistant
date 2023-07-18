import speech_recognition as sr
import os

import webbrowser

import pyttsx3
import openai

import subprocess
import sys


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1  # if there is pause of 1 sec, the listening will stop
        r.energy_threshold = 100  # energy smaller than 100 will not be recognizable
        audio = r.listen(source, 0, 5)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            print("Could not understand audio.")
            return ""
        except sr.RequestError as e:
            print("Error occurred; {0}".format(e))
            return ""


if __name__ == '__main__':
    say("What you want me to do, sir?")
    webbrowser.register('chrome', None,
                        webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
    webbrowser.get('chrome')

    while True:
        print("Listening")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["google", "https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                webbrowser.open(site[1])
                say(f"Opening {site[0]}")



        if 'open music' in query:
            musicPath = "C:/Users/HP/Downloads/song1.mp3"

            # Platform-specific command to open the music file using the default associated program
            if sys.platform.startswith('darwin'):  # macOS
                subprocess.run(['open', musicPath])
            elif sys.platform.startswith('win32'):  # Windows
                subprocess.run(['start', musicPath], shell=True)
            elif sys.platform.startswith('linux'):  # Linux
                subprocess.run(['xdg-open', musicPath])



