#!/usr/bin/env python3

from tkinter import *
from tkinter import messagebox
import os
# import subprocess
from pynput.keyboard import Key, Controller       	# third party module
from tkinter import filedialog
from tkinter import ttk
import threading
from time import sleep

keyboard = Controller()

destination = '/home/{}/Desktop'.format(os.getlogin())
os.chdir(destination)

destination_options = ['/home/{}/Desktop'.format(os.getlogin()),
                       '/home/{}/Downloads'.format(os.getlogin()),
                       '/home/{}/Videos'.format(os.getlogin()),
                       '/home/{}/Music'.format(os.getlogin()),
                       ]

# Global Variables
global playEnt

# options
op0 = ' Downloaded_URLs '  # urls
op1 = ''  # format
op2 = ''
op3 = ''  # playlist
op4 = ''  # update
op5 = ''  # playlist individual videos
op6 = ''  # Playlist video to start at  --playlist-start NUMBER
op7 = ''  # Playlist video to end at    --playlist-end NUMBER
op8 = ''  # Download playlist videos in reverse order --playlist-reverse
op9 = ''  # Download playlist videos in random order   --playlist-random
op10 = ''  # --max-downloads NUMBER  Abort after downloading NUMBER files
op11 = ''  # --min-filesize SIZE     Do not download any videos smaller than SIZE (e.g. 50k or 44.6m)
op12 = ''  # --max-filesize SIZE     Do not download any videos larger than SIZE (e.g. 50k or 44.6m)
op13 = ''  # --datebefore DATE       Download only videos uploaded on or before this date (i.e. inclusive)
op14 = ''  # --dateafter DATE        Download only videos uploaded on or after this date (i.e. inclusive)
op15 = ''  # --min-views COUNT       Do not download any videos with less than COUNT views
op16 = ''  # --max-views COUNT       Do not download any videos with more than COUNT views
op17 = ''  # --age-limit YEARS       Download only videos suitable for the given age
op18 = ''  # --include-ads           Download advertisements as well (experimental)
op19 = ''  #
op20 = ''

formats = ['(Video Formats)',
           'mp4 [BEST]',
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

qualities = ['Best',
             'worst',
             'Best video',
             'Worst video',
             'Best audio',
             'Worst audio',

             ]

qualities2 = ['3gp',
              'aac',
              'flv',
              'm4a',
              'mp3',
              'mp4',
              'ogg',
              'wav',
              'webm'
              ]


def exit_all():

    qiuz = messagebox.askquestion('EXIT?', 'ARE YOU SURE\nYOU WANT TO EXIT?')

    if qiuz == 'yes':
        mainWindow.destroy()
    else:
        pass


def downloader():

    global playEnt
    global downthread_state
    downthread_state = True
    global op0
    global op1
    global op2
    global op3
    global op4
    global op5
    global op6
    global op7
    global op8
    global op9
    global op10
    global op11
    global op12
    global op13
    global op14
    global op15
    global op16
    global op17
    global op18
    global op19
    global op20
    formatVal = fop.get()

    # Format selection

    if formatVal == formats[0]:
        op1 = ''
    elif formatVal == formats[1]:
        op1 = ' -f best '
    elif formatVal == formats[2]:
        op1 = ' -f 18 '
    elif formatVal == formats[3]:
        op1 = ' -f 22 '
    elif formatVal == formats[4]:
        op1 = ' -f 37 '
    elif formatVal == formats[5]:
        op1 = ' -f 38 '
    elif formatVal == formats[6]:
        op1 = ''
    elif formatVal == formats[7]:
        op1 = ' -x '
    elif formatVal == formats[8]:
        op1 = ' -x --audio-format mp3 '
    elif formatVal == formats[9]:
        op1 = ' -x --audio-format wav '
    elif formatVal == formats[10]:
        op1 = ' -x --audio-format opus '

# Playlist option selection

    if plvar.get() == 1 or playCheck1Var.get() == 1 or playCheck2Var.get() == 1 or playCheck3Var.get() == 1 \
            or playCheck4Var.get() == 1 or playCheck5Var.get() == 1:
        op3 = ' --yes-playlist '
    elif plvar.get() == 0:
        op3 = ' --no-playlist '

# Playlist Advanced selection

    if playCheck1Var.get() == 1:  # first check if Advanced option playlist is checked
        plad = playEntVar.get()
        if plad.endswith(',') == 1:
            plad = plad.strip(',')
            op5 = ' --playlist-items {} '.format(plad)
        else:
            op5 = ' --playlist-items {} '.format(plad)
    else:
        op5 = ''

    if playCheck2Var.get() == 1:
        op6 = ' --playlist-start {} '.format(playSpin1Var.get())
    else:
        op6 = ''

    if playCheck3Var.get() == 1:
        op7 = ' --playlist-end {} '.format(playSpin2Var.get())
    else:
        op7 = ''

    if playCheck4Var.get() == 1:
        op8 = ' --playlist-reverse '
    else:
        op8 = ''

    if playCheck5Var.get() == 1:
        op9 = ' --playlist-random '
    else:
        op9 = ''

    if vidCheck1Var.get() == 1:
        op10 = ' --max-downloads {} '.format(vidSpin1Var.get())
    else:
        op10 = ''

    if vidCheck2Var.get() == 1:
        op11 = ' --min-filesize {} '.format(vidSpin2Var.get())
    else:
        op11 = ''

    if vidCheck3Var.get() == 1:
        op12 = ' --max-filesize {} '.format(vidSpin3Var.get())
    else:
        op12 = ''

    if vidCheck4Var.get() == 1:
        op13 = ' --datebefore {} '.format(vidEnt1Var.get())
    else:
        op13 = ''

    if vidCheck5Var.get() == 1:
        op14 = ' --dateafter {} '.format(vidEnt2Var.get())
    else:
        op14 = ''

    if vidCheck6Var.get() == 1:
        op15 = ' --min-views {} '.format(vidSpin4Var.get())
    else:
        op15 = ''

    if vidCheck7Var.get() == 1:
        op16 = ' --max-views {} '.format(vidSpin5Var.get())
    else:
        op16 = ''

    if vidCheck8Var.get() == 1:
        op17 = ' --age-limit {} '.format(vidSpin6Var.get())
    else:
        op17 = ''

    if vidCheck9Var.get() == 1:
        op18 = ' --include-ads '
    else:
        op18 = ''
        
# THE OUTPUT FORMAT

    #op19 = ' -o "%(title)s.%(ext)s" '


# ADVANCED VIDEO and AUDIO QUALITY and FORMAT SELECTION

    if qualCheck1Var.get() == 1:

        if qualityVar == qualities[0]:
            op1 = ' -f best '
        elif qualityVar == qualities[1]:
            op1 = ' -f worst '
        elif qualityVar == qualities[2]:
            op1 = ' -f bestvideo '
        elif qualityVar == qualities[3]:
            op1 = ' -f worstvideo '
        elif qualityVar == qualities[4]:
            op1 = ' -f bestaudio '
        elif qualityVar == qualities[5]:
            op1 = ' -f worstaudio'
    else:
        pass

    if qualCheck2Var.get() == 1:

        if qualityVar2 == qualities[0]:
            op1 = ' -f 3gp '
        elif qualityVar2 == qualities2[1]:
            op1 = ' -f aac '
        elif qualityVar2 == qualities2[2]:
            op1 = ' -f flv '
        elif qualityVar2 == qualities2[3]:
            op1 = ' -f m4a '
        elif qualityVar2 == qualities2[4]:
            op1 = ' -f mp3 '
        elif qualityVar2 == qualities2[5]:
            op1 = ' -f mp4 '
        elif qualityVar2 == qualities2[6]:
            op1 = ' -f ogg '
        elif qualityVar2 == qualities2[7]:
            op1 = ' -f wav '
        elif qualityVar2 == qualities2[8]:
            op1 = ' -f webm '
    else:
        pass

# Status Updater

    statvar.set('Downloading')

                ## The downloading part !!**************

    l = text1.get(0.1, END)

    with open('Downloaded_URLs', 'w') as downList:
        downList.write(l)
        downList.close()

    ask1 = messagebox.askyesno('INFORMATION FOR YOU', 'This application will now\nopen the terminal\nIs it okay?')

    if ask1 == 1:

        if len(text1.get(1.0, END)) <= 1:
            '''checking if at least one url is provided'''

            messagebox.showerror(' ERROR !!! ', 'you must include at lest one url'.upper())
        else:

            command = 'youtube-dl -a {} '.format(op0)+op1+op2+op3+op4+op5+op6+op7+op8+op9+op10+op11+op12+op13+op14+op15+op16+op17+op18+op19+op20
            #print("gnome-terminal -e 'bash -c \" {} && exit ; exec bash\"'".format(command))
            print(command)
            #os.system("gnome-terminal -e 'bash -c \" {} && exit ; exec bash\"'".format(command))

            for x in range(2):
                print(' DOWNLOADING>>>... ')

            messagebox.showinfo(' ** INSTRUCTION ** ', 'do not close the open window until done. \
                                You can continue on to download other videos :-)'.title())

    else:
        pass


def extraing():  # For general

    general = Toplevel()

    # Widgets

    general.config(bg='white')
    general.resizable(width=FALSE, height=FALSE)
    general.title('General Settings')
    general.geometry('650x550+300+100')


def generaling():

    global general
    global playEnt
    global playSpin1
    global playSpin2
    global vidSpin1
    global vidSpin2
    global vidSpin3
    global vidSpin4
    global vidSpin5
    global vidSpin6
    global vidEnt1
    global vidEnt2

    general = Toplevel(bg='white')
    general.grid()
    general.title(' GENERAL ')

# Playlist Frame Options
    playTop = LabelFrame(general, bg='white', fg='black', bd=3, text='Playlist Advanced Options')
    playTop.grid(row=0, column=0, padx=15, pady=5)
# Playlist Widgets
    playCheck1 = Checkbutton(playTop, selectcolor='white', bg='white', variable=playCheck1Var, fg='black',
                             command=checking1, width=0, height=0, activebackground='white', bd=0,
                             text='Playlist video items to download ', activeforeground='black')
    playCheck1.grid(row=1, column=0, padx=5, pady=5, ipadx=4)
    playEnt = Entry(playTop, textvariable=playEntVar, bg='white', fg='black', width=40,
                    state='disabled')
    playEnt.grid(row=1, column=2, padx=10, pady=5)

    playCheck2 = Checkbutton(playTop, variable=playCheck2Var, bg='white', fg='black', activebackground='white',
                             command=checking2, text=' Playlist video to start at ', activeforeground='black')
    playCheck2.grid(row=2, column=0, padx=5, pady=5, sticky=E+W)
    playSpin1 = Spinbox(playTop, from_=1, to=9999, textvariable=playSpin1Var, width=5, wrap=True, state='disabled')
    playSpin1.grid(row=2, column=2, sticky=W, padx=10)

    playCheck3 = Checkbutton(playTop, bg='white', fg='black', activebackground='white', command=checking3,
                             variable=playCheck3Var, text=' Playlist video to end at ', activeforeground='black')
    playCheck3.grid(row=3, column=0, padx=5, pady=5, sticky=E+W)
    playSpin2 = Spinbox(playTop, from_=1, to=9999, textvariable=playSpin2Var, width=5, wrap=True, state='disabled')
    playSpin2.grid(row=3, column=2, sticky=W, padx=10)

    playCheck4 = Checkbutton(playTop, bg='white', fg='black', activebackground='white', command=checking3,
                             variable=playCheck4Var, text=' Download videos in reverse order ',
                             activeforeground='black')
    playCheck4.grid(row=4, column=0, padx=5, pady=5, sticky=E+W)

    playCheck5 = Checkbutton(playTop, bg='white', fg='black', activebackground='white', command=checking3,
                             variable=playCheck5Var, text=' Download videos in random order ',
                             activeforeground='black')
    playCheck5.grid(row=5, column=0, padx=5, pady=5, sticky=E+W)
# End of playlist Widgets and playlist labelframe

# The Advanced video selection top level window
    vidFormatTop = LabelFrame(general, bg='white', fg='black', bd=3, text='Advanced Video Selection Options')
    vidFormatTop.grid(row=1, column=0, padx=15, pady=5)
# The Video selection Widgets
    vidCheck1 = Checkbutton(vidFormatTop, bg='white', fg='black', activebackground='white', command=checking4,
                            variable=vidCheck1Var, text='Max Downloads',
                            activeforeground='black')
    vidCheck1.grid(row=1, column=0, padx=5, pady=5, sticky=E + W)
    vidSpin1 = Spinbox(vidFormatTop, bg='white', fg='black', from_=1, to=999, width=4, wrap=1, textvariable=vidSpin1Var,
                       state='disabled')
    vidSpin1.grid(row=1, column=1)

    vidCheck2 = Checkbutton(vidFormatTop, bg='white', fg='black', activebackground='white', command=checking5,
                            variable=vidCheck2Var, text=' Min File size ',
                            activeforeground='black')
    vidCheck2.grid(row=2, column=0, padx=5, pady=5, sticky=E + W)
    vidSpin2 = Spinbox(vidFormatTop, bg='white', fg='black', from_=1, to=9999, width=4, wrap=1, textvariable=vidSpin2Var,
                       state='disabled',)
    vidSpin2.grid(row=2, column=1)
    vidSpin2label = Label(vidFormatTop, text='Mbs', fg='black', bg='white').grid(row=2, column=2)

    vidCheck3 = Checkbutton(vidFormatTop, bg='white', fg='black', activebackground='white', command=checking6,
                            variable=vidCheck3Var, text=' Max File size ', activeforeground='black')
    vidCheck3.grid(row=3, column=0, padx=5, pady=5, sticky=E + W)
    vidSpin3 = Spinbox(vidFormatTop, bg='white', fg='black', from_=1, to=9999, width=4, wrap=1,
                       textvariable=vidSpin3Var,
                       state='disabled', )
    vidSpin3.grid(row=3, column=1)
    vidSpin3label = Label(vidFormatTop, text='Mbs', fg='black', bg='white').grid(row=3, column=2)

    vidCheck4 = Checkbutton(vidFormatTop, bg='white', fg='black', activebackground='white', command=checking7,
                            variable=vidCheck4Var, text=' Date Before ', activeforeground='black')
    vidCheck4.grid(row=1, column=4, padx=5, pady=5, sticky=E+W)
    vidEnt1 = Entry(vidFormatTop, bg='white', fg='black', width=10, textvariable=vidEnt1Var,
                    state='disabled')
    vidEnt1.grid(row=1, column=5)

    vidCheck5 = Checkbutton(vidFormatTop, bg='white', fg='black', activebackground='white', command=checking8,
                            variable=vidCheck5Var, text=' Date After ', activeforeground='black')
    vidCheck5.grid(row=2, column=4, padx=5, pady=5, sticky=E + W)
    vidEnt2 = Entry(vidFormatTop, bg='white', fg='black', width=10, textvariable=vidEnt2Var,
                    state='disabled')
    vidEnt2.grid(row=2, column=5)

    vidCheck6 = Checkbutton(vidFormatTop, bg='white', fg='black', activebackground='white', command=checking9,
                            variable=vidCheck6Var, text=' Min Views ', activeforeground='black')
    vidCheck6.grid(row=1, column=6, padx=5, pady=5, sticky=E + W)
    vidSpin4 = Spinbox(vidFormatTop, bg='white', fg='black', from_=1, to=99999999, width=8, wrap=1,
                       textvariable=vidSpin4Var, state='disabled', )
    vidSpin4.grid(row=1, column=7)

    vidCheck7 = Checkbutton(vidFormatTop, bg='white', fg='black', activebackground='white', command=checking10,
                            variable=vidCheck7Var, text=' Max Views ', activeforeground='black')
    vidCheck7.grid(row=2, column=6, padx=5, pady=5, sticky=E + W)
    vidSpin5 = Spinbox(vidFormatTop, bg='white', fg='black', from_=1, to=99999999, width=8, wrap=1,
                       textvariable=vidSpin5Var, state='disabled', )
    vidSpin5.grid(row=2, column=7)

    vidSeparator = ttk.Separator(vidFormatTop, orient=HORIZONTAL).grid(row=4, columnspan=8, sticky=E+W)

    vidCheck8 = Checkbutton(vidFormatTop, bg='white', fg='black', activebackground='white', command=checking11,
                            variable=vidCheck8Var, text=' Age Limit ', activeforeground='black')
    vidCheck8.grid(row=5, column=0, padx=5, pady=5, sticky=E + W)
    vidSpin6 = Spinbox(vidFormatTop, bg='white', fg='black', from_=1, to=999, width=4, wrap=1,
                       textvariable=vidSpin6Var, state='disabled', )
    vidSpin6.grid(row=5, column=1)

    vidCheck9 = Checkbutton(vidFormatTop, bg='white', fg='black', activebackground='white', variable=vidCheck9Var,
                            text=' Download Adverts ', activeforeground='black')
    vidCheck9.grid(row=5, column=4, columnspan=2, padx=5, pady=5, sticky=E + W)
# The end of Video Selection options

# The output format options

    outTop = LabelFrame(general, bg='white', fg='black', text=' Output Name Formatting Options ')
    outTop.grid(row=2, column=0)

    outCheck1 = Checkbutton(outTop, selectcolor='white', bg='white', fg='black', activebackground='white',
                            text=' file output format ', activeforeground='black', variable=outCheck1Var)
    outCheck1.grid(row=1, column=1)

# The exit and save buttons
    playSaveBut = Button(general, text='Save', bg='white', fg='black', bd=2, relief=SUNKEN,
                         command=generalSaveing)
    playSaveBut.grid(row=10, column=0, sticky=E, padx=5)
    playExitBut = Button(general, text='Exit', bg='white', fg='black', bd=2, relief=SUNKEN,
                         command=lambda: general.destroy())
    playExitBut.grid(row=10, column=0, padx=20)

# End of save and exit buttons
    playTop.config(width=600, height=150)
    vidFormatTop.config(width=600, height=150)
    general.geometry('650x550+300+100')


def formating():

    formTop = Toplevel(mainWindow, bg='white')
# custom command
    command_frame = LabelFrame(formTop, text=' Custom Command ', bg='white', fg='black')

    command_ent = Entry(command_frame, width=55, bg='white', fg='black', textvariable=command_entVar)
    command_ent.grid(row=1, column=1, pady=10, ipady=2, padx=5)

    command_frame.grid(row=1, column=1)

# Advanced Video and Audio Quality Selection
    quality_frame = LabelFrame(formTop, text=' Advanced Video and Audio Quality Selection ', bg='white',
                               fg='black')

    checkbutton1 = Checkbutton(quality_frame, text=' Select an advanced quality ', bg='white',
                               fg='black', variable=qualCheck1Var)
    checkbutton1.grid(row=1, column=1)
    quality_drop = OptionMenu(quality_frame, quality, *qualities)
    quality_drop.grid(row=2, column=1, ipadx=10, pady=10, padx=10)

    checkbutton2 = Checkbutton(quality_frame, text=' Select a file extension ', bg='white',
                               fg='black', variable=qualCheck2Var)
    checkbutton2.grid(row=3, column=1)
    quality_drop = OptionMenu(quality_frame, quality2, *qualities2)
    quality_drop.grid(row=4, column=1, ipadx=10, pady=10, padx=10)

    quality_frame.grid(row=2, column=1)

    formTop.geometry('600x400+300+200')
    formTop.title(' Advanced Format Selection ')
    formTop.grid()

    #save buttons
    def saving1():
        messagebox.showinfo('INFO', 'Saving Configurations')
    savebut = Button(formTop, text='Save', command=saving1)


def subtitling():

    pass


def pasting():

    statvar.set('Pasting')

    keyboard.press(Key.ctrl)
    keyboard.press('v')
    keyboard.release(Key.ctrl)
    keyboard.release('v')

    addButton.config(state='normal')

    statvar.set('Done Pasting.')


def adding():

    statvar.set('Adding...')

    if len(text1.get(0.1, END)) >= 2 :
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    keyboard.press(Key.ctrl)
    keyboard.press('v')
    keyboard.release(Key.ctrl)
    keyboard.release('v')

    statvar.set('Done Adding.')


def undoing():

    statvar.set('Undone.')

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


def deleting():

    keyboard.press(Key.delete)
    keyboard.release(Key.delete)


def coping():

    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release(Key.ctrl)
    keyboard.release('c')


def opening():
    pass


def savingto():
    askdir = filedialog.askdirectory()

    destination_options.append(askdir)

    os.chdir(askdir)


def copingall():

    keyboard.press(Key.ctrl)
    keyboard.press('a')
    keyboard.release(Key.ctrl)
    keyboard.release('a')

    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release(Key.ctrl)
    keyboard.release('c')


def checking1():

    if playCheck1Var.get() == 1:
        playEnt.config(state='normal')

    elif playCheck1Var.get() == 0:
        playEnt.config(state='disabled')


def checking2():

    if playCheck2Var.get() == 1:
        playSpin1.config(state='normal')
    elif playCheck2Var.get() == 0:
        playSpin1.config(state='disabled')


def checking3():

    if playCheck3Var.get() == 0:
        playSpin2.config(state='disabled')
    elif playCheck3Var.get() == 1:
        playSpin2.config(state='normal')


def checking4():

    if vidCheck1Var.get() == 0:
        vidSpin1.config(state='disabled')
    elif vidCheck1Var.get() == 1:
        vidSpin1.config(state='normal')


def checking5():

    if vidCheck2Var.get() == 0:
        vidSpin2.config(state='disabled')
    elif vidCheck2Var.get() == 1:
        vidSpin2.config(state='normal')


def checking6():

    if vidCheck3Var.get() == 0:
        vidSpin3.config(state='disabled')
    elif vidCheck3Var.get() == 1:
        vidSpin3.config(state='normal')


def checking7():

    if vidCheck4Var.get() == 0:
        vidEnt1.config(state='disabled')
    elif vidCheck4Var.get() == 1:
        vidEnt1.config(state='normal')


def checking8():

    if vidCheck5Var.get() == 0:
        vidEnt2.config(state='disabled')
    elif vidCheck5Var.get() == 1:
        vidEnt2.config(state='normal')


def checking9():

    if vidCheck6Var.get() == 0:
        vidSpin4.config(state='disabled')
    elif vidCheck6Var.get() == 1:
        vidSpin4.config(state='normal')


def checking10():

    if vidCheck7Var.get() == 0:
        vidSpin5.config(state='disabled')
    elif vidCheck7Var.get() == 1:
        vidSpin5.config(state='normal')


def checking11():

    if vidCheck8Var.get() == 0:
        vidSpin6.config(state='disabled')
    elif vidCheck8Var.get() == 1:
        vidSpin6.config(state='normal')


def generalSaveing():

    general.destroy()


def updater():

    upcommand = 'youtube-dl -U'
    os.system("gnome-terminal -e 'bash -c \" {} ; exec bash\"'".format(upcommand))


mainWindow = Tk()

# tkinter variables
plvar = IntVar()
statvar = StringVar()
statvar.set('** Welcome To YouTube Downloader **')
playSpin1Var = StringVar()
playSpin2Var = StringVar()
playEntVar = StringVar()
playCheck1Var = IntVar()
playSpin1Var.set(0)
playCheck2Var = IntVar()
playCheck2Var.set(0)
playCheck3Var = IntVar()
playCheck3Var.set(0)
playCheck4Var = IntVar()
playCheck4Var.set(0)
playCheck5Var = IntVar()
playCheck5Var.set(0)
vidSpin1Var = IntVar()
vidSpin2Var = IntVar()
vidSpin3Var = IntVar()
vidSpin4Var = IntVar()
vidSpin5Var = IntVar()
vidSpin6Var = IntVar()
vidEnt1Var = StringVar()
vidEnt1Var.set('YYYYMMDD')
vidEnt2Var = StringVar()
vidEnt2Var.set('YYYYMMDD')
vidCheck1Var = IntVar()
vidCheck1Var.set(0)
vidCheck2Var = IntVar()
vidCheck2Var.set(0)
vidCheck3Var = IntVar()
vidCheck3Var.set(0)
vidCheck4Var = IntVar()
vidCheck4Var.set(0)
vidCheck5Var = IntVar()
vidCheck5Var.set(0)
vidCheck6Var = IntVar()
vidCheck6Var.set(0)
vidCheck7Var = IntVar()
vidCheck7Var.set(0)
vidCheck8Var = IntVar()
vidCheck8Var.set(0)
vidCheck9Var = IntVar()
vidCheck9Var.set(0)
outCheck1Var = IntVar()
outCheck1Var.set(0)
command_entVar = StringVar()
command_entVar.set(' -f COMMAND ')
qualCheck1Var = IntVar()
qualCheck1Var.set(0)
quality = StringVar()
quality.set(qualities[0])
qualCheck2Var = IntVar()
qualCheck2Var.set(0)
quality2 = StringVar()
quality2.set(qualities2[0])
qualityVar2 = quality2.get()
qualityVar = quality.get()
fop = StringVar()
fop.set(formats[0])
formatVal = fop.get()

# the menubar
menubar = Menu(mainWindow)

sub_setting = Menu(menubar, tearoff=0)
sub_setting.add_command(label='General', command=generaling)
sub_setting.add_command(label='Formats', command=formating)
sub_setting.add_checkbutton(label='Playlist', variable=plvar, underline=0)
sub_setting.add_command(label='Downloads')
sub_setting.add_command(label='general', command=generaling)


filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Download', command=downloader)
filemenu.add_command(label='Remove', command=deleting)
filemenu.add_command(label='open..', command=opening)
filemenu.add_command(label='Save To..', command=savingto)
filemenu.add_separator()
filemenu.add_cascade(label='Settings', menu=sub_setting)
filemenu.add_command(label=' Exit ', command=exit_all)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label='Undo', accelerator='ctrl+z', command=undoing)
editmenu.add_command(label='Redo', accelerator='ctrl+shift+z', command=redoing)
editmenu.add_command(label='Copy', command=coping)
editmenu.add_command(label='paste', command=pasting)
editmenu.add_command(label='Copy All', command=copingall)
editmenu.add_separator()
editmenu.add_command(label='Delete', command=deleting)
editmenu.add_command(label='Delete all', command=lambda: text1.delete(0.1, END))

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label='About')
helpmenu.add_command(label='Developer')
helpmenu.add_command(label='Manual')
helpmenu.add_separator()
helpmenu.add_command(label='Supported sites')
helpmenu.add_command(label='Update', command=updater)

menubar.add_cascade(label='File', menu=filemenu)
menubar.add_cascade(label='Edit', menu=editmenu)
menubar.add_cascade(label='Help', menu=helpmenu)


# Fonts
font1 = ('DejaVu Sans', 12)
font2 = ('Latin Modern Roman ', 11, 'normal', 'roman')


# The Widgets
canvas1 = Canvas(height=200, bg='blue', bd=4)
canvas2 = Canvas(height=70, bg='red', bd=4)
canvas3 = Canvas(height=200, bg='green', bd=4)
canvas4 = Canvas(height=50, bg='red', bd=4)

label1 = Label(canvas1, text='Enter the URL(s) below..', fg='black', bg='white', font=font1)
label2 = Label(canvas3, text='Destination: ', font=font1, anchor=E, bg='white', fg='black')

text1 = Text(canvas1, bg='white', fg='black', height=10, font=font1, undo=True, wrap=NONE,
             selectbackground='blue')  # url text entry

addButton = Button(canvas2, text='Add', bg='white', fg='green', relief=GROOVE, bd=2,
                   activebackground='green', state='disabled', command=adding)
downButton = Button(canvas4, text='Download', bg='white', fg='black', relief=RAISED, bd=3, command=downloader)
pasteButton = Button(canvas2, text='paste', bg='white', fg='black', command=pasting)

statusbar = Canvas(mainWindow, bg='blue', height=3,)
status = Label(statusbar, font=font2, bg='white', bd=3, fg='black', textvariable=statvar)

separator1 = ttk.Separator(canvas3, orient=VERTICAL)


vidformatop = OptionMenu(canvas2, fop, *formats)

savetoOpt = ttk.Combobox(canvas3, font=13, values=destination_options)  # Destination drop down

frame = Frame(canvas3, height=200, bg='red')


# Displaying the widgets
canvas1.pack(fill=X, pady=1)
canvas2.pack(fill=X, pady=1)
canvas3.pack(fill=X, pady=1)
canvas4.pack(fill=X, pady=1)

label1.pack(side=TOP, ipadx=2, pady=5, padx=4, anchor=W)
label2.pack(anchor=W)

text1.pack(fill=X, pady=2, padx=3)

addButton.grid(row=1, column=1, padx=10, pady=4, sticky=E)
downButton.pack(anchor=E, padx=10, pady=5, ipadx=2)
pasteButton.grid(row=1, column=2, sticky=E)

statusbar.pack(fill=X)
status.pack(anchor=W, padx=3, pady=4)


vidformatop.grid(row=1, column=0, padx=5, ipadx=4)
savetoOpt.pack(anchor=N+W, padx=4, pady=4)
separator1.pack(fill=X)

frame.pack(fill=X)

# Main window setup

mainWindow.config(bg='black', menu=menubar)
mainWindow.resizable(height=False, width=False)
mainWindow.title(' YouTube Downloader ')
mainWindow.geometry('850x620+250+200')
mainWindow.mainloop()
