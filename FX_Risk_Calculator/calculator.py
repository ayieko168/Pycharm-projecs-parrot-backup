#!/usr/bin/env python3

from tkinter import *
from tkinter import font
from os import system
import threading

calclist = ['  Risk      ',
            '  Lot       ',
            '  Stop Loss '
            ]

currencies = [' USD ',
              ' EUR ',
              ' AUD ',
              ' GBP ',
              ' JPY ',
              ' CAD ',
              ' CHF',
              ' KSH ',
              ]

currency_value = currencies[0]


def optionsing(value):

    def riskup():

        slpipEntry.place_forget(), slpipLabel.place_forget(), slpipLabel2.place_forget(), lotEntry.place_forget()
        lotLabel.place_forget(), riskLabel.place_forget(), riskEntry.place_forget(), riskLabel2.place_forget()

        riskLabel2.config(text=currency_value)

        slpipLabel.place(x=220, y=30)
        slpipEntry.place(x=320, y=30)
        slpipLabel2.place(x=390, y=30)

        lotLabel.place(x=220, y=70)
        lotEntry.place(x=320, y=70)

    def lotup():

        slpipEntry.place_forget(), slpipLabel.place_forget(), slpipLabel2.place_forget(), lotEntry.place_forget()
        lotLabel.place_forget(), riskLabel.place_forget(), riskEntry.place_forget(), riskLabel2.place_forget()

        riskLabel2.config(text=currency_value)

        riskLabel.place(x=220, y=30)
        riskEntry.place(x=300, y=30)
        riskLabel2.place(x=370, y=30)

        slpipLabel.place(x=220, y=70)
        slpipEntry.place(x=300, y=70)
        slpipLabel2.place(x=370, y=70)

    def slpipup():

        slpipEntry.place_forget(), slpipLabel.place_forget(), slpipLabel2.place_forget(), lotEntry.place_forget()
        lotLabel.place_forget(), riskLabel.place_forget(), riskEntry.place_forget(), riskLabel2.place_forget()

        riskLabel2.config(text=currency_value)

        riskLabel.place(x=220, y=30)
        riskEntry.place(x=320, y=30)
        riskLabel2.place(x=390, y=30)

        lotLabel.place(x=220, y=70)
        lotEntry.place(x=320, y=70)

    if value == calclist[0]:
        riskup()
    elif value == calclist[1]:
        lotup()
    elif value == calclist[2]:
        slpipup()


def currenciesing(value):

    global currency_value

    currency_value = value


def calculating():

    if calcvals.get() == calclist[0]:

        risk = slpipEntryVar.get() * lotEntryVar.get() * 10.0
        ans_label.config(text='Risk: {:,.2f}{}'.format(risk, currency_value))

    elif calcvals.get() == calclist[1]:

        print('loting')
        lot = riskEntryVar.get() / (slpipEntryVar.get() * 10)
        ans_label.config(text='Lot: {:,.2f}'.format(lot))

    elif calcvals.get() == calclist[2]:

        print('stoping loss')
        sl = riskEntryVar.get() / (lotEntryVar.get() * 10)
        ans_label.config(text='S.L: {:,.2f} PIPs'.format(sl))


def currency_calculatoring():

    currency_calcTop = Toplevel(mainWindow, bg='white')

    def fvalupdate(value):

        fromLabel1.config(text=value)

    def tvalupdate(value):

        toLabel1.config(text=value)

    def calculateing():

        if fromEntVar.get() == currencies[0]:

            pass

    fromLabel = Label(currency_calcTop, text='From:', bg='white', fg='black', font=font3)
    fromLabel.place(x=5, y=5)
    fromOptionMenu = OptionMenu(currency_calcTop, fromvals, *currencies, command=fvalupdate)
    fromOptionMenu.place(x=15, y=30)
    fromEnt = Entry(currency_calcTop, textvariable=fromEntVar, bg='white', fg='black', width=7, bd=3)
    fromEnt.place(x=5, y=70)
    fromLabel1 = Label(currency_calcTop, text=fromvals.get(), bg='white', fg='black', font=font3)
    fromLabel1.place(x=75, y=73)

    equalLabel = Label(currency_calcTop, text='=', font=font12, bg='white', fg='black')
    equalLabel.place(x=130, y=73)

    toLabel = Label(currency_calcTop, text='To:', bg='white', fg='black', font=font3)
    toLabel.place(x=180, y=5)
    toOptionMenu = OptionMenu(currency_calcTop, tovals, *currencies, command=tvalupdate)
    toOptionMenu.place(x=190, y=30)
    toEnt = Entry(currency_calcTop, textvariable=toEntVar, bg='white', fg='black', width=7, bd=3)
    toEnt.place(x=180, y=70)
    toLabel1 = Label(currency_calcTop, text=tovals.get(), bg='white', fg='black', font=font3)
    toLabel1.place(x=250, y=73)

    statusBar = Frame(currency_calcTop, bg='white', height=25, bd=2, relief=GROOVE,)
    statusBar.pack(side=BOTTOM, fill=X)

    convetButton = Button(currency_calcTop, text=' CONVERT ', bg='black', fg='white', bd=3)
    convetButton.place(x=100, y=120)

    currency_calcTop.geometry('300x200+520+300')
    currency_calcTop.title('Currency Converter')


def calculatoring():

    def com():

        system('mate-calculator')

    th1 = threading.Thread(target=com, name='calc')
    th1.start()


mainWindow = Tk()

# Tkinter Variables
calcvals = StringVar()
calcvals.set(calclist[0])
currencyVar = StringVar()
currencyVar.set(currencies[0])
slpipEntryVar = DoubleVar()
slpipEntryVar.set(1.0000)
lotEntryVar = DoubleVar()
lotEntryVar.set(1.0000)
riskEntryVar = DoubleVar()
riskEntryVar.set(1.000)
answer = StringVar()
answer.set('Welcome')
answerValue = answer.get()
fromvals = StringVar()
fromvals.set(currencies[0])
fromEntVar = DoubleVar()
fromEntVar.set(1)
tovals = StringVar()
tovals.set(currencies[0])
toEntVar = DoubleVar()
toEntVar.set(1)

font1 = font.Font(size=30, weight='bold', family='Helvetica')
font2 = font.Font(size=12, underline=1)
font3 = font.Font(size=11,)
font12 = font.Font(size=15)

# The widgets

    # the menubar

menubar = Menu(mainWindow)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Calculator', command=calculatoring)
filemenu.add_command(label='Currency Converter', command=currency_calculatoring)

menubar.add_cascade(label='File', menu=filemenu)

optionsLabel = Label(mainWindow, text='What To Calculate', bg='white', fg='black', font=font2)
optionsLabel.place(x=5, y=5)
options = OptionMenu(mainWindow, calcvals, *calclist, command=optionsing)
options.place(x=15, y=30)

currencyLabel = Label(mainWindow, text='Quoted Currency', bg='white', fg='black', font=font2)
currencyLabel.place(x=5, y=115)
currency_option = OptionMenu(mainWindow, currencyVar, *currencies, command=currenciesing)
currency_option.place(x=15, y=140)

calculate_button = Button(mainWindow, text=' CALCULATE ', relief=RAISED, bg='black', fg='white',
                          bd=3, command=calculating)
calculate_button.place(x=320, y=275)

ans_label = Label(mainWindow, text=answerValue, bg='white', fg='black', font=font1)
ans_label.place(x=10, y=320)

slpipLabel = Label(mainWindow, text='Stop Loss:', bg='white', fg='black')
slpipEntry = Entry(mainWindow, width=7, textvariable=slpipEntryVar)
slpipLabel2 = Label(mainWindow, text='PIPs', bg='white', fg='black')
lotLabel = Label(mainWindow, text='Lot Volume:', bg='white', fg='black')
lotEntry = Entry(mainWindow, width=7, textvariable=lotEntryVar)
riskLabel = Label(mainWindow, text=' Risk :', bg='white', fg='black')
riskEntry = Entry(mainWindow, width=7, textvariable=riskEntryVar)
riskLabel2 = Label(mainWindow, text=currency_value, bg='white', fg='black')

slpipLabel.place(x=220, y=30)
slpipEntry.place(x=320, y=30)
slpipLabel2.place(x=390, y=30)
lotLabel.place(x=220, y=70)
lotEntry.place(x=320, y=70)

mainWindow.title('  Forex Risk Calculator ')
mainWindow.geometry('500x400+400+200')
mainWindow.config(bg='white', menu=menubar)
mainWindow.resizable(width=0, height=0)
mainWindow.mainloop()

