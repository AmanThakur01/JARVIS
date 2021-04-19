import cv2
import numpy as np

img = cv2.imread("shapes.jpg")
imgrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgblur = cv2.GaussianBlur(imgrey, (7, 7), 1)
imgcanny = cv2.Canny(imgblur, 50, 50)
imgcnt = img.copy()


def getContours(imgcany):
    contours, hierarchy = cv2.findContours(imgcany, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 100:
            cv2.drawContours(imgcnt, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            objCor = len(approx)
            if objCor == 3: objTyp = "Triangle"
            elif objCor == 4:
                aspRatio=w/float(h)
                if aspRatio>0.95 and aspRatio<1.25:
                    objTyp= "Square"
                else:objTyp='Rectangle'
            else:objTyp='circle'
            cv2.putText(img, objTyp, (x + (w // 2) - 10, y + (h // 2) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        (0, 255, 255), 2)

            print(objCor)
            print(peri)
        print(area)


getContours(imgcanny)
cv2.imshow("out canny", imgcanny)
cv2.imshow("cnt", imgcnt)
cv2.imshow("img", img)
cv2.waitKey()
