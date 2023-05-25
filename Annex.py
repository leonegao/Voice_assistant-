import random
import cv2
import PyPDF2
import pyttsx3
import speech_recognition as sr
import yfinance as yf
import datetime
import tkinter
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import requests
from tkinter import simpledialog
import os
import pygame
from twilio.rest import Client
import openai

# twilio sid value
sidValue = 'AC142d627820a74e0a3328e5860d5c5a9a'
# twilio token
tokenTwilio = 'c8bfca43edfd09d1f5f17630bd7b90ed'
# create a client
client = Client(sidValue, tokenTwilio)

# using the library audio music
pygame.init()
pygame.mixer.init()
keyNewApi = 'c89a91d369c748ca8b781f1b7f2a1658'
gear = pyttsx3.init()
listenerMe = sr.Recognizer()
# get price and volume from coin market API
headers = {
    'X-CMC_PRO_API_KEY': '1a2711d6-f7d6-4bdc-8b3b-aef01a81a0b5',
    'Accepts': 'application/json',
}
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': '5',
    'convert': 'USD'
}
json = requests.get(url, params=parameters, headers=headers).json()
coins = json['data']
volume = 0  # the volume of the day
price = 0  # the actual bitcoin price
for i in coins:  # loop over all coin available
    if i['symbol'] == 'BTC':
        volume = i['quote']['USD']['volume_24h']
        price = i['quote']['USD']['price']
# get the open price from yahoo
data = yf.download(tickers='BTC-USD', period='1d', interval='1d')  # get the open day from yahoo
openPrice = data['Open']


def command_copy():
    try:

        with sr.Microphone() as source:

            speak("Ready..")  # when angel is ready
            my_voice = listenerMe.listen(source)

            command = listenerMe.recognize_google(my_voice)  # getting the string text from the voice

            command = command.lower()  # make command to lower case

            if 'angel' in command:
                command = command.replace('angel', '')  # Angel must be in the command voice



    except:
        pass
    return command


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        speak("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        speak("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        speak(f"User said: {query}\n")

    except Exception as e:
        print(e)
        speak("Unable to Recognize your voice.")
        return "None"

    return query


def speak(talk):  # angel to speak
    gear.say(talk)
    gear.runAndWait()


def exists(terms, q):  # if have the term in the request
    for term in terms:
        if term in q:
            return True


def readPdf(b):  # function to read book pdf
    book = open(b, 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak('what page do you want to start please,give me a second')
    startPage = takeCommand()
    for num in range(int(startPage), pages):  # start with page 8 to the end of the pdf
        page = pdfReader.getPage(num)
        text = page.extractText()
        speak(text)


def bitcoin(opening):  # function to get the close price of the day
    strDay = datetime.date.today().strftime('%Y-%m-%d')
    df = yf.download('BTC-USD', start='2010-01-01', end=strDay)  # YY/MM/DD

    X = df[['Open', 'Volume']]
    y = df['Close']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    clf = LinearRegression()
    clf.fit(X_train, y_train)
    A = clf.predict([[opening, volume]])

    # The score of the model
    speak(A)
    tkinter.messagebox.showinfo(title='BITCOINS', message=A)
    S = clf.score(X, y)
    speak('the percentage to close in that price is')
    speak(S)


def hPrice(opening):  # function to get the height price of the day
    strDay = datetime.date.today().strftime('%Y-%m-%d')
    df = yf.download('BTC-USD', start='2010-01-01', end=strDay)  # YY/MM/DD

    X = df[['Open', 'Volume']]
    y = df['High']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    clf = LinearRegression()
    clf.fit(X_train, y_train)
    A = clf.predict([[opening, volume]])

    # The score of the model
    speak(A)
    tkinter.messagebox.showinfo(title='BITCOINS', message=A)


def lPrice(opening):  # function to get the lower price of the day
    strDay = datetime.date.today().strftime('%Y-%m-%d')

    df = yf.download('BTC-USD', start='2010-01-01', end=strDay)  # YY/MM/DD

    X = df[['Open', 'Volume']]
    y = df['Low']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    clf = LinearRegression()
    clf.fit(X_train, y_train)
    A = clf.predict([[opening, volume]])

    # The score of the model
    speak(A)
    tkinter.messagebox.showinfo(title='BITCOINS', message=A)


def weather(city):  # get the weather and city in the world
    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + \
          '&appid=0f46b9cf25e608b5a63b73898618c7fc&units=metric'
    response = requests.get(url).json()
    description = response['weather'][0]['description']
    speak(description)
    temp_c = int(response['main']['temp'])  # round the temperature
    speak('with temperature')
    speak(temp_c)
    speak('celsius')


class camera:  # take a photo and  create a folder called camera to store the pictures
    def __init__(self):
        self.result = None
        self.frame = None
        self.ret = None
        self.videoCaptureObject = None
        self.ImageName = None

    def takePhoto(self):
        self.videoCaptureObject = cv2.VideoCapture(0)
        self.result = True
        a = os.getcwd()
        if not os.path.exists("Camera"):
            os.mkdir("Camera")
        os.chdir(a + '\Camera')
        speak('what is your name please')
        imgName = simpledialog.askstring(title="Test",
                                         prompt="What's the name?:")
        self.ImageName = imgName + ".jpg"
        while self.result:
            self.ret, self.frame = self.videoCaptureObject.read()
            cv2.imwrite(self.ImageName, self.frame)
            self.result = False
        self.videoCaptureObject.release()
        cv2.destroyAllWindows()
        os.chdir(a)

        return "Camera\\" + self.ImageName


def deny():  # function to deny users
    speak('access deny')
    exit()


def welcome():  # function welcome
    speak('hi leo welcome back')


def stop():  # function stop audio mp3
    pygame.mixer.music.stop()


def pause():  # function stop audio mp3
    pygame.mixer.music.pause()


def play():  # function stop audio mp3
    pygame.mixer.music.play()


# music files path
path = './audio/'

# get music files
songs = os.listdir(path)

# filter mp3 files
songs = [fi for fi in songs if fi.endswith(".mp3")]


def play_songs():
    try:
        # pygame.mixer.music.set_volume(0.50)
        filename = random.choice(songs)
        # print('playing now {}'.format(filename))
        pygame.mixer.music.load(path + filename)

        while True:
            controller = simpledialog.askstring(title="Test",
                                                prompt="Enter play,pause or stop:")
            if controller.lower() == "pause":
                pause()
            elif controller.lower() == "stop":
                stop()
                break
            elif controller.lower() == "play":
                play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except ValueError:
        print('Excemption: {}', format(ValueError))


def alarm():  # Setting up the alarm
    Hours = simpledialog.askstring(title="Alarm",
                                   prompt="Enter the Hour Please:")  # choosing the hour
    alarmH = int(Hours)
    Min = simpledialog.askstring(title="Alarm",
                                 prompt="Enter the min:")  # choosing the min
    alarmM = int(Min)
    alarmAm = simpledialog.askstring(title="Alarm",
                                     prompt="am/ pm:")  # am or pm
    if alarmAm == "pm":  # if the user choose pm hour will be + 12
        alarmH += 12
    while True:
        if alarmH == datetime.datetime.now().hour and alarmM == datetime.datetime.now().minute:  # if hour is equal actual hour and min the music will start
            speak("playing")
            filename = "meditaion.mp3"
            pygame.mixer.music.load(path + filename)
            play()

            controller = simpledialog.askstring(title="Alarm",
                                                prompt="Enter stop:")
            if controller.lower() == "stop":  # stopping the music
                stop()
                break


# bitcoin  news
def NewsFromBit():
    # Bitcoin news api
    bitime = str(datetime.datetime.now().hour)
    main_url = "https://newsapi.org/v2/everything?q=bitcoin&from=" + bitime + "&sortBy=publishedAt&apiKey=c89a91d369c748ca8b781f1b7f2a1658"

    # fetching data in json format
    open_bbc_page = requests.get(main_url).json()

    # getting all articles in a string article
    article = open_bbc_page["articles"]

    # empty list which will
    # contain all trending news
    results = []

    for ar in article:
        results.append(ar["title"])

    for i in range(len(results)):
        speak(results[i])


def call(number):
    callnumber = client.calls.create(number, from_='+19289388444',
                                     url="https://handler.twilio.com/twiml/EHa4da13174e63d808ed70b4b9afe6e2aa")


def OP(request):
    # Set up the OpenAI API client
    openai.api_key = "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"

    # Set up the model and prompt
    model_engine = "text-davinci-003"
    prompt = request

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = completion.choices[0].text
    if response is not None:
        speak(response)
        tkinter.messagebox.showinfo(title='ANSWER', message=response)
    else:
        speak("try again please")
