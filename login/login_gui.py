#!/usr/bin/env python3

from tkinter import *
from pynput.mouse import Button, Controller as m
from pynput.keyboard import Key, Controller as k

def butonning():

    pass
    

mainWindow = Tk()

frame = Frame(mainWindow, bg='white', width=200, height=200)
frame.pack()

lab1 = Label(frame, text='Username', anchor=E, bg='white', fg='black')
lab2 = Label(frame, text='password', anchor=E, bg='white', fg='black')

entry1 = Entry(frame, bd=6, fg='black', bg='white', relief=GROOVE,)
entry2 = Entry(frame, bd=6, fg='black', bg='white', show='*', relief=GROOVE,)

check = Checkbutton(frame, bg='white', fg='black', bitmap='questhead', compound=LEFT, text='keep me signed in', activebackground=None)

lab1.grid(row=1, column=1)
lab2.grid(row=3, column=1)
entry1.grid(row=1,column=2)
entry2.grid(row=3,column=2)
check.grid(columnspan=5)


mainWindow.mainloop()
