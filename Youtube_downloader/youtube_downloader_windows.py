#!/usr/bin/env python3

from tkinter import *
from tkinter import messagebox
import os
from pynput.keyboard import Key, Controller
import time
from tkinter import filedialog

keyboard = Controller()
destination = '/home/ayieko/'
os.chdir(destination)

# options
urlList = 'url_list'
op1=''  # format
op2=''
op3=''  # playlist
op4=''  # audio

formats = ['Video Formats',
           'mp4',
           'mp4 [360p]',
           'mp4 [720p]',
           'mp4 [1080p]',
           'mp4 [4K]',
           '',
           'Audio Formats',
           'mp3',
           'wav',
           'opus'

           ]

global fop


def exit_all():

    qiuz = messagebox.askquestion('EXIT?', 'ARE YOU SURE\nYOU WANT TO EXIT?')

    if qiuz == 'yes':
        mainWindow.destroy()
    else:
        pass


def downloader():

    fopval = fop.get()
    if fopval == formats[0]:
        op1 = ''
    elif fopval == formats[1]:
        op1 = ''
    elif fopval == formats[2]:
        op1 = ' -f 18 '
    elif fopval == formats[3]:
        op1 = ' -f 22 '
    elif fopval == formats[4]:
        op1 = ' -f 37 '
    elif fopval == formats[5]:
        op1 = ' -f 38 '
    elif fopval == formats[6]:
        op1 = ''
    elif fopval == formats[7]:
        op1 = ' -x '
    elif fopval == formats[8]:
        op1 = ' -x --audio-format mp3 '
    elif fopval == formats[9]:
        op1 = ' -x --audio-format wav '
    elif fopval == formats[10]:
        op1 = ' -x --audio-format opus '


    l = text1.get(0.1, END)

    downList = open('url_list', 'w+')
    downList.write(l)
    downList.close()

    try:
        ask1 = messagebox.askyesno('INFORMATION FOR YOU', 'This application will now\nopen the terminal\nIs it okay?')

        if ask1 == True:
            COMMAND = 'youtube-dl -a {}'.format(urlList)+op1+op2+op3+op4
            os.system("gnome-terminal -e 'bash -c \" {} ; exec bash\"'".format(COMMAND))
        else:
            pass


    except FileNotFoundError as nofileerror:

        messagebox.showerror('ERROR', 'Error finding the destination\n "{}"'.format(urlList))


def pasting():

    keyboard.press(Key.ctrl)
    keyboard.press('v')
    keyboard.release(Key.ctrl)
    keyboard.release('v')

def undoing():

    keyboard.press(Key.ctrl)
    keyboard.press('z')
    keyboard.release(Key.ctrl)
    keyboard.release('z')

def redoing():

    keyboard.press(Key.ctrl)
    keyboard.press(Key.shift)
    keyboard.press('z')
    keyboard.release(Key.ctrl)
    keyboard.release(Key.shift)
    keyboard.release('z')

def delAll():
    text1.delete(0.1, END)

def opening():
    pass

def savingto():
    askdir = filedialog.askdirectory()

    os.chdir(askdir)

mainWindow = Tk()

# the menubar
menubar = Menu(mainWindow)

sub_setting = Menu(menubar, tearoff=0)
sub_setting.add_command(label='General')
sub_setting.add_command(label='Formats')
sub_setting.add_command(label='Downloads')
sub_setting.add_command(label='Extra')


filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Download', command=downloader)
filemenu.add_command(label='Remove')
filemenu.add_command(label='open..', command=opening)
filemenu.add_command(label='Save To..', command=savingto)
filemenu.add_separator()
filemenu.add_cascade(label='Settings', menu=sub_setting)
filemenu.add_command(label=' Exit ', command=exit_all)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label='Undo', accelerator='ctrl+z', command=undoing)
editmenu.add_command(label='Redo', accelerator='ctrl+shift+z', command=redoing)
editmenu.add_command(label='Copy')
editmenu.add_command(label='paste', command=pasting)
editmenu.add_separator()
editmenu.add_command(label='Delete')
editmenu.add_command(label='Delete all',command=delAll)

menubar.add_cascade(label='File', menu=filemenu)
menubar.add_cascade(label='Edit', menu=editmenu)


# Fonts
font1 = ('DejaVu Sans', 12)
font2 = ('Latin Modern Roman ', 11, 'normal', 'roman')


# The Widgets
canvas1 = Canvas(height=200, bg='green', bd=4)
canvas2 = Canvas(height=70, bg='blue', bd=4)
canvas3 = Canvas(height=200, bg='red', bd=4)
canvas4 = Canvas(height=50, bg='yellow', bd=4)

label1 = Label(canvas1, text='Enter the URLs below..', fg='black', bg='white', font=font1)

text1 = Text(canvas1, bg='white', fg='black', height=10, font=font1, undo=True, wrap=NONE)

addButton = Button(canvas2, text='Add', bg='white', fg='green', relief=GROOVE, bd=2, activebackground='green')
downButton = Button(canvas4, text='Download', bg='white', fg='black', relief=RAISED, bd=3, command=downloader)
pasteButton = Button(canvas2, text='paste', bg='white', fg='black', command=pasting)

statusbar = Canvas(mainWindow, bg='blue', height=3,)
status = Label(statusbar, text='Processing...', font=font2, bg='white', bd=3, fg='black')

fop = StringVar()
fop.set(formats[0])
vidformatop = OptionMenu(canvas2, fop, *formats)



# Displaying the widgets
canvas1.pack(fill=X, pady=1)
canvas2.pack(fill=X, pady=1)
canvas3.pack(fill=X, pady=1)
canvas4.pack(fill=X, pady=1)

label1.pack(side=TOP, ipadx=2, pady=5, padx=4, anchor=W)

text1.pack(fill=X, pady=2, padx=3)

addButton.grid(row=1, column=1, padx=10, pady=4, sticky=E)
downButton.pack(anchor=E, padx=10, pady=5, ipadx=2)
pasteButton.grid(row=1, column=2, sticky=E)

statusbar.pack(fill=X)
status.pack(anchor=W, padx=3, pady=4)

vidformatop.grid(row=1, column=0)

# Binding the widgets


mainWindow.config(bg='black', menu=menubar)
mainWindow.title('YouTube Downloader')
mainWindow.geometry('850x600')
mainWindow.mainloop()

# Created on Thu 29 Mar 2018 02:21:38 AM
