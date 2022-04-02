import speech_recognition as sr
import pyttsx3
import datetime
import time
from subprocess import *


print('Loading your voice assistant')

engine=pyttsx3.init('sapi5')
rate = engine.getProperty('rate')
voices = engine.setProperty('rate',170)
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            #print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

speak("Loading your AI voice assistant")
wishMe()

if __name__=='__main__':


    while True:
        speak("Tell me. how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your voice assistant is shutting down. Good bye and Have a Nice day')
            print('your voice assistant is shutting down,Good bye')
            break

        elif 'launch tool' or 'open tool' in statement:
            print("opening virtual mouse...")
            procmouse = Popen('python main.py')
            speak("virtual tool is open now")
            time.sleep(3)



time.sleep(3)
