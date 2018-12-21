#!/usr/bin/env python3

from tkinter import *

mainWindow = Tk()

#  MENU BAR
# *********

menubar = Menu()

filemenu = Menu(tearoff=0)
filemenu.add_command(label='New ')
filemenu.add_command(label='Save To... ')
filemenu.add_separator()
filemenu.add_command(label='EXIT', command=lambda: mainWindow.destroy())

menubar.add_cascade(label='File', menu=filemenu)

#


mainWindow.title('  **CRUNCH GUI**  ')
mainWindow.geometry('500x400+500+100')
mainWindow.config(bg='white', menu=menubar)
mainWindow.mainloop()






