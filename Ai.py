import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pywhatkit
import smtplib
import pyjokes
import webbrowser

ai='Siri' #initializing the name of AI
master='master' #initializing the master
flag= True

#setting speech engine
engine=pyttsx3.init('sapi5') #sapi5 is used for windows 
voice=engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)  #for male voice set index[0] and for female voice set index[1]
engine.setProperty('rate', 180) #setting the rate of the voice

#for converting text to speech
def speak(text):
    engine.say(text) #speaks out the string passed to it
    engine.runAndWait() #waits until the say() completes its task and then moves to next step  

#Wishing the Master
def wishMaster():
    currentTime = datetime.datetime.now()
    print("Date : {} and Time : {}".format(currentTime.strftime("%d/%m/%Y"),currentTime.strftime("%I:%M:%S %p"))) #displays the currrent date and time in 12Hrs format
    h=datetime.datetime.now().hour #stores the current time in hour in 24Hrs format
    '''
    Wishing the master according to the current time 
    '''
    if h>=0 and h<12:
                speak('Good morning '+master)
    elif h>=12 and h<16:
        speak('Good afternoon '+master)
    else:
        speak('Good evening '+master)
    print('How may I help you.....?')
    speak('How may I help you.....?')

#for sending automated mail from master
def sendMail(body):
    server =  smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    speak('Enter your email address')
    username=input('Enter your email address: ')
    speak('Enter your password:')
    password=input('Enter your password: ')
    server.login(username,password)
    to=input('Enter destination email address')
    server.sendmail(username,to,body)
    server.close()

#For takig the command in the form of audio
def listenMasterCommand():
    rec = sr.Recognizer() #A class that implements different API methods
    try:
        with sr.Microphone() as source: # Reading Microphone as source
            print(f'{ai} listening...')
            rec.adjust_for_ambient_noise(source)  # this helps adjust the recognizer sensitivity to ambient noise
            audio = rec.listen(source)
            
            command = rec.recognize_google(audio,language='en-in')
            command = command.lower() #This helps comparing the text of the command
            command = command.replace(ai , '') #for good visualization in command printing we remove ai name from our command
            print(f'Master command:{command}\n')
    except: #if any exception is raised by recognize_google() just ignore it
        pass
    return command


#Basic intialization
print('Initializing '+ai+'........')
speak('Initializing '+ai)
wishMaster()


