import pyttsx3 as p
import speech_recognition as sr
import wikipedia
import pyjokes
import datetime
import webbrowser
import os
import cv2
import requests
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
import psutil

cam=cv2.VideoCapture(0)

cv2.namedWindow("Python webcam screenshot app")

img_counter=0

Engine=p.init()
voices=Engine.getProperty('voices')
Engine.setProperty('voice',voices[1].id)
rate=Engine.getProperty('rate')
Engine.setProperty('rate',180)


def speechtx(x):
   
    Engine.say(x)
    Engine.runAndWait()

def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>-0 and hour<12:
        speechtx("Good morning!")

    elif hour>=12 and hour<18:
        speechtx("Good afternoon!")

    else:
        speechtx("Good evening!")

    speechtx("I am pottor. Please tell me how may i help you?")

def sptext():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
        try:
            print("recognizing...")
            data=r.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not understand")


if __name__== '__main__':
    wish()

    #if sptext().lower() == "hety pottor":

    while True:


        data1= sptext().lower()
        
        if 'your name' in data1:
            name="My name is pottor, what can i do for you sir"
            speechtx(name)
            print(name)

        elif 'old are you' in data1:
            age="I am 2 days old , so technically i am pretty young . But iahve learned so much!"
            speechtx(age)
            print(age)


        elif 'time' in data1:
            time=datetime.datetime.now().strftime("%I%M%p")
            speechtx(time)
            print(time)

        elif 'youtube' in data1:
            webbrowser.open("https://www.youtube.com/")

        elif 'facebook' in data1:
            webbrowser.open("https://www.facebook.com/")

        elif 'instagram' in data1:
            webbrowser.open("https://www.instagram.com/")

        elif 'joke' in data1:
            joke_1=pyjokes.get_joke(language="en",category="neutral")
            speechtx(joke_1)
            print(joke_1)

        elif 'play music' in data1:
            music='C:\\Users\\Pratik Dey\\OneDrive\\Documents\\song'
            songs=os.listdir(music)
            print(songs)
            os.startfile(os.path.join(music,songs[0]))

        elif 'temperature' in data1:
            search="temperature in delhi"
            url=f"https://www.google.com/search?q={search}"
            re=requests.get(url)
            data=BeautifulSoup(re.text,"html.parser")
            temp=data.find("div",class_="BNeawe").text
            speechtx(f"current{search} is {temp}")

        elif 'wikipedia' in data1:
            speechtx("searching wikipedia...")
            data1=data1.replace("wikipedia","")
            results=wikipedia.summary(data1,sentences=2)
            speechtx("According to wikipedia")
            print(results)
            speechtx(results)

        elif "how much battery left" in data1:
            battery=psutil.sensors_battery()
            percentage=battery.percent
            speechtx(f"sir our system have {percentage} percent battery")
            if percentage>=75:
                speechtx("We ahve enough power to continue")
            
            elif percentage>=40 and percentage<=75:
                speechtx("Now you sjould connect charging point")

            elif percentage<40:
                speechtx("Enough!Now its high time to connect to charging point and stop doing your work")

        elif 'actiavte how to do mod' in data1:
            speechtx("How to do mod is activated")
            while True:
                speechtx("Please tell me what you want to know")
                how = takecommand()
                try:
                    if "exit" in how or "close" in how:
                        speechtx("Okay sir , how to do mod is closed")
                        break

                    else:
                        max_results=1
                        how_to = search_wikihow(how,max_results)
                        assert len(how_to)==1
                        how_to[0].print()
                        speechtx(how_to[0].summary)

                except Exception as e:
                    speechtx("sorry sir , i am not able to find this")

        elif 'webcam' in data1:

            ret,frame = cam.read()

            if not ret:
                print("failed to grab frame")
                break

            cv2.imshow("test",frame)

            k=cv2.waitKey(1)

            if k%256 == 27:
                print("Escape hit,closing the app")
                break

            elif k%256 == 32:
                img_name="opencv_frame_{}.png".format(img_counter)
                cv2.imwrite(img_name,frame)
                print("Screenshot taken")
                img_counter+=1
                cam.release()
                #cam.destroyAlWindows()                


            elif 'exit' in data1:
                    
                speechtx("Thank you")
                print(speechtx)
                break

    