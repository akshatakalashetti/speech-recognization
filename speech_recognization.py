import pyttsx3

# pyttsx3 =python text to aspeech
import speech_recognition as speech_recognitionim
import speech_recognition as sr
# speech_recognitionim = used to convert spoken words into  text and words on API's
import datetime
# datetime = used to work with date and time
import wikipedia
# automate_wikipedia = used to automate and work with wikipedia
import webbrowser
#webbrowser= used for to automate webbrowser
import os
# os = used  to work/interaxct with operating system
import smtplib
#sending mails
print("18 line .........................................")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # 1 for female , 0 for male
print("22 line .........................................")
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    
    hour = int(datetime.datetime.now().hour)
    print(hour)
    
    if hour >=0 and hour<=12:
        speak("good morning")
    if hour >12 and hour<=16:
        speak("good afternoon")
    if hour >16 and hour<=20:
        speak("good evening")    
    if hour >20 and hour<24:
        speak("good night")
    speak("how are you?")
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening.........")
        r.pause_threshold = 1
        print("47...................")
        r.adjust_for_ambient_noise(source, duration=5)
        audio = r.listen(source)
        print("49..............")
    
        try:
            print(" Recognizing your voice..........")
            query = r.recognize_google(audio, language='en-in')
            print(f"my friend you said : {query}\n")
            speak("my friend you said :",query)

        except:
            print("could please repeat it again......")
            return "None"

    return query

# to excess email
def sendEmail(to,content):
    server =  smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('shinchandoremon2001@gmail.com', 'shinchan@1995')
    server.sendmail('shinchandoremon2001@gmail.com', to, content)
    server.close()


wishme()
query = takecommand().lower()
if 'open wikipedia' in query:
    speak('searching wikipedia....')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to wikipedia ")
    print(results)
    speak(results)
if 'open Notepad' in query:
    npath ="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories"
    os.startfile(npath)

elif 'open paint' in query:
    npath =" "
    os.startfile(npath)

elif 'open Youtube' in query:
    webbrowser.open('youtube.com')
    
elif 'open Great learning academy' in query:
    webbrowser.open('https://www.codecademy.com/learn')

elif 'open google' in query:
    webbrowser.open('google.com')
    
elif 'tell me the time' in query:
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The current time is {strTime}")
    print(strTime)


elif 'open Great learning youtube channel' in query:
    webbrowser.open('https://www.youtube.com/c/GreatLearningOfficial')

elif 'email to friend' in query:
    try:
        speak("what should i send? ")
        content = takecommand()
        to = "akshatakalashetty2001@gmail.com"
        sendEmail(to, content)
        speak("your mail sent successfully")
    
    except Exception as e:
        print(e)
        speak("mail is not sent")
