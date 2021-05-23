from tkinter import *
from tkinter import messagebox
import tkinter as tk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import initialize_app
from firebase_admin import db
from reference import reference

ref = reference()

def reg():
    global name
    global password

    register = Toplevel()
    register.title("Register")
    register.geometry("400x500")
    register['background'] = '#4C4FEC'
    register.wm_iconbitmap('icon.ico')

    Label(register, text = "\nWork Flow\nREGISTER", bg = '#4C4FEC', fg = "white", font = ('sans-serif', 50)).pack(pady = 20)

    name = tk.Entry(register, width = 30, font = ('sans-serif', 16))
    name.insert(END, 'Username')
    name.pack(pady = 10)

    password = tk.Entry(register, width = 30, font = ('sans-serif', 16), show="*")
    password.insert(END, 'Password')
    password.pack(pady = 10)

    btn = Button(register, height = 3, width = 25, bg = '#F4C4F4', highlightthickness = 0, bd = 0, text = "Register", command = check)
    btn.pack(side=TOP, pady=5)

def end():
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
    userString = name.get()
    passwordString = password.get()

    lengthDb = len(ref.get())

    data = {
            "username": userString,
            "password": passwordString,
            "points": 0
    }

    ref.push(data)
    file = open(r"scores.txt", "w+")
    strOut = f"{userString} {0}"
    file.write(strOut)
    file.close()
    end()

