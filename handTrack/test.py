import cv2
import numpy as np

cap = cv2.VideoCapture(0)
def preprocess(img):
    img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower = np.array([0,48,80])
    upper = np.array([20,255,255])
    mask = cv2.inRange(img_hsv,lower,upper)
    ret,thresh = cv2.threshold(mask,0,255,cv2.THRESH_BINARY)
    return thresh

while True:
    _, frame = cap.read()
    thresh = preprocess(frame)
    contours,hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    contours = max(contours, key= lambda x: cv2.contourArea(x))
    cv2.drawContours(frame,[contours], -1, (255,0,0), 2)
    cv2.imshow("origin",frame)
    cv2.imshow("frame",thresh)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()