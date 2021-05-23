from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from login import log
from register import reg
import firebase_admin
from firebase_admin import credentials
from firebase_admin import initialize_app
from firebase_admin import db

def signup():
    logged = False

    file2 = open(r"logged.txt","r")
    lines = file2.readlines()
    if lines[0] == 'False':
        logged = False
    else:
        logged = True
    file2.close()

    root = Tk()
    root.title("Log-in")
    root.geometry("300x300")
    root['background'] = '#4C4FEC'
    root.wm_iconbitmap('icon.ico')

    logo = Image.open("icon.png")

    logo = logo.resize((90,90), Image.ANTIALIAS)
    logoImg = ImageTk.PhotoImage(logo)

    Label(root, image = logoImg, bg = '#4C4FEC').pack()

    btn1 = Button(root, height = 3, width = 25, bg = '#F4C4F4', highlightthickness = 0, bd = 0, text = "Register", command = reg)
    btn2 = Button(root, height = 3, width = 25, bg = '#F4C4F4', highlightthickness = 0, bd = 0, text = "Log-In", command = log)

    btn1.pack(side=TOP, pady=25)
    btn2.pack(side=TOP)

    Label(root, text = "Made for JamHacks", bg = '#4C4FEC', fg = "white").pack(pady = 20)

    mainloop()


signup()