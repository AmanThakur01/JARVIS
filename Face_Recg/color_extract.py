import cv2
import numpy as np
def empty(a):
    pass
# img=cv2.imread("girl_face.jpg")
cv2.namedWindow("TrackBar")
cv2.resizeWindow("TrackBar",640,240)
cv2.createTrackbar("h_mini","TrackBar",0,179,empty)
cv2.createTrackbar("h_max","TrackBar",89,179,empty)
cv2.createTrackbar("s_mini","TrackBar",0,255,empty)
cv2.createTrackbar("s_max","TrackBar",118,255,empty)
cv2.createTrackbar("v_mini","TrackBar",151,255,empty)
cv2.createTrackbar("v_max","TrackBar",255,255,empty)
while True:
    img = cv2.imread("girl_face.jpg")
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_mini = cv2.getTrackbarPos("h_mini","TrackBar")
    h_max = cv2.getTrackbarPos("h_max","TrackBar")
    s_mini = cv2.getTrackbarPos("s_mini","TrackBar")
    s_max = cv2.getTrackbarPos("s_max","TrackBar")
    v_mini = cv2.getTrackbarPos("v_mini","TrackBar")
    v_max = cv2.getTrackbarPos("v_max","TrackBar")
    print(h_mini,h_max,s_mini,s_max,v_mini,v_max)
    lower=np.array([h_mini,s_mini,v_mini])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imgHSV,lower,upper)
    imgRes = cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow("output image",img)
    cv2.imshow("HSV image",imgHSV)
    cv2.imshow("mask image",mask)
    cv2.imshow("result image",imgRes)
    cv2.waitKey(1)