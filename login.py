from tkinter import *
from tkinter import messagebox
import tkinter as tk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import initialize_app
from firebase_admin import db
from reference import reference

ref = reference()

correctPass = False

def log():
    global name
    global password

    login = Toplevel()
    login.title("Log-In")
    login.geometry("400x500")
    login['background'] = '#4C4FEC'
    login.wm_iconbitmap('icon.ico')
    
    Label(login, text = "\nWork Flow\nLOGIN", bg = '#4C4FEC', fg = "white", font = ('sans-serif', 50)).pack(pady = 20)

    name = tk.Entry(login, width = 30, font = ('sans-serif', 16))
    name.insert(END, 'Username')
    name.pack(pady = 10)

    password = tk.Entry(login, width = 30, font = ('sans-serif', 16), show="*")
    password.insert(END, 'Password')
    password.pack(pady = 10)
    
    btn = Button(login, height = 3, width = 25, bg = '#F4C4F4', highlightthickness = 0, bd = 0, text = "Log In", command = check)
    btn.pack(side=TOP, pady=5)

def success():
    userString = name.get()

    file2 = open(r"logged.txt","w+")
    file2.write("True")
    file2.close()

    success = Toplevel()
    success.title("Success")
    success.geometry("200x200")
    success['background'] = '#4C4FEC'
    success.wm_iconbitmap('icon.ico')
    Label(success, text = f"Login\nSuccessful\n{userString}\nclose to\nbegin", bg = '#4C4FEC', fg = "white", font = ('sans-serif', 16)).pack(pady = 20)




def check():
    global correctPass

    userString = name.get()
    passwordString = password.get()

    users = ref.get()
    print(len(users))
    userPos = None
    print(users)
    keyList = []
    for key in users.keys():
        keyList.append(key)
    print(keyList)
    for user in range(len(users)):
        if userString == users[keyList[user]]['username']:
            if passwordString == str(users[keyList[user]]['password']):
                correctPass = True
                userPos = user
                break
    
    if correctPass == True:
        file = open(r"scores.txt", "w+")
        strOut = f"{userString} {users[keyList[user]]['points']}"
        file.write(strOut)
        file.close()
        success()

    print(userString, passwordString)