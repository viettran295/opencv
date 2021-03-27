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

while True:
    _, frame = cap.read()

    imgThres = preprocessing(frame)
    cv2.imshow("frame",imgThres)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.release()
cv2.destroyAllWindows()