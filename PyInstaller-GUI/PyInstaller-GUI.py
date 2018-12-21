#!/usr/bin/env python3

from tkinter import *
import os
import subprocess
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

# global variables
options = []

# The Function


def searching():

    searchVar = filedialog.askopenfile(filetypes=[('Python', '.py'), ('All Files', '*')])

    try:
        EntSearchVar.set(searchVar.name)
    except AttributeError:
        messagebox.showinfo('SORRY', 'YOU DID NOT CHOOSE ANY FILE')


def executing():
    global options1
    options1 = []
    global EntSearchVar

    # appending the entry options
    if len(optionsEnt1.get()) > 3:
        options1.append('--distpath')
        options1.append(optionsEnt1.get())

    if len(optionsEnt2.get()) > 3:
        options1.append('--workpath')
        options1.append(optionsEnt2.get())

    if len(genEnt1Var.get()) > 3:
        options1.append('--specpath')
        options1.append(genEnt1Var.get())

    if len(genEnt2Var.get()) > 3:
        options1.append('--name')
        options1.append(genEnt2Var.get())

    # end of appending entry options

    if EntSearchVar.get().endswith('.py') == 1:

        filepath = EntSearchVar.get()

        command = ['pyinstaller', filepath]

        for op in options: command.insert(len(command)-1, op)
        for op1 in options1: command.insert(len(command) - 1, op1)

        os.chdir('/home/ayieko/test')
        subprocess.run(command)
        #print(command)

        messagebox.showinfo('INFO', 'DONE!')

    else:
        messagebox.showerror('File Name Error', 'SORRY PLEASE SELECT A PYTHON FILE (.py)')


def findingdir():

    found = filedialog.askdirectory()

    mainWindow.clipboard_clear()
    mainWindow.clipboard_append(str(found))

    messagebox.showinfo('DONE', 'THE PATH TO SELECTED DIRECTORY HAS BEEN COPIED TO THE CLIPBOARD')


def checking1():

    if optionsCheck1Var.get() == 1:
        options.append('--clean')
    elif optionsCheck1Var.get() == 0:
        options.remove('--clean')


def checking2():

    if genCheck1Var.get() == 1:
        options.append('--onedir')
    elif genCheck1Var.get() == 0:
        options.remove('--onedir')


def checking3():

    if genCheck2Var.get() == 1:
        options.append('--onefile')
    elif genCheck2Var.get() == 0:
        options.remove('--onefile')


mainWindow = Tk()

# Variables
FileSearchImage = PhotoImage(file='save.png')
EntSearchVar = StringVar()
EntSearchVar.set('Path to python File...')
optionsEnt1Var = StringVar()
optionsEnt2Var = StringVar()
genEnt1Var = StringVar()
genEnt2Var = StringVar()
optionsCheck1Var = IntVar()
optionsCheck1Var.set(0)
genCheck1Var = IntVar()
genCheck1Var.set(0)
genCheck2Var = IntVar()
genCheck2Var.set(0)


# Notebook Files
Notebook = ttk.Notebook(mainWindow)

canvas1 = Canvas(bg='white', width=600, height=370)
canvas2 = Canvas(bg='red', width=600, height=370)
canvas3 = Canvas(bg='green', width=600, height=370)


# The Menu
menubar = Menu()

filemenu = Menu(tearoff=False)
filemenu.add_command(label='Search..', command=searching)
filemenu.add_command(label='Open', command=findingdir)
filemenu.add_command(label='Settings')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=lambda : mainWindow.destroy())

helpmenu = Menu(tearoff=False)
helpmenu.add_command(label='About')
helpmenu.add_command(label='Developers')
helpmenu.add_command(label='Manual')
helpmenu.add_separator()
helpmenu.add_command(label='Help')

menubar.add_cascade(label='File', underline=0, menu=filemenu)
menubar.add_cascade(label='Help', underline=0, menu=helpmenu)


FileSearch = Button(mainWindow, image=FileSearchImage, relief=RAISED, bd=1.5, command=searching
                    ).grid(row=1, column=1, padx=20, pady=30)

EntSearch = Entry(mainWindow, textvariable=EntSearchVar, bg='white', fg='black', bd=4, width=40
                  ).grid(row=1, column=2, padx=5, pady=30)

ExecuteBut = Button(mainWindow, text=' EXECUTE ', command=executing, font=10, bg='green', activebackground='green',
                    relief=RAISED, activeforeground='black', bd=2
                    ).grid(row=1, column=3, padx=20, columnspan=2, pady=30, sticky=E)

# The options Tab widgets

# The 'Optional Arguments' Frame
optionsFrame = LabelFrame(canvas1, text=' Optional Arguments ', bg='white', fg='black')

optionsEntLab1 = Label(optionsFrame, text='Destination path :', fg='black', bg='white').grid(row=1, column=1, padx=5, pady=5)
optionsEnt1 = Entry(optionsFrame, width=30, fg='black', bg='white', textvariable=optionsEnt1Var)
optionsEnt1.grid(row=1, column=2, padx=5, pady=10)

optionsEntLab2 = Label(optionsFrame, text='Work path :', fg='black', bg='white').grid(row=2, column=1, padx=5, sticky=E)
optionsEnt2 = Entry(optionsFrame, width=30, fg='black', bg='white', textvariable=optionsEnt2Var)
optionsEnt2.grid(row=2, column=2, padx=5, pady=10)

optionsSep = ttk.Separator(optionsFrame, orient=HORIZONTAL).grid(row=1, column=3, rowspan=10, padx=10, sticky=N+S)

optionsCheck1 = Checkbutton(optionsFrame, text='Clean cache', fg='black', bg='white', activebackground='white',
                            activeforeground='black', variable=optionsCheck1Var, command=checking1)
optionsCheck1.grid(row=1, column=4, padx=5, pady=5)

optionsFrame.grid(row=1, column=1, padx=30, pady=10)
# End of The 'Optional Arguments' Frame
# The 'What to generate' Frame
genFrame = LabelFrame(canvas1, text=' What to Generate ', bg='white', fg='black', width=500, height=30)

genCheck1 = Checkbutton(genFrame, text=' One Directory ', bg='white', fg='black', activebackground='white',
                        activeforeground='black', variable=genCheck1Var, command=checking2)
genCheck1.grid(row=1, column=1, padx=5, pady=5)

genCheck2 = Checkbutton(genFrame, text=' One File ', bg='white', fg='black', activebackground='white',
                        activeforeground='black', variable=genCheck2Var, command=checking3)
genCheck2.grid(row=2, column=1, padx=5, pady=5, sticky=E)

genSep = ttk.Separator(genFrame, orient=HORIZONTAL).grid(row=1, column=2, rowspan=10, padx=10, sticky=N+S)

genEntLab1 = Label(genFrame, text='Spec File :', fg='black', bg='white').grid(row=1, column=3, padx=5, pady=5, sticky=E)
genEnt1 = Entry(genFrame, width=30, fg='black', bg='white', textvariable=genEnt1Var)
genEnt1.grid(row=1, column=4, padx=5, pady=10)

genEntLab2 = Label(genFrame, text='App name :', fg='black', bg='white').grid(row=2, column=3, padx=5, pady=5, sticky=E)
genEnt2 = Entry(genFrame, width=30, fg='black', bg='white', textvariable=genEnt2Var)
genEnt2.grid(row=2, column=4, padx=5, pady=10)

genFrame.grid(row=2, column=1, padx=30, pady=10, sticky=W)
# End of 'What To Generate' Frame
# The Help And FindPath Buttons
helpBut1 = Button(canvas1, text=' Help ', bg='white', fg='black', bd=3, relief=RAISED)
helpBut1.grid(row=3, column=1, pady=50, sticky=E)

FindFileBut1 = Button(canvas1, text=' Find a Dir ', bg='white', fg='black', bd=3, relief=RAISED, command=findingdir)
FindFileBut1.grid(row=3, column=1, pady=50)
# End of Help And FindPath Buttons

# End of Options Tab

Notebook.add(canvas1, text=' Options ', underline=1)
Notebook.add(canvas2, text=' Advanced Options ', underline=1)
Notebook.add(canvas3, text=' Advanced.. ', underline=1)
Notebook.grid(row=2, column=1, columnspan=3, padx=23)


mainWindow.geometry('650x500+370+100')
mainWindow.title('PyInstaller GUI')
mainWindow.config(bg='white', menu=menubar)
mainWindow.resizable(width=False, height=False)
mainWindow.mainloop()
