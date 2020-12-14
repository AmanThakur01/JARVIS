import datetime
from pygame import mixer

rmd_time = ""
lst = dict()
keys = []
values = []
ij = 0


def music(stopper):
    mixer.init()
    mixer.music.load('../JARVIS/Calming-river.mp3')
    mixer.music.play()
    while True:
        print("Press 'Enter' to stop music.")
        stop = input()
        if stop == stopper:
            mixer.music.stop()
            break
    start_todo()


def usr_inp():
    try:
        global rmd_time, keys
        global lst
        detail = input("Enter work in todo : ")
        h1 = float(input("Enter time (e.g 24.60) : "))
        rmd_time = "{}.00".format(h1)
        ct_date = datetime.datetime.now()
        val_ct_date = ct_date.strftime("%H.%M.%S") # strftime convert into string
        if rmd_time > val_ct_date:
            keys.append(rmd_time)
            values.append(detail)
            lst = dict(zip(keys, values))
        else:
            print("Enter Future Time...!")
    except Exception:
        print("Enter Valid integers.")


def start_todo():
    global keys, ij
    while ij < len(lst):
        ct_date = datetime.datetime.now()
        val_ct_date = ct_date.strftime("%H.%M.%S")
        for i in keys:
            if i == val_ct_date:
                print("Its time to ",lst.get(i))
                ij += 1
                music("")


def print_task():
    print(lst)


while True:
    print("-----------------Welcome------------------")
    usr = int(input("Press 1. For Entry.\nPress 2. For View\nPress 3. For Start Todo Reminder.\nPress 0. For Exit\n"))
    if usr == 1:
        usr_inp()
    elif usr == 2:
        print_task()
    elif usr == 3:
        start_todo()
    elif usr == 0:
        break
    else:
        print("Enter Valid integer ..!")
