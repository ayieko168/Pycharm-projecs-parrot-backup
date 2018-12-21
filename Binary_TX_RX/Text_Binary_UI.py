#!/usr/bin/env python3

from tkinter import *
import Converter


def converting():

    text = entryText.get(0.0, END)

    # print(text)

    Converter.convert_tb(text)


mainWindow = Tk()

#  MENU BAR
# ************

menubar = Menu()

filemenu = Menu(tearoff=0)
filemenu.add_command(label='Open')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=lambda: mainWindow.destroy())

menubar.add_cascade(menu=filemenu, label='File')

#  WIDGETS
# **********

entryText = Text(mainWindow, width=83, height=12, bg='white', fg='black', bd=2)
entryText.grid(row=1, column=1, padx=15, pady=5)

convertBut = Button(mainWindow, text=' CONVERT ', bd=3, bg='white', fg='black', command=converting)
convertBut.grid(row=2, column=1, padx=50, pady=5)

outText = Text(mainWindow, width=83, height=12, bg='white', fg='black', bd=2)
outText.grid(row=3, column=1, padx=15, pady=5)


mainWindow.geometry('700x500+300+100')
mainWindow.title(' ***BINARY TRANSCRIBER*** ')
mainWindow.config(bg='white', menu=menubar)
mainWindow.mainloop()





