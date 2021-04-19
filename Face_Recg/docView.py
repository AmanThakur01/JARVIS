import cv2
import numpy as np

##########
widthImg=380
heightImg=680
###########
vdcap = cv2.VideoCapture(0)
vdcap.set(3, widthImg)
vdcap.set(4, heightImg)
vdcap.set(10,150)

def preProcess(img):
    imgrey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgblur=cv2.GaussianBlur(imgrey,(5,5,),1)
    imgcanny=cv2.Canny(imgblur,200,200)
    kernel=np.ones((5,5))
    imgdil=cv2.dilate(imgcanny,kernel,iterations=2)
    imgerod=cv2.erode(imgdil,kernel,iterations=1)
    return imgerod

def getContours(imgcany):
    maxArea=0
    biggest=np.array([])
    contours, hierarchy = cv2.findContours(imgcany, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        cv2.drawContours(imgcnt, cnt, -1, (255, 225, 0), 2)
        if area > 4000:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            print(approx)
            if area>maxArea and len(approx)==4:
                biggest=approx
                print(biggest)
                maxArea=area
    # x, y, w, h = cv2.boundingRect(approx)
    cv2.drawContours(imgcnt, biggest, -1, (255, 0, 0), 20)
    return biggest

def reorder(mypoints):
    mypoints=mypoints.reshape((4,2))
    mypointNew=np.zeros((4,1,2),np.int32)
    add = mypoints.sum(1)
    print("add",add)
    mypointNew[0]=mypoints[np.argmin(add)]
    mypointNew[3]=mypoints[np.argmax(add)]
    print("mypointNew:",mypointNew[0],mypointNew[3])
    diff=np.diff(mypoints,axis=1)
    mypointNew[1]=mypoints[np.argmin(diff)]
    mypointNew[2]=mypoints[np.argmax(diff)]
    print("mypointNew[1]",mypointNew[1],"mypointNew[2]",mypointNew[2])
    return mypointNew

def getWrap(img,biggest):
    biggest=reorder(biggest)
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgout = cv2.warpPerspective(img, matrix, (widthImg, heightImg))
    # imgcroped=imgout[20:imgout.shape[0]-20,20,imgout.shape[1]-20]
    # imgrezized=imgcroped.resize(widthImg,heightImg)
    return imgout


while True:
    success, img = vdcap.read()
    img=cv2.resize(img,(widthImg,heightImg))
    imgcnt=img.copy()

    imgThres=preProcess(img)
    biggest=getContours(imgThres)
    if biggest.size!=0:
        imgout=getWrap(img,biggest)
        cv2.imshow("imgout", imgout)
    else:pass
    cv2.imshow("output video", imgcnt)
    cv2.imshow("imgThres", imgThres)
    # cv2.imshow("imgout", imgout)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
    else:
        pass
