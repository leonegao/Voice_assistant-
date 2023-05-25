import ctypes
import getpass
import subprocess

import PIL
import face_recognition
import folium
from tkinter import simpledialog
from opencage.geocoder import OpenCageGeocode
import os
import pygame
import webbrowser

import Annex
from Db import insert_record, read_data, read_dataAll, delete_element, update_elements, selectPoneNumber
import phonenumbers
from phonenumbers import geocoder
import tkinter as tk
from tkinter import *
import pyjokes
import pywhatkit
import wikipedia
import wolframalpha
from PIL import ImageTk, Image
from send_sms import *
from Annex import *

# setting chrome path
key = 'e71dd2d46c0a49ca93993a91c1ffd965'  # opencage key
chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
app = wolframalpha.Client("JPK4EE-L7KR3XWP9A")  # API key for wolframalpha


def getAngel():
    while True:
        request = command_copy()  # Request
        hour = int(datetime.datetime.now().hour)  # casting  hour
        if exists(['phone location', 'target', 'person location'], request):  # get phone global location

            ROOT = tk.Tk()

            ROOT.withdraw()
            # the input dialog
            USER_INP = simpledialog.askstring(title="Test",
                                              prompt="What's the number?:")
            if USER_INP is not None and len(USER_INP) == 13:

                personNumber = phonenumbers.parse(USER_INP, "CH")
                location = geocoder.description_for_number(personNumber, 'en')
                # servProvider = carrier.name_for_number(personNumber, 'RO')
                geo = OpenCageGeocode(key)
                query = str(location)
                result = geo.geocode(query)
                formats = result[0]['formatted']
                L = result[0]['geometry']['lat']
                Ln = result[0]['geometry']['lng']
                my_map = folium.Map(location=[L, Ln], zoom_start=9)
                folium.Marker([L, Ln], popup=location).add_to(my_map)
                my_map.save("targetLocation.htm")

                speak(f'that person is in {location}')

            # speak(servProvider)

            else:
                speak('invalid number, try again please')
                break
        elif exists(['my mp3 list', 'my mp3', 'mp3'], request):

            play_songs()

        elif exists(['send a message, message send', 'wm'], request):
            speak('what number do you want to send the message')
            number = simpledialog.askstring(title="Test",
                                            prompt="What's the number?:")

            speak('what is the message')
            message = takeCommand()
            speak('that is the correct message')
            ms = takeCommand()
            if exists(['yes', 'sure', 'confirmation'], ms):
                speak('what time do you want to sell the message please')
                messageTime = simpledialog.askstring(title="Test",
                                                     prompt="What's the message Time?:")
                MT = int(messageTime)
                speak('minutes please')
                messageMin = simpledialog.askstring(title="Test",
                                                    prompt="What's the second?:")
                MM = int(messageMin)
                WhatsApp(number, message, MT, MM)
            else:
                speak('Could please try again')

        elif 'play' in request:  # play YouTube videos
            play = request.replace('play', '')
            speak(f"that is your request{play}")
            play_music = takeCommand()
            if exists(['yes', 'sure', 'good', 'positive', 'please'], play_music):
                pywhatkit.playonyt('play' + play)
                break
            else:
                speak('try again please')
                # taking a selfie
        elif exists(['take a photo', 'take a selfie', 'take my photo', 'take photo', 'take selfie'], request):
            takephoto = Annex.camera()
            Location = takephoto.takePhoto()
            os.startfile(Location)
            del takephoto
            speak("Captured picture is stored in Camera folder.")
            break
        elif exists(['write a note', 'take a note', 'take note', 'write note'], request):
            speak('In your command')
            note = takeCommand()
            file = open('note.txt', 'w')
            speak('that is the correct note')
            correct = takeCommand()

            if exists(['yes', 'positive', 'sure'], correct):
                time_ = datetime.datetime.now().strftime("%m/%d/%Y")

                file.write(note)
                file.write(":")
                file.write(time_)
                speak('the note be add thanks')
                break
            else:
                speak('could you please try again')

        elif exists(['read  my note', 'read the note', 'read my note'], request):
            speak('do you want me to read your notes')
            notes = takeCommand()
            if exists(['yes', 'sure', 'please', 'positive'], notes):
                f = open("note.txt", "r")
                a = True
                while a:
                    speak(f.readline())
                    if not f:
                        speak('end of file')
                        a = False
                f.close()

            else:
                speak('could you please try again')

        elif exists(['add student', 'insert student', 'new student'], request):  # Add student in the database
            speak('id number please')
            ID = simpledialog.askstring(title="Test",
                                        prompt="What's the id?:")
            id_int = int(ID)
            speak('name please')
            name = simpledialog.askstring(title="Test",
                                          prompt="What's the name?:")
            speak('email please')
            email = simpledialog.askstring(title="Test",
                                           prompt="What's the email?:")
            speak('whatsapp number please')
            WhatsApp = simpledialog.askstring(title="Test",
                                              prompt="What's the whatsapp?:")

            speak('weight please')
            weight = simpledialog.askstring(title="Test",
                                            prompt="What's the weight?:")

            if ID is not None and name is not None and email is not None and weight is not None:
                insert_record(id_int, name, email, WhatsApp, weight)
                speak('the records been inserted in the database')
            else:
                speak('make sure that the values do you insert is not in the database and are not null values,'
                      'please try '
                      'to '
                      'insert the values again')
        elif exists(['students records', 'how many students'], request):  # check how many students I have in the
            # database
            speak('do you what me to show you all the database records')
            records = takeCommand()
            if exists(['yes', 'sure', 'positive'], records):
                read_dataAll()
            else:
                speak('what do you want me to do please')
        elif exists(['check email address', 'email verification'], request):  # email verification
            speak('what is your email please')
            email = simpledialog.askstring(title="Test",
                                           prompt="What's the email?:")
            read_data(email)
        elif exists(['delete row ', 'delete from database'], request):  # Delete row from the database
            speak('what is the Id email you would like to delete please')
            ID = simpledialog.askstring(title="Test",
                                        prompt="What's the email?:")
            delete_element(ID)
            speak('The Id was deleted')

        elif exists(['update the email', 'email update', 'update email'], request):  # UPDATE STUDENT EMAIL
            speak('what is the new email, please')
            new_email = simpledialog.askstring(title="Test",
                                               prompt="What's the actual email?:")
            speak('what is the actual email, please')
            actual_email = simpledialog.askstring(title="Test",
                                                  prompt="What's the new email?:")
            update_elements(new_email, actual_email)
            speak('email been update thanks')

        elif exists(['creator', 'inventor', 'designer', 'design', 'create your code'], request):  # angel creator
            speak("My creator is Leo, a cage fighter from Brazil")

        elif exists(['explain', 'do you know', 'information about'], request):  # get explanation
            # from
            # wikipedia
            if 'explain' in request:
                thing = request.replace('explain', '')
                speak(f'do you want to know the explanation of{thing}')
                explain = takeCommand()
                if exists(['yes', 'sure', 'positive'], explain):
                    info = wikipedia.summary(thing, 5)
                    speak(info)
                    tkinter.messagebox.showinfo(title='ANSWER', message=info)
                else:
                    speak('Try again please')

            elif 'do you know' in request:
                person = request.replace('do you know', '')
                speak(f'do you want to know {person}')
                explain = takeCommand()
                if exists(['yes', 'sure', 'positive'], explain):
                    info = wikipedia.summary(person, 5)
                    speak(info)
                    tkinter.messagebox.showinfo(title='ANSWER', message=info)
                else:
                    speak('Try again please')

            elif 'information about' in request:  # get explanation from wikipedia
                about = request.replace('information about', '')
                speak(f'Do you like to know information about {about}')
                ask = takeCommand()
                if exists(['yes', 'sure', 'positive'], ask):
                    info = wikipedia.summary(about, 5)
                    speak(info)
                    tkinter.messagebox.showinfo(title='ANSWER', message=info)
                else:
                    speak('Try again please')
            else:
                speak('could you please try again')

        elif 'joke' in request:  # python jokes
            speak(pyjokes.get_joke())

        elif exists(['finish now', 'off now', 'end now', 'off'], request):  # going of line
            speak("going offline")
            exit()
        elif 'open youtube' in request:  # open youtube
            speak("Youtube")
            webbrowser.open("youtube.com")
            break

        elif 'open google' in request:  # open google
            speak("Google")
            webbrowser.open("google.com")
            break
        elif 'open bloomberg' in request:  # open bloomberg
            speak("Here you go to bloomberg")
            webbrowser.open("www.bloomberg.com")
            break

        elif exists(['search for', 'look for'], request):  # search in google
            search = request.split("for")[-1]
            url = f"https://google.com/search?q={search}"
            webbrowser.get().open(url)
            speak(f'The following is what I found {search} on google')
            break
        elif 'youtube' in request:  # search in YouTube
            search = request.split("for")[-1]
            url = f"https://www.youtube.com/results?search_query={search}"
            webbrowser.get().open(url)
            speak(f'The following is what I found {search} on youtube')
            break
        elif exists(['good morning', 'good afternoon', 'good evener', 'good evening'], request):
            OP(request)
        elif exists(["how are you", "how are you doing", 'hi', 'hello'], request):
            OP(request)

        elif 'open stackoverflow' in request:  # open stackoverflow
            speak("Here you go to Stack Over flow")
            webbrowser.open("stackoverflow.com")
            break
        elif exists(
                ["what is my exact location", "my location", "my current location", "exact current location"],
                request):  # show my location in Google Maps
            url = "https://www.google.com/maps/search/Where+am+I+?/"
            webbrowser.get().open(url)
            speak("Showing your current location on google maps...")
            break
        elif exists(['the date'], request):  # find the date
            strDay = datetime.date.today().strftime("%B %d, %Y")
            speak(f"Today is {strDay}")
        elif exists(['what day it is', 'what day is today', 'which day is today', "today's day name please"],
                    request):  # find the day
            speak(f"Today is {datetime.datetime.now().strftime('%A')}")
        elif exists(['open notepad plus plus', 'open notepad++', 'open notepad ++'], request):  # open notepad
            speak('Opening notepad++')
            os.startfile(r"C:\Program Files\Notepad++\notepad++.exe")
            break
        elif exists(['eclipse', 'start eclipse'], request):  # open eclipse
            speak('Opening eclipse')
            os.startfile(r'C:\Users\negao\eclipse\java-2021-12\eclipse\eclipse.exe')
            break
        elif exists(['filezilla', 'start filezilla'], request):  # open filezilla
            speak('Opening filezilla')
            os.startfile(r'"C:\Program Files\FileZilla FTP Client\filezilla.exe"')
            break
        elif exists(['bitcoin prediction', 'what is the bitcoin close price', 'what is your prediction for bitcoin',
                     'predict bitcoin price'], request):  # get the close ,heighten and lower price of bitcoin

            bitOpenPrice = float(openPrice)
            speak('the actual price is')
            speak(price)
            tkinter.messagebox.showinfo(title='BITCOINS', message=price)
            speak('the close price of bitcoin will be')
            bitcoin(bitOpenPrice)
            speak('the highers  price in the day will be')
            hPrice(bitOpenPrice)
            speak('the lower price in the day will be')
            lPrice(bitOpenPrice)
        elif exists(['alarm', 'my alarm', 'set alarm'], request):
            alarm()
        elif exists(['how is the weather in', 'how the weather looks like in ', 'weather in'],
                    request):  # check the word city weather
            try:

                search = request.split("in")[-1]
                speak('that is the city correct name')
                speak(search)
                cityCorrect = takeCommand()
                if exists(['yes', 'please', 'sure', 'correct'], cityCorrect):
                    weather(search)
                else:
                    speak('could you please try again')
            except:
                speak("Internet Connection Error")

        elif exists(['down the system', "shutdown the computer", "computer down"], request):  # turn off the computer
            speak('do you want to  shutdown the computer')
            shutdown = takeCommand()
            if shutdown == 'yes':
                os.system("shutdown /s /t 1")
            else:
                speak('please try again')
        elif exists(["lock computer", "lock", "lock system"], request):  # lock the system
            speak('lock computer')
            ctypes.windll.user32.LockWorkStation()

            break
        elif exists(['sleep mode computer', 'computer  sleep', 'sleep now'], request):  # sleep mode the computer
            speak(' Are you sure do you want to activate the sleep mode')
            sleepComputer = takeCommand()
            if exists(['yes', 'sure', 'please', 'positive'], sleepComputer):
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            else:
                speak('ok')

        # maths question using wolframalpha api
        elif exists(['+', '-', '*', 'x', '/', '√', 'plus', 'add', 'minus', 'subtract', 'divide', 'multiply', 'divided',
                     'power', 'square root', 'modulo', 'mod', '%',
                     'multiplied'], request):
            try:
                res = app.query(request)
                speak(next(res.results).text)
                response = next(res.results).text
                tkinter.messagebox.showinfo(title='ANSWER', message=response)


            except:
                OP(request)
        # My name is from the username
        elif exists(['what is my name', 'tell me my name', "i don't remember my name", 'what is my nickname'], request):
            speak("Your name is " + str(getpass.getuser()))
        elif exists(['deeplearning book', 'python pdf', 'book'], request):
            b = 'deeplearningwithpython.pdf'
            readPdf(b)
        elif "restart" in request:  # restart the computer
            subprocess.call(["shutdown", "/r"])
        elif exists(["screenshot", "take a screenshot"], request):  # screenshot
            speak('tell me  the name of the picture,give me a second')
            picName = takeCommand()
            pic = pyautogui.screenshot()
            pic.save(f"{picName}.png")
            speak("The screenshot is save in our main folder")
        elif exists([" what is", "who is", 'how to stop', 'how to make'],
                    request):  # sciences question
            client = app
            res = client.query(request)

            try:
                response = next(res.results).text
                speak(response)
                tkinter.messagebox.showinfo(title='ANSWER', message=response)
            except StopIteration:
                OP(request)

        elif 'volume up' in request:  # volume up 10 press
            for i in range(0, 10):
                pyautogui.press("volumeup")
        elif 'volume down' in request:  # volume down 10 press
            for i in range(0, 10):
                pyautogui.press("volumedown")
        elif exists(['bitcoin news', 'news bitcoin'], request):
            NewsFromBit()
        elif exists(['make a voice  message ', ' message voice ', 'call message'],
                    request):  # twilio voice message call using student db
            speak('Do you want to send a voice message to your student')
            studantTakeComand = takeCommand()
            if exists(['yes', 'sure', 'positive', 'please'], studantTakeComand):
                speak('email address please')
                email = simpledialog.askstring(title="Test",
                                               prompt="What's the email?:")
                studantNumber = selectPoneNumber(email)
                speak('calling the student')
                call(studantNumber)
            else:
                speak('give me the new number please')
                number = simpledialog.askstring(title="Test",
                                                prompt="What's the number?:")
                speak('calling the number')
                call(number)

        else:
            OP(request)


def main_program():
    root = Tk()

    def start(event):  # function to start the gui
        getAngel()

    root.title("Angel")
    ico = Image.open('M.jpg')
    photo = ImageTk.PhotoImage(ico)
    root.wm_iconphoto(False, photo)
    root.geometry("300x300")
    root.configure(bg='#000000')
    image1 = PIL.Image.open("M.jpg")  # Matrix img
    img = PIL.ImageTk.PhotoImage(image1)
    resized = image1.resize((350, 270))
    img = PIL.ImageTk.PhotoImage(resized)
    myLabel = Label(root, image=img)
    myLabel.image = img
    myLabel.place(x=0, y=0)
    button1 = tk.Button(root, text='Angel', fg='white', width=30, bg='#000000')  # Angel button
    button1.bind('<Button-1>', start)
    button1.pack(side=tk.BOTTOM)
    root.mainloop()


# Unlock the application with face recognition
if __name__ == '__main__':
    main_program()
