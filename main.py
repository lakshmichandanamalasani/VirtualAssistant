import speech_recognition as sr
import pyttsx3
import datetime as dt
import pywhatkit as pk
import wikipedia
import webbrowser
import ecapture

listener = sr.Recognizer()
speaker = pyttsx3.init()

""" RATE"""
rate = speaker.getProperty('rate')
print(rate)
speaker.setProperty('rate', 125)

def speak(text):
    speaker.say(text)
    speaker.runAndWait()

def wish():
    hour = int(dt.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak('good morning')
    elif hour > 12 and hour < 18:
        speak('good afternoon')
    else:
        speak('good evening')
wish()
speak('Hello, Alex here')

va_name = 'Alex'
def take_command():
    command=''
    try:
        with sr.Microphone() as source:
            print('listening')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command=command.lower()
            if va_name in command:
                command = command.replace(va_name+ '','')
                #print(command)
                #speak(command)
    except:
        print('check your microphone')
    return command

while True:
    user_command=take_command()
    if 'sleep' in user_command or 'shutdown' in user_command or 'stop' in user_command or 'break' in user_command:
        speak('see you again ')
        break
    elif 'time' in user_command:
        cur_time = dt.datetime.now().strftime('%I:%M %p')
        speak('the current time is ' + cur_time)
    elif 'play ' in user_command:
        user_command=user_command.replace('play','')
        speak('playing'+user_command)
        pk.playonyt(user_command)
    elif 'wikipedia' in user_command or 'who' in user_command :
        speak('searching in wikipdia')
        result=wikipedia.summary(user_command,2)
        print(result)
        speak(result)
    elif 'open youtube' in user_command:
        webbrowser.open('www.youtube.com')
    elif 'open stack overflow' in user_command:
        webbrowser.open('www.stackoverflow.com')
    elif 'open facebook' in user_command:
        webbrowser.open('www.facebook.com')
    elif 'open google' in user_command or 'google' in user_command or 'search' in user_command or 'open' in user_command:
        speak('opening in bing')
        cm = take_command().lower()
        webbrowser.open(f'{cm}')