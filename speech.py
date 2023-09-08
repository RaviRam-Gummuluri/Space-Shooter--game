import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import webbrowser
#import pywhatkit


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 196)
engine.setProperty('volume', 2.7)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)
    try:
        print("Recognising...")
        Query = r.recognize_google(audio,language='en-in')
        print(f"User said: {Query}")
        speak(Query)
    except Exception as e:
        speak("Say that again please....")
        return "None"
    return Query
def wish():
    hour=int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("good morning")
    elif hour >= 12 and hour <= 17:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("Hi sir!,I am jarvis sir.how can i help you")







if __name__=="__main__":
    wish()
    speak("please! Tell me your name sir!")
    speak("ravi or hemanth")
    person = takecommand().lower()
    if 'ravi' in person:
        speak("Hi ravi sir!,Do you want to play space invaders")
    elif 'hemanth' in person:
        speak("Hi hemanth sir!,Do you want to play space invaders")
    else:
        speak(f"Hi {person} sir!,Do you want to play space invaders")

    response=takecommand().lower()
    if 'yes' in response:
        speak("lets,start the game")
    if 'no' in response:
        speak("you quit the game!")

    #takecommand()
    #speak('Hey Hemanth!,how can i help you')
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak("please tell sir!,what I need to search in wikipedia.....")
            speak("Searching Wikipedia.....")

            query=query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")


        if 'right' in query:
            speak("scapeship is moving right")
        elif 'left' in query:
            speak('scapeship is moving left')
        elif 'up' in query:
            speak('spaceship is moving up')
        elif 'down' in query:
            speak('spaceship is moving down')

        else:
            webbrowser.open(query)

