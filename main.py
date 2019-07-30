import os
from tkinter import *
import tkinter.messagebox
from pygame import mixer
from tkinter import filedialog

root = Tk()  # create window

# create menubar
menuBar = Menu(root)
root.config(menu=menuBar)  # We want menubar fixed at top and should have submenus


def browse_file():
    global filename
    filename = filedialog.askopenfilename()
    # print(filename)


# create submenu
subMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open", command=browse_file)
subMenu.add_command(label="Exit", command=root.destroy)


def about_us():
    tkinter.messagebox.showinfo('About Melody', 'This is a music player built by python Tkinter.')


subMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About Us", command=about_us)

mixer.init()  # initialize mixer for playing music

# root.geometry('300x300')  # give the size of window
root.title('Spotify')  # title of the window
root.iconbitmap(r'Images/spotify.ico')  # image on the title bar

fileLabel = Label(root, text='Lets make some noise')  # Adding text inside the window
fileLabel.pack(pady=10)

'''lengthLabel = Label(root,text='Total Length - 00:00')
lengthLabel.pack()'''

def show_details():
    fileLabel['text']='Playing'+' - '+os.path.basename(filename);
    '''a = mixer.Sound(filename.name)
    total_length = a.get_length()
    mins,secs = divmod(total_length,60)
    mins = round(mins)
    secs = round(secs)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    lengthLabel['text'] = "Total Length" + ' - ' + timeformat
    # print(total_length)'''



def play_music():
    global paused

    if paused:
        mixer.music.unpause()
        statusBar['text']='Music Resumed'
        paused=FALSE
    else:
        try:
            mixer.music.load(filename)
            mixer.music.play()
            statusBar['text'] = 'Playing Music' + ' ' + os.path.basename(filename)
            show_details()
        except:
            tkinter.messagebox.showerror('File not found', 'Spotify could not find the file.Please check again')




def stop_music():
    mixer.music.stop()
    statusBar['text'] = 'Music Stopped' + ' ' + os.path.basename(filename)

paused = FALSE
def pause_music():
    global paused
    paused = TRUE
    mixer.music.pause()
    statusBar['text'] = 'Music Paused' + ' ' + os.path.basename(filename)


def rewind_music():
    play_music()
    statusBar['text'] = 'Music Restarted'


def set_vol(val):
    volume = int(val) / 100  # convert value to int and mixer takes value form 0 to 1
    mixer.music.set_volume(volume)

muted=FALSE


def mute_music():
    global muted
    if muted:  # unmute
        mixer.music.set_volume(0.01)
        volumeBtn.configure(image=volumePhoto)
        scale.set(10)
        muted=FALSE
    else: #mute
        mixer.music.set_volume(0)
        volumeBtn.configure(image=mutePhoto)
        scale.set(0)
        muted=TRUE


middleframe = Frame(root)
middleframe.pack(pady=30, padx=30)

playPhoto = PhotoImage(file='Images/play.png')  # Adding image
playBtn = Button(middleframe, image=playPhoto, command=play_music)
playBtn.grid(row=0, column=0, padx=10)

stopPhoto = PhotoImage(file='Images/stop.png')  # Adding image
stopBtn = Button(middleframe, image=stopPhoto, command=stop_music)
stopBtn.grid(row=0, column=1, padx=10)

pausePhoto = PhotoImage(file='Images/pause.png')  # Adding image
pauseBtn = Button(middleframe, image=pausePhoto, command=pause_music)
pauseBtn.grid(row=0, column=2, padx=10)

bottomframe = Frame(root)
bottomframe.pack(pady=10)

rewindPhoto = PhotoImage(file='Images/rewind.png')  # Adding image
rewindBtn = Button(bottomframe, image=rewindPhoto, command=rewind_music)
rewindBtn.grid(row=0, column=0)

mutePhoto = PhotoImage(file='Images/mute.png')  # Adding image
volumePhoto = PhotoImage(file='Images/speaker.png')  # Adding image
volumeBtn = Button(bottomframe, image=volumePhoto, command=mute_music)
volumeBtn.grid(row=0, column=1)

scale = Scale(bottomframe, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(10)
mixer.music.set_volume(0.01)
scale.grid(row=0, column=2, pady=15, padx=30)

statusBar = Label(root, text="Welcome to Spotify", relief=SUNKEN, anchor=W)  # W-west leftside
statusBar.pack(side=BOTTOM, fill=X)

root.mainloop()  # keeps running
