#Importing Libraries
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests, json , sys
import pyaudio
import os


r = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)

def engine_talk(text):
    engine.say(text)
    engine.runAndWait()
    

def user_commands():
    global command
    try:
        with sr.Microphone() as source:
             r.energy_threshold=12000
             r.adjust_for_ambient_noise(source,1.2)

             print("Start Speaking!!")
             voice = r.listen(source)
             command = r.recognize_google(voice)
             command = command.lower()
             if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command
    
    
def run_alexa():
    command = user_commands()
    if 'play' in command:
        song = command.replace('play', '')
        #print('New Command is' +command)
        #print('The bot is telling us: Playing' +command)
        engine_talk('Playing' +song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        engine_talk('The current time is' +time)
    elif 'who is' in command:
        name = command.replace('who is' , '')
        info =  wikipedia.summary(name, 1)
        print(info)
        engine_talk(info)
    elif 'joke' in command:
        engine_talk(pyjokes.get_joke())
    
    elif 'stop' in command:
        sys.exit()
    else:
        engine_talk('I could not hear you properly')
        
        
while True:
    run_alexa()