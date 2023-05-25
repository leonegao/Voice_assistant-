import pywhatkit as pwk
from Annex import *
import pyautogui


def Whatsapp(N, M, T, S):
    # using Exception Handling to avoid unexpected errors
    try:
        pwk.sendwhatmsg(N, M, T, S)
        pyautogui.press('enter')
        speak("Message Sent!")  # Prints success message in console

        # error message
    except:
        speak("Error in sending the message")
