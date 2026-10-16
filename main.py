import speech_recognition as sr  #to reduce the text of import speech recognition into sr as keyword use that'why
import webbrowser
import pyttsx3 
import musicLibrary
import requests
import os
from google import genai
# pip install pocketsphinex


recognizer = sr.Recognizer()
engine = pyttsx3.init()



def speak(text):
    engine.say(text) 
    engine.runAndWait()

def aiprocess(command):   
    client = genai.Client(api_key="Your api key")

    response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=command
)

    return response.text
    
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com", new=2)

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://Youtube.com")

    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link= musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=dd325f9329534e19bbc86f6c68d33760")


        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            for article in articles:
                speak(article["title"])



    else:
        #Let gemini ai handle the problem
       output =  aiprocess(c)
       speak(output)









if __name__=="__main__":
    speak("Initializing Jarvis.....")

    while True:
        #Listen for the wake word "jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        

        
        print("recognizing....")
        
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("ya ......")
                #Listen for the command
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
        