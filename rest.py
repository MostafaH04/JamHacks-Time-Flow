from tkinter import *
from tkinter import messagebox
import tkinter as tk

def work():
    root = Tk()
    root.title("Register")
    root.geometry("400x200")
    root['background'] = '#4C4FEC'
    root.wm_iconbitmap('icon.ico')
    Label(root, text = f"You have been working\nfor over 1 hr, try\n taking a break!", bg = '#4C4FEC', fg = "white", font = ('sans-serif', 16)).pack(pady = 30)

    root.mainloop()

