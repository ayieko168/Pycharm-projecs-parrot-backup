from tkinter import *
from PIL import Image


mainWindow = Tk()

# The menubar
menubar = Menu()

filemenu = Menu(tearoff=0)
filemenu.add_command(label=' New ')
filemenu.add_command(label=' Open.. ')
filemenu.add_command(label=' Save As ')
filemenu.add_separator()
filemenu.add_command(label='Settings')

editmenu = Menu(tearoff=0)
editmenu.add_command(label=' Undo ')
editmenu.add_command(label=' redo ')
editmenu.add_separator()
editmenu.add_command(label=' cut ')
editmenu.add_command(label=' copy ')
editmenu.add_command(label=' paste ')

menubar.add_cascade(label='  File  ', underline=2, menu=filemenu)
menubar.add_cascade(label='  Edit  ', underline=2, menu=editmenu)


# The task bar
taskbar = Canvas(mainWindow, height=25, bg='green', bd=2, relief=RAISED)

# taskbar widgets

taskbar.pack(fill=X, side=TOP)

# Main Window Widgets




# MainWindow Configurations
mainWindow.config(bg='white', menu=menubar)
mainWindow.title('PIL Image Editor')
screen_width = mainWindow.winfo_screenwidth()
screen_height = mainWindow.winfo_screenheight()
mainWindow.geometry('{}x{}'.format(screen_width, screen_height))
mainWindow.mainloop()

# Started on Tuesday, May 01 2018 03:37:00 PM
