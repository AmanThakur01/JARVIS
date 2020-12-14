import numpy as np
import cv2

def stackImage(scale,imgArray):
    rows=len(imgArray)
    cols=len(imgArray[0])
    rowsAvalable = isinstance(imgArray[0],list)
    width=imgArray[0][0].shape[1]
    height=imgArray[0][0].shape[0]
    if rowsAvalable:
        for x in range(0,rows):
            for y in range(0,cols):
                if imgArray[x][y].shape[:2]==imgArray[x][y].shape[:2]:
                    imgArray[x][y] =cv2.resize(imgArray[x][y],(0,0),None)
                else:
                    imgArray[x][y] =cv2.resize(imgArray[x][y],(imgArray[0][0],imgArray[0][0]),None)


