import speech_recognition as sr
import os
import webbrowser
import pyttsx3
import openai
import subprocess
import sys
import datetime




#For selecting the voice type

engine = pyttsx3.init()
voices=engine.getProperty('voices')
selected_voice_idx = 1
engine.setProperty('voice', voices[selected_voice_idx].id)



def say(text, rate= 100):

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


def play_music(song_list, query):
    for song_info in song_list:
        if query.lower() in f"play {song_info[0]}".lower():
            music_path = song_info[1]

            if sys.platform.startswith('darwin'):  # macOS
                subprocess.run(['open', music_path])
            elif sys.platform.startswith('win32'):  # Windows
                subprocess.run(['start', music_path], shell=True)
            elif sys.platform.startswith('linux'):  # Linux
                subprocess.run(['xdg-open', music_path])
            break
    else:
        print("Song not found.")


def open_application(application_name):
    for app_info in applications:
        if application_name.lower() in app_info[1].lower():
            try:
                subprocess.Popen(app_info[0])
                print(f"Opening {app_info[1]}...")
                return True
            except Exception as e:
                print(f"Error occurred: {e}")
                return False

    print("Application not found.")
    return False


sites = [["youtube", "https://www.youtube.com"], ["google", "https://www.google.com"],
         ["leetcode", "https://www.leetcode.com"],
         ["geeks for geeks", "https://www.geeksforgeeks.com"], ["github", "https://www.github.com"],
         ["facebook", "https://www.facebook.com"],
         ["instagram", "https://www.instagram.com"], ["erp", "https://student.gehu.ac.in/"],
         ["aniwatch", "https://www.aniwatch.to"],a
         ["weather report", "https://www.accuweather.com"], ["gmail", "https://www.gmail.com"],
         ["coursera", "https://www.coursera.org"]]


applications = [
    [r"D:\setups\telegram\Telegram Desktop\Telegram.exe", "Telegram"],
    [r"D:\Applications\Application2\application2.exe", "Application 2"],

]




if __name__ == '__main__':
    say("Hello Sir .......... My name is Ava ............... I am a basic AI assistant ...................What you want me to do, sir?")
    webbrowser.register('chrome', None,
                        webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
    webbrowser.get('chrome')

    while True:
        print("Listening")
        query = takeCommand()

        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                webbrowser.open(site[1])
                say(f"Opening {site[0]} as per your command sir ....")


        if 'open music' in query:
            song_list = [["song one", r"C:\Users\HP\Downloads\song1.mp3"], ["song two", r"C:\Users\HP\Downloads\song2.mp3"]]
            say("Sure! Please tell me the name of the song you want to play")
            user_input = takeCommand()
            play_music(song_list, user_input)

        if "time" in query:
            strfTime=datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir the time is {strfTime}")

        if "open" in query.lower():
            # Extract the application name from the query
            application_name = query.replace("open", "").strip()
            if application_name:
                if open_application(application_name):
                    continue;



