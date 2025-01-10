'''
1) speak()
2) wishMe()
3) take command()
''' 

import pyttsx3 # python module
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5') #---->used to take voices as inputs or to use in build windows voices
voices = engine.getProperty('voices')
# print(voices) #prints the system voices
# print(voices[0].id) #this is the voice of david whose id is 0
# print(voices[1].id) #this is the voice of zira whose id is 1
engine.setProperty('voice',voices[0].id)
# engine.setProperty('voice',voices[1].id)



def speak(audio): # this function enables the computer to speak 
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour= int(datetime.datetime.now().hour) #--------> importing date time module and getting only the times hour 
    if hour>=0 and hour<=12:
        speak("Good Morning!")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        
    else:
        speak("Good Evening!")
    
    speak("I am jarvis sir. please tell me how may i help you")
    
def takeCommand(): #----> It Takes Microphone's Input From the user and returns string as a output
    
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold =1 #----> this is the pause time of the user speaking value
        audio =r.listen(source) #-->this all are comming from speechRecognition module
    
    try:
        print("Recognizing.....")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
    
    except Exception as e:
        # print(e)
        
        print("Say that Again please!......")
        return "None"
    
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password-here')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()
    
       
if __name__ == "__main__": #-----> this is the main function 
    # speak("Aniket is a Good Boy")
    wishMe()
    while(True):
    # if 1: #----> for one time execution of jarvis
        query=takeCommand().lower()
    
        #logics for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia.....')
            query = query.replace("wikipedia", "") #----> removing the word wikipedia from the query and searching the query on google
            results =wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results) #---->prints the searched result
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query :
            webbrowser.open("google.com")
        
        elif 'open flipkart' in query:
            webbrowser.open("flipkart.com")
        
        elif 'open amazon' in query :
            webbrowser.open("amazon.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'play music' in query:
            music_dir = 'C:\\Users\\anike\\Music'
            songs= os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0])) # here we can use the random module to generate random nos and use that random no to play random songs
        
        elif 'the time' in query :
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")
            
        elif 'open code' in query:
            codePath="C:\\Users\\anike\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'email to aniket' in query : # ----> we can use dictionary here to dtore different names and email addresses
            try:
                speak("what should i say!")
                content=takeCommand()
                to= "aniketyourEmail@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            
            except Exception as e: #--> for sending the email only i have to give acess to the less secure apps to the email aniketraj1274@gmail.com
                print(e)
                speak("Sorry my friend aniket . I am not able to send this email")
                
                
        elif 'close' or 'exit' or 'quit' or 'stop' in query:
            exit(0)
            
        
        
             
        
        
            
            