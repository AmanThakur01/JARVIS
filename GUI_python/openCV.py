from tkinter import *
import cv2
from tkinter import ttk
from ttkthemes import themed_tk as tk
root = tk.ThemedTk()
root.get_themes()
root.set_theme('adapta')

vdcap = cv2.VideoCapture("face_video.mp4")
while True:
    success,img=vdcap.read()
    if success:
        cv2.imshow('root',img)
        if cv2.waitKey(25)and 0xFF==ord('q'):
            break
        else:pass

    else:
        print("not lode file")
