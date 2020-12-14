import cv2
import numpy as np
img=cv2.imread("card.png")      #(x=512,y=398)
width,height=220,320
pts1=np.float32([[300,37],[512,100],[418,397],[212,344]])
pts2=np.float32([[0,0],[width,0],[width,height],[0,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgout=cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("output image",img)
cv2.imshow("output image2",imgout)

himg=np.hstack((img,img))

cv2.imshow("output image3",himg)
cv2.waitKey(0)