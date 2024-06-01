from http import server
from lib2to3.pgen2 import driver
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
# import getpass
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException
# options = webdriver.ChromeOptions()
# options.add_argument("user-data-dir=C:/Users/" + getpass.getuser() + "/AppData/local/Google/Chrome/User Data")
# driver = webdriver.Chrome(executable_path= "C:/Users/daund/OneDrive/Desktop/Project Jarvis/chromedriver.exe", chrome_options=options)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from from the user and returns strings output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login()
    server.sendmail('', to, content)
    server.close()

# def music(song):
#     speak("1 second")
#     driver.get("https://www.youtube.com/results?search_query=" + song)
#     delay = 3
#     myElem = WebDriverWait(driver , delay).until(EC.presence_of_element_located((By.ID, 'video-title')))
#     driver.find_element_by_css_selector("a[id='video-title-link']").click()
#     speak("Enjoy" + song)

if __name__ == "__main__":
    wishMe()
    while True:
     if 1:
        query = takeCommand().lower()

    # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        # elif 'play' in query:
        #     music(query.split('play')[1])

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = "C:\\Users\\daund\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = ""
            os.startfile(codePath)

        elif 'email to name' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = ""
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I couldn't send email to your friend.")