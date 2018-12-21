#!/usr/bin/env python3

from tkinter import *
import os
from time import sleep
import sys


# The functions

def starting():

    statusVar.set("Starting the server at port {}".format(ent1Var.get()))
    sleep(0.25)
    if sys.version_info.major == 3:
        command = 'python3 -m http.server {}'.format(ent1Var.get())
    elif sys.version_info.major == 2:
        command = 'python2 -m SimpleHTTPServer {}'.format(ent1Var.get())

    statusVar.set("")
    sleep(0.5)
    os.system("gnome-terminal -e 'bash -c \"{}; exec bash\"'".format(command))

    for x in range(8):
        print('Jah Jah')
    sleep(0.25)
    statusVar.set("Running")


mainWindow = Tk()

# The tkinter variables
ent1Var = StringVar()
ent1Var.set('8000')
statusVar = StringVar()
statusVar.set('  Welcome..  ')

# The menubar

menubar = Menu(tearoff=0)

helpmenu = Menu(tearoff=0)
helpmenu.add_command(label='Developer')
helpmenu.add_command(label='About')
helpmenu.add_command(label='Manual')
helpmenu.add_separator()
helpmenu.add_command(label='About')
helpmenu.add_command(label='Exit', command=lambda : mainWindow.destroy())

menubar.add_cascade(label='  Help  ', menu=helpmenu, underline=2)

# The widgets

ent1 = Entry(mainWindow, width=10, textvariable=ent1Var, bg='white', fg='black', font=32)
ent1.pack(padx=40, pady=10)

entlab = Label(text='Enter the port number ', fg='black', bg='white')
entlab.pack(pady=20)

exbutton = Button(mainWindow, text='START', font=32, fg='black', bg='white', bd=4, relief=RAISED, command=starting)
exbutton.pack(ipadx=12)

statusbar = Frame(mainWindow, bg='white', height=22, relief=GROOVE, bd=2)
statusbar.pack(fill=X, side=BOTTOM)

status = Label(statusbar, bg='white', fg='black', textvariable=statusVar)
status.pack(side=LEFT)

mainWindow.geometry('400x300+300+100')
mainWindow.title('****SimpleHTTPServer****')
mainWindow.config(bg='white', menu=menubar)
mainWindow.mainloop()
