from tkinter import *
import glob
import os
from threading import Thread
import vlc
import time
from ttkthemes import themed_tk as tk
import tkinter.messagebox as km
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import imageio

player = vlc.MediaPlayer()
nextSong=0
index = 0
musicNo=True
timeformat=""
cutoff=5
addedSongList=[]
randomBoolen=False
indexRandom=0
addSongIndex=0
def playBack():
    global player,fileName,timeformat,obj,musicNo,duration,t1
    if player.is_playing()!=1 and musicNo:
        playButton.configure(image=pausePhoto)

        class playlist(Thread):
            def run(self):
                global player,nextSong,index,timeformat,musicNo,duration,cutoff,t1,songList,manuallst,addedSongList
                path = "/media/aman/Disk/music/*.mp3"
                lst = glob.glob(path)
                index=0
                # if songList.curselection():
                #     songName=songList.curselection()
                #     songIndex=int(songName[0])
                #     actualPath=addedSongList[songIndex]
                #     player=vlc.MediaPlayer(actualPath)
                #     player.play()
                #     player.audio_set_volume(50)
                # else:
                if randomBoolen:
                    manuallst=lst#[:]
                elif len(addedSongList)==0:
                    km.showerror("JARVIS 'ERROR'","Playlist EMPTY,Please select song or play randomly")
                else:
                    manuallst=addedSongList#[:]
                for i in manuallst:
                    if nextSong>1:
                        nextSong=nextSong-1
                        index = index + 1
                        continue
                    elif musicNo!=True:
                        break
                    elif len(addedSongList) == 0 and randomBoolen!=True:
                        break
                    elif songList.curselection():
                        songName=songList.curselection()
                        songIndex=int(songName[0])
                        actualPath=addedSongList[songIndex]
                        player=vlc.MediaPlayer(actualPath)
                        player.play()
                        player.audio_set_volume(50)
                    else:
                        musicNo = False
                        player = vlc.MediaPlayer(i)
                        player.play()
                        if index==0:
                            player.audio_set_volume(50)
                        else:pass
                        index = index+1
                        statusBar['text'] = "Music Playing" + " " + os.path.basename(i)
                        time.sleep(1)
                        duration=int(player.get_length()/1000)
                        min,secs=divmod(duration,60)
                        round(min),round(secs)
                        timeformat = "{}:{}".format(min,secs)
                        musicLength['text'] = ("Total length is " + timeformat)
                        global t1
                        cutoff = 10
                        t1 = newThread()
                        t1.start()
                    # elif songList.curselection():
                    #     songName=songList.curselection()
                    #     songIndex=int(songName[0])
                    #     actualPath=addedSongList[songIndex]
                    #     player=vlc.MediaPlayer(actualPath)
                    #     player.play()
                    #     player.audio_set_volume(50)
                    # else:
                    #     #popup
                    #     pass

        obj=playlist()
        obj.start()

    else:
        playButton.configure(image=playPhoto)
        player.pause()
        statusBar['text'] = "Music Paused"
        musicNo=False

class newThread(Thread):
    def run(self):
        global duration,cutoff
        while True:
            if cutoff>=0:
                while duration and player.is_playing() and cutoff>=0:
                    min, secs = divmod(duration, 60)
                    round(min), round(secs)
                    currentTime = "{}:{}".format(min, secs)
                    time.sleep(1)
                    currentLength['text'] = ("current length is " + currentTime)
                    duration -= 1
            else:
                raise Exception
    def exception(self):
            raise Exception

def pauseBack():
    global player
    player.pause()
    statusBar['text']="Music Paused"

def setVolume(vol):
    global player
    volume = float(vol)
    player.audio_set_volume(round(volume))

def aboutUs():
    km.showinfo("About Us","Jarvis player")

def fileOpen():
    global fileName
    fileName = filedialog.askopenfile()
    playBack()

sound = False
def mute():
    thread = Thread(target=stream, args=(middleLabel,))
    thread.daemon = 1
    thread.start()
    global player,sound
    if sound:
        muteButton.configure(image=mutePhoto)
        volumeScale.set(50)
        player.audio_set_volume(50)
        sound = False
    else:
        muteButton.configure(image=mutedPhoto)
        volumeScale.set(0)
        player.audio_set_volume(0)
        sound = True

def forwardPlay():
    global musicNo,t1,cutoff
    player.stop()
    cutoff = (-11)
    musicNo = True
    global nextSong,index
    nextSong=index+1
    # t1.exception()
    playBack()

def backwardPlay():
    global musicNo,t1
    t1.kill()
    musicNo = True
    player.stop()
    global nextSong, index
    nextSong = index - 1
    playBack()

def crossButton():
    if km.showinfo("JARVIS : Alert!!!","Are you closing JARVIS Player window"):
        player.stop()
        root.destroy()
    else:pass

def addSong():
    global songList,fileName,addedSongList,addSongIndex
    fileName = filedialog.askopenfilename()
    f=os.path.basename(fileName)
    songList.insert(addSongIndex,f)
    addedSongList.insert(addSongIndex,fileName)
    addSongIndex+=1
    songList.pack()

def randomPlay():
    global randomBoolen,indexRandom
    if (indexRandom%2)==0:
        randomButton.configure(image=randomIMG2)
        randomBoolen=True
    else:
        randomButton.configure(image=randomIMG)
        randomBoolen = False
    indexRandom+=1
def removeSong():
    global songList,addedSongList
    songIndex=songList.curselection()
    songValue=int(songIndex[0])
    del addedSongList[songValue]
    songList.delete(songValue)

def stream(rightFrame):
    global video
    for image in video.iter_data():
        frame_image = ImageTk.PhotoImage(Image.fromarray(image))
        rightFrame.config(image=frame_image)
        # a=100
        # ran="random.png"
        # PhotoImage.width(r)
        # PhotoImage.height(ran)
        rightFrame.image = frame_image
        time.sleep(0.01)

video_name = "face_video.mp4" #This is your video file path
video = imageio.get_reader(video_name)

root = tk.ThemedTk()
root.get_themes()
root.set_theme('adapta')

menubar = Menu(root)
root.config(menu=menubar)
submenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=submenu)
submenu.add_command(label="Exit",command=root.destroy)
submenu.add_command(label="Open",command=fileOpen)
submenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=submenu)
submenu.add_command(label="About Us",command=aboutUs)

root.title("This is JARVIS")
root.geometry("800x500")
window_text = ttk.Label(root, text = "DJ Aman Thakur to night")
window_text.pack(pady=10)

leftFrame = Frame(root,bg="light blue")
leftFrame.pack(side=LEFT)

middleFrame=Frame(root,width=100, height=200)#,width=300, height=200
middleFrame.pack()
middleLabel=ttk.Label(middleFrame)
middleLabel.pack()

rightFrame = Frame(root)
rightFrame.pack(side=RIGHT)

songList = Listbox(leftFrame)
songList.pack(side=TOP)

addButton = ttk.Button(leftFrame,text="ADD",command = addSong)
addButton.pack(side=LEFT)       #column=0,row=0

delButton = ttk.Button(leftFrame,text="DELETE",command = removeSong)
delButton.pack(side=LEFT)

topFrame = Frame(rightFrame)
topFrame.pack()
musicLength = ttk.Label(topFrame, text = "Total length is --:--"+timeformat)
musicLength.pack(pady=10)

currentLength = ttk.Label(topFrame, text = "current length is --:--"+timeformat,relief=GROOVE)#,fg="blue"
currentLength.pack(pady=10)

frame = Frame(rightFrame)
frame.pack(pady=10,padx=20,side=LEFT)

pausePhoto = PhotoImage(file ="pause-button.png")
playPhoto = PhotoImage(file = "play.png")
forward = PhotoImage(file = "fast-forward.png")
backward = PhotoImage(file = "fast-backward.png")

# pauseButton = Button(frame, image = pausePhoto,command = pauseBack)
# pauseButton.grid(row=0,column=1,padx=10)

frame2 = Frame(rightFrame)
frame2.pack(pady=10,padx=20)
mutedPhoto = PhotoImage(file="mute.png")
mutePhoto = PhotoImage(file = "megaphone.png")
muteButton = ttk.Button(frame2,image=mutePhoto,command = mute)
muteButton.grid(column=0,row=0)

volumeScale = ttk.Scale(frame2,from_=0,to=120,orient=HORIZONTAL,command=setVolume)
volumeScale.set(50)
volumeScale.grid(row=0,column=1)

randomIMG = PhotoImage(file = "random2.png")
randomIMG2 = PhotoImage(file = "random.png")
randomButton = ttk.Button(frame2,image=randomIMG,command = randomPlay)
randomButton.grid(pady=20)

statusBar = ttk.Label(text="This is JARVIS",relief=SUNKEN,font="Times 10 italic")#,anchor=W ,bg="light blue"
statusBar.pack(side=BOTTOM,fill=X)

bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)
root.protocol("WM_DELETE_WINDOW",crossButton)

playButton = ttk.Button(bottomFrame, image = playPhoto,command = playBack)
forwardButton = ttk.Button(bottomFrame, image = forward,command = forwardPlay)
backwardButton = ttk.Button(bottomFrame, image = backward,command = backwardPlay)
playButton.grid(row=0,column=1,padx=10)
forwardButton.grid(row=0,column=2,padx=10)
backwardButton.grid(row=0,column=0,padx=10)

root.mainloop()
