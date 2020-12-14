from pygame import mixer
from time import time
from datetime import datetime
k = 1


def playmusic(file, stopper):
    global k
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    # time.sleep(180)
    while k > 0:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

def logmsg(msg):
    with open("msg.txt", "a") as f:
        f.write("{0} {1}\n".format(msg, datetime.now()))


if __name__ == "__main__":
    water_time = time()
    eye_time = time()
    physical_time = time()
    watersecs = 25   #30
    eyesecs = 30    #45
    physicalsecs = 20   #40
    while k > 0:
        if time() - water_time > watersecs:
            print("This is water drinking time. Enter 'drank' to stop")
            playmusic("../JARVIS/Calming-river.mp3", "drank")
            water_time = time()
            logmsg("Drank at ")
        if time() - eye_time > eyesecs:
            print("This is Eyes exercise time. Enter 'done' to stop")
            playmusic("../JARVIS/brownrang.mp3", "done")
            eye_time = time()
            logmsg("Exercise done at ")
        if time() - physical_time > physicalsecs:
            print("This is exercise time. Enter 'done' to stop")
            playmusic("../JARVIS/brownrang.mp3", "done")
            physical_time = time()
            logmsg("Exercise done at ")