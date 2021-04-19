import cv2

vdcap = cv2.VideoCapture(0)
vdcap.set(3, 640)
vdcap.set(4, 440)

def face(img):
    eyeCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    smileCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
    # img = cv2.imread('grpPic.jpeg')
    igrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = faceCascade.detectMultiScale(igrey, 1.1, 2)
    eye = eyeCascade.detectMultiScale(igrey, 1.1, 12)
    smile = smileCascade.detectMultiScale(igrey, 1.2, 12)

    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 210), 2)

        for x, y, w, h in smile:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
        for ex, ey, ew, eh in eye:
            cv2.rectangle(img, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)
    # cv2.imshow('face', img)
    # cv2.waitKey()
    return img

while True:
    success, img = vdcap.read()
    imgFace = face(img)
    cv2.imshow("output video", imgFace)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
    else:
        pass
