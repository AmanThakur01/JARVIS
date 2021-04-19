from tkinter import *
import cv2
import numpy as np
from PIL import ImageTk,Image

class stack():
    def takeImg(self,*lst):
        print(type(lst))
        root = Tk()
        root.title('image stack')
        root.geometry('800x500')

        label1 = Label(width="100", highlightbackground='black', highlightthicknes=3)
        label1.grid(row=0, column=0, ipadx=1, ipady=1)
        im={}
        for i, img in enumerate(lst):
            print(i)
            im[i]=cv2.resize(img,(100,100))
            print(type(im))
            print(im)
            cv2.imshow("Image number {}".format(i), img)
        index=0
        # imCon={}
        mCon = cv2.vconcat((im[0], im[1]))

        # while len(im)>=index:
        #     y=index+1
        #     imCon = np.concatenate((im[index], im[y]), axis=1)
        #     index+=2

        # root = Tk()
        # root.title('image stack')
        # root.geometry('800x500')
        #
img=Image.open('shapes.png')
img2=Image.open('card.png')
        # img1=img.resize((100,100), Image.ANTIALIAS)
        # img2 = img2.resize((100,100), Image.ANTIALIAS)
        # self = ImageTk.PhotoImage(img1)
        #
        # label1=Label(width="100",highlightbackground='black',highlightthicknes=3)
        # label1.grid(row=0,column=0,ipadx=1,ipady=1)
        # l1=Label(label1,image=self)
        # l1.grid()#row=0,column=0,ipadx=1,ipady=1)
        #
        # label2=Label(width="100",highlightbackground='black',highlightthicknes=3)
        # label2.grid(row=0,column=1,ipadx=1,ipady=1)
        # l2=Label(label2,image=self)
        # l2.grid()#row=0,column=0,ipadx=1,ipady=1)
        #
        # label3=Label(width="100",highlightbackground='black',highlightthicknes=3)
        # label3.grid(row=1,column=0,ipadx=1,ipady=1)
        # l3=Label(label3,image=self)
        # l3.grid()#row=0,column=0,ipadx=1,ipady=1)
        #
        # label4=Label(width="100",highlightbackground='black',highlightthicknes=3)
        # label4.grid(row=1,column=1,ipadx=1,ipady=1)
        # l4=Label(label4,image=self)
        # l4.grid()#row=0,column=0,ipadx=1,ipady=1)
        #
        # root.mainloop()


stack.takeImg(img2,img2,img2,img2)