import cv2
import numpy as np
'''image open in window'''
# img=cv2.imread("girl_face.jpg")
# cv2.imshow("output image",img)
# cv2.waitKey(0)

'''video open in window'''
# vdcap = cv2.VideoCapture("face_video.mp4")
# while True:
#     success,img=vdcap.read()
#     cv2.imshow("output",img)
#     if cv2.waitKey(1)and 0xFF==ord('q'):
#         break
#     else:pass
'''webcam in window'''
# vdcap = cv2.VideoCapture(0)
# vdcap.set(3,640)
# vdcap.set(4,440)
# while True:
#     success,img=vdcap.read()
#     cv2.imshow("output video",img)
#     if cv2.waitKey(1)and 0xFF==ord('q'):
#         break
#     else:pass

'''basics function'''
# kernel = np.ones((3,3),np.uint8)#3,3 means square matrix box width
# img=cv2.imread("girl_face.jpg")
# imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgblur=cv2.GaussianBlur(imgGray,(7,7),0)# always take odd integer
# cannyimg = cv2.Canny(imgGray,100,100)
# cv2.imshow("output3",cannyimg)
# imgdilation = cv2.dilate(cannyimg,kernel,iterations=1)
# imgerode = cv2.erode(imgdilation,kernel,iterations=5)
# cv2.imshow("output",imgGray)
# cv2.imshow("output4",imgdilation)
# cv2.imshow("output5",imgerode)
# cv2.imshow("output2",imgblur)
# cv2.waitKey(0)

'''resize'''
# img=cv2.imread("girl_face.jpg")
# print(img.shape)# output--->(hight,length,RBG)
# resizeimg=cv2.resize(img,(700,517))#(length,height)
# imgcroped=img[0:10,790:870]#(height:width)
# cv2.imshow("output image",img)
# cv2.imshow("output image crop",imgcroped)
# # cv2.imshow("output image2",resizeimg)
# cv2.waitKey(0)

'''image'''
img=np.zeros((300,300,3),np.uint8)
# img[:]=(255,0,0)
# cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
# cv2.rectangle(img,(0,0),(255,255),(0,0,255),4)
# cv2.rectangle(img,(0,0),(255,255),(0,0,255),cv2.FILLED)
# cv2.circle(img,(255,255),50,(243,7,78),5,11)
cv2.putText(img,"JARVIS",(200,100),cv2.FONT_HERSHEY_COMPLEX,1,(200,200,200),2)
cv2.imshow("output image2",img)
print(img)
cv2.waitKey(0)
