from tkinter import *


mainWindow = Tk()

# The MenuBar

menubar = Menu(mainWindow, tearoff=False)

filemenu = Menu(tearoff=False)
filemenu.add_command(label='New')
filemenu.add_command(label='Open..')

helpmenu = Menu(tearoff=False)
helpmenu.add_command(label='About')
helpmenu.add_command(label='Help..')

menubar.add_cascade(label='File', menu=filemenu, underline=0)
menubar.add_cascade(label='Help', menu=helpmenu, underline=0)


mainWindow.config(bg='white', menu=menubar)
mainWindow.geometry('500x400+200+100')
mainWindow.title('Pytube GUI')
mainWindow.mainloop()