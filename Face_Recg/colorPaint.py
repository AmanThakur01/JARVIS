import cv2
import numpy as np

# from webcam

vdcap = cv2.VideoCapture(0)
vdcap.set(3, 640)
vdcap.set(4, 440)
vdcap.set(10, 150)
#0, 133, 124, 172, 255, 255
mycolor = [[20, 94, 80, 154, 202, 178],
           [69, 145, 120, 255, 21, 245],
           [45, 141, 69, 255, 0, 255]]

mycolorval=[[255,0,0],[0,255,0],[0,0,255]]

mypoints=[]#   [x,y,colorID]
# cv2.namedWindow("TrackBar")
# cv2.resizeWindow("TrackBar",640,240)
# cv2.createTrackbar("h_mini","TrackBar",0,179,empty)
# cv2.createTrackbar("h_max","TrackBar",89,179,empty)
# cv2.createTrackbar("s_mini","TrackBar",0,255,empty)
# cv2.createTrackbar("s_max","TrackBar",118,255,empty)
# cv2.createTrackbar("v_mini","TrackBar",151,255,empty)
# cv2.createTrackbar("v_max","TrackBar",255,255,empty)
def findColor(img, mycolor):
    # imgrey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count=0
    newPoints=[]
    for color in mycolor:
        # h_mini = cv2.getTrackbarPos("h_mini", "TrackBar")
        # h_max = cv2.getTrackbarPos("h_max", "TrackBar")
        # s_mini = cv2.getTrackbarPos("s_mini", "TrackBar")
        # s_max = cv2.getTrackbarPos("s_max", "TrackBar")
        # v_mini = cv2.getTrackbarPos("v_mini", "TrackBar")
        # v_max = cv2.getTrackbarPos("v_max", "TrackBar")
        # print(h_mini, s_mini,v_mini ,h_max, s_max , v_max)
        # lower = np.array([h_mini, s_mini, v_mini])
        # upper = np.array([h_max, s_max, v_max])
        lower=np.array(color[0:3])
        upper=np.array(color[3:6])
        # print(upper, lower)
        masks = cv2.inRange(imgHSV, lower, upper)
        cv2.imshow(str(color[0]), masks)
        x,y=getContours(masks)
        cv2.circle(imgRes,(x,y),10,mycolorval[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count+=1
    return newPoints

def getContours(imgcany):
    contours, hierarchy = cv2.findContours(imgcany, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 10:
            # cv2.drawContours(imgRes, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return x+w//2,y

def drawOnCanvas(mypoints,mycountval):
    for point in mypoints:
        cv2.circle(imgRes, (point[0], point[1]), 10, mycountval[point[2]], cv2.FILLED)
while True:

    success, img = vdcap.read()
    imgRes=img.copy()
    newPoints = findColor(img, mycolor)
    if len(newPoints)!=0:
        for newp in newPoints:
            mypoints.append(newp)
    if len(mypoints)!=0:
        drawOnCanvas(mypoints,mycolorval)
    cv2.imshow("output video", imgRes)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
    else:
        pass
