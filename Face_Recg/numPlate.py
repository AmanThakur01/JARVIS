import cv2

vdcap = cv2.VideoCapture(0)
vdcap.set(3,640)
vdcap.set(4,440)

nPlateCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_russian_plate_number.xml')
# img = cv2.imread('grpPic.jpeg')

while True:
    success,img=vdcap.read()
    igrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numPlate = nPlateCascade.detectMultiScale(igrey, 1.3, 15)

    for x, y, w, h in numPlate:
        area=w*h
        if area>50:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img,"Number Plate",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,(255,233,45),2)
            imgRoi=img[y:y+h,x:x+w]
            cv2.imshow("imgRoi",imgRoi)

    cv2.imshow("output video",img)
    if cv2.waitKey(1)and 0xFF==ord('s'):
        break
    else:pass