#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import os

global saveAsFileName
global saveName
saveAsFileName = ''
f_exte = ''
donefont = 15, 'bold', 'roman'

root = Tk()

def exiting():

    root.destroy()


def helping():
    pass


def opening():

    destination = filedialog.askopenfile()

    try:
        entvar.set(destination.name)

    except AttributeError:

        messagebox.showinfo('INFO!', 'SORRY YOU DID NOT CHOSE ANY FILE\nTRY AGAIN')


def savingas():

    name = filedialog.asksaveasfilename()

    saveAsFileName = name.split('/')[-1]

    print('saving as : {}'.format(saveAsFileName))


def converting():
    file = entvar.get()
    opval = opmenVar.get()

    if opval == formts[0]:
        ext = opval
    elif opval == formts[1]:
        ext = opval
    elif opval == formts[2]:
        ext = opval
    elif opval == formts[3]:
        ext = opval
    elif opval == formts[4]:
        ext = opval
    elif opval == formts[5]:
        ext = opval
    elif opval == formts[6]:
        ext = opval
    elif opval == formts[7]:
        ext = opval
    elif opval == formts[8]:
        ext = opval
    elif opval == formts[9]:
        ext = opval
    elif opval == formts[10]:
        ext = opval
    elif opval == formts[11]:
        ext = opval
    elif opval == formts[12]:
        ext = opval
    elif opval == formts[13]:
        ext = opval
    elif opval == formts[14]:
        ext = opval
    elif opval == formts[15]:
        ext = opval
    elif opval == formts[16]:
        ext = opval
    elif opval == formts[17]:
        ext = opval
    elif opval == formts[18]:
        ext = opval
    elif opval == formts[19]:
        ext = opval
    elif opval == formts[20]:
        ext = opval
    elif opval == formts[21]:
        ext = opval
    elif opval == formts[22]:
        ext = opval
    elif opval == formts[23]:
        ext = opval

    try:
        x = file.split('/')
        y = x[-1]
        try:
            i_name, i_ext =y.split('.')
            name = i_name
        except Exception as ex:

            name = y
            print(ex)

        im1 = Image.open(file)
        try:
            try:
                os.chdir(file.split('/{}'.format(name))[0])
                print('saving in {}'.format(os.getcwd()))
                im1.save('{}.{}'.format(name, ext).lower(), format=ext)
                messagebox.showinfo('INFO!', 'DONE CONVERTING {}.{}'.format(name.upper(), ext.upper()))
            except NotADirectoryError as NAD:
                messagebox.showerror('OOPs!', NAD)


        except KeyError as ke:

            messagebox.showerror('ERROR', 'THE FORMAT OPTION YOU SELECTED {} IS CURRENTLY\nUNAVAILABLE'.format(ke).upper())

        im1.close()

    except FileNotFoundError:

        messagebox.showerror('ERROR', 'PLEASE ENTER A VALID PATH')


def developing():

    win1 = Toplevel(root)

    font = 'Freeserif', 12
    devText = Text(win1, font=font, bg='white', fg='black',)
    with open('text.txt', 'r+') as text:
        content = text.read()
        devText.insert(0.1, content)
    devText.config(state=DISABLED)
    devText.pack()

    win1.geometry('400x300+450+250')


def formating():

    win2 = Toplevel(root)

    font = 'Freeserif', 12
    formText = Text(win2, font=font, bg='white', fg='black',)
    with open('formats.txt', 'r+') as text:
        content = text.read()
        formText.insert(0.1, content)
    formText.config(state=DISABLED)
    formText.pack()

    win2.geometry('600x400+450+250')


# Formats
formts = [' ANI  ', ' BMP   ', '  CAR  ',
          ' FAX  ', ' GIF   ', '  IMG  ',
          ' ICO  ', ' JPE   ', '  JPEG ',
          ' JPG  ', ' PIXAR ', '  PBM  ',
          ' PCD  ', ' PCX   ', '  PCT  ',
          ' PGM  ', ' PNG   ', '  PPM  ',
          ' PSD  ', ' PDF   ', '  TGA  ',
          ' TIFF ', ' WMF   '
          ]


# Variables
opmenVar = StringVar()
entvar = StringVar()
opmenVar.set(formts[0])
entvar.set('Enter the File path here')
butimage = PhotoImage(file='file.png')

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=False)
filemenu.add_command(label='Open', command=opening)
filemenu.add_command(label='Save As..', command=savingas)
filemenu.add_command(label='Convert', command=converting)
filemenu.add_command(label='Exit', command=exiting)


helpmenu = Menu(tearoff=False)
helpmenu.add_command(label='About')
helpmenu.add_command(label='Formats', command=formating)
helpmenu.add_command(label='Developer', command=developing)
helpmenu.add_separator()
helpmenu.add_command(label='Help')

menubar.add_cascade(label='File', menu=filemenu)
menubar.add_cascade(label='Help', menu=helpmenu)

# The Widgets

entry = Entry(root, font=20, width=25, textvariable=entvar).grid(row=1, column=1, padx=10, pady=25)

findbut = Button(root, image=butimage, command=opening).grid(row=2, column=1, sticky=N + W, padx=5)

label1 = Label(root, font=22, text='TO').grid(row=1, column=2, padx=15)

optMenu = OptionMenu(root, opmenVar, *formts).grid(row=1, column=3, padx=10)

sep1 = ttk.Separator(root, orient=HORIZONTAL).grid(row=3, pady=10, columnspan=5, sticky=E + W)

convertBut = Button(root, text='CONVERT', font=40, command=converting).grid(row=4, column=2, ipadx=30)

helpBut = Button(root, text='Help').grid(row=5, column=1, padx=2, pady=40, sticky=S + W, ipadx=4, ipady=2)

exitBut = Button(root, text='Exit', command=exiting).grid(row=5, column=3, padx=5, pady=40, sticky=S + E, ipadx=4,
                                                          ipady=2)

root.geometry('530x250+400+200')
root.resizable(width=False, height=False)
root.title('Image Converter')
root.config(bg='blue', menu=menubar)
root.mainloop()
