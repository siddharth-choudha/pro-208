import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

PORT  = 8050
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

listbox = None
name = None
selectSong = None


def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    MusicWindow()

def MusicWindow():
    window=Tk()

    window.title('Music Window')
    window.geometry("300x300")
    window.configure(bg='LightSkyBlue')

    global listbox
    global selectSong
    
    listbox = Listbox(window,height = 10,width = 39,activestyle = 'dotbox', borderwidth=2, font = ("Calibri",10))
    listbox.place(x=10, y=10)

    
    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)

    selectLabel = Label(window, text='Select Song', bg = 'lightBlueSky', font = ('Calibri', 8))
    selectLabel.place(x=2, y=1)

    playButton = Button(window, text= 'Play', width = 10 ,bd = 1, bg='skyBlue', font=('Calibri', 10))
    playButton.place(x = 30, y = 200)

    stopButton = Button(window, text = 'Stop', width = 10, bd=1 , bg = 'skyBlue', font = ('Calibri', 10))
    stopButton.place(x=200 ,y= 200)

    upload = Button(window, text= 'Upload', width=10, bd=1, bg='skyBlue', font=('Calibri', 10))
    upload.place(x=30 , y=250)

    Download = Button(window, text='Download', width=10, bd=1, bg='skyBlue', font=('Calibri', 10))
    Download.place(x = 200 , y=250)

    infoLabel = Label(window, text='', fg='Blue', font=('Calibri',8))
    infoLabel.place(x=4, y=280)

    window.mainloop()



setup()