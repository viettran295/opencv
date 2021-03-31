import cv2
import numpy as np 

cap = cv2.VideoCapture(0)
def preprocessing(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv2.Canny(imgBlur,50,50)
    return imgCanny

def getContour(img):
    #just for binary image/ canny img
    #each contour is stored in vector
    contour, hierarchy = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    for con in contour:
        area = cv2.contourArea(con)
        if area>100:
            cv2.drawContours(imgCon,con,-1,255,2)
    return imgCon

while True:
    _,frame = cap.read()

    imgCon = frame.copy()
    prepro = preprocessing(frame)
    getContour(prepro)

    cv2.imshow("frame",imgCon)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.release()
cv2.destroyAllWindows()