import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

def preprocessing(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv2.Canny(imgBlur,200,200)
    kernel = np.ones((5,5))
    imgDial = cv2.dilate(imgCanny, kernel, iterations=2)
    imgThres = cv2.erode(imgDial, kernel, iterations=1)
    return imgThres

def getContour(img):
    biggest = np.array([])
    maxArea = 0
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for con in contours:
        area = cv2.contourArea(con)
        if area>5000:
            cv2.drawContours(imgCon, con, -1, 255, 3)
            peri = cv2.arcLength(con, True)
            approx = cv2.approxPolyDP(con, 0.02*peri, True)
            if area>maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area
    return biggest

while True:
    _, frame = cap.read()

    imgCon = frame.copy()
    imgThres = preprocessing(frame)
    getContour(imgThres)
    cv2.imshow("frame",imgCon)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.release()
cv2.destroyAllWindows()