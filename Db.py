import sqlite3
import tkinter

from Annex import *

conn = sqlite3.connect('AngelX.db')  # create file AgelX.db
c = conn.cursor()


def insert_record(ID, Name, EMAIL, WHATSAPP, WEIGHT):
    c.execute('''INSERT INTO fighter_records(ID,NAME,EMAIL,WHATSAPP,WEIGHT)
              VALUES(?,?,?,?,?)''', (ID, Name, EMAIL, WHATSAPP, WEIGHT))
    conn.commit()


def read_data(D):  # email address verification

    DATA = c.execute('''SELECT * FROM fighter_records''')
    for i in DATA:
        if str(i[2]) == D:
            speak('Welcome to the MMA gym ')

        else:
            speak('I cannot find your email in database, please go online to subscribe to the gym')


def read_dataAll():  # read values from the database by email address

    dataSet = c.execute('''SELECT * FROM fighter_records''')  # query to return all the students records
    lis = []  # list to append the records
    count = 0  # create a counter
    if dataSet is not None:
        for i in dataSet:  # loop in the records
            lis.append(i)
        speak('That is the values that are available ')
        for x in lis:  # loop over the list elements
            count += 1
            tkinter.messagebox.showinfo(title='Students', message=x)  # showing the message
        speak(f'do you have {count} students ')
    else:
        speak(f' Do you have {count}')


def delete_element(EMAIL):  # delete email

    sql = "DELETE FROM  fighter_records WHERE EMAIL=?"
    adr = (EMAIL,)
    c.execute(sql, adr)
    conn.commit()


def update_elements(NewEmail, Email):  # update email

    c.execute(''' UPDATE fighter_records SET EMAIL=? WHERE EMAIL=? ''', (NewEmail, Email))
    conn.commit()


def selectPoneNumber(email):  # getting the email and returning the student phone number
    DATA = c.execute('''SELECT * FROM fighter_records''')
    for i in DATA:  # looping ove all the elements of the table
        if str(i[2]) == email:
            number = str(i[3])
            return number

        else:
            speak('I cannot find your email in database, please go online to subscribe to the gym')



