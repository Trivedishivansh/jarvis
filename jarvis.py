import speech_recognition as sr
import pyttsx3
import pywhatkit as kit
import wikipedia
import datetime
import webbrowser
import os

# Initialize the speech engine
engine = pyttsx3.init()

def speak(text):
    """Function to make the assistant speak."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Function to recognize speech."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query.lower()
    except Exception as e:
        print("Sorry, I didn't get that.")
        return None

def wish_user():
    """Function to greet the user based on time."""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("I am your assistant, how can I help you today?")

def execute_command(query):
    """Function to execute commands based on the user's query."""
    if 'play' in query:
        song = query.replace('play', '')
        speak(f'Playing {song}')
        kit.playonyt(song)
    
    elif 'search' in query:
        query = query.replace('search', '')
        speak(f'Searching for {query}')
        kit.search(query)
    
    elif 'time' in query:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {time}")
    
    elif 'open' in query:
        if 'youtube' in query:
            webbrowser.open('https://www.youtube.com')
        elif 'google' in query:
            webbrowser.open('https://www.google.com')
        else:
            speak("I can only open YouTube or Google for now.")
    
    elif 'wikipedia' in query:
        query = query.replace('wikipedia', '')
        speak(f"Searching Wikipedia for {query}")
        result = wikipedia.summary(query, sentences=1)
        speak(result)
    
    elif 'how are you' in query:
        speak("I'm doing great, thank you for asking!")
    
    elif 'exit' in query:
        speak("Goodbye! Have a nice day.")
        exit()

if __name__ == "__main__":
    wish_user()

    while True:
        query = listen()
        
        if query:
            execute_command(query)
            
