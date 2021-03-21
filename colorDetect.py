import cv2
import numpy as np
import random

cap = cv2.VideoCapture(0)

while True: 
    _, frame = cap.read()

    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #blue detect 
    lower_blue = np.array([90,50,50])
    upper_blue = np.array([130,255,255])

    #red detect 
    lower_red = np.array([150,150,50])
    upper_red = np.array([180,255,150])

    mask_blue = cv2.inRange(img_hsv, lower_blue, upper_blue)
    mask_red = cv2.inRange(img_hsv, lower_red, upper_red)
    res_blue = cv2.bitwise_and(frame, frame, mask=mask_blue)
    res_red = cv2.bitwise_and(frame, frame, mask= mask_red)

    cv2.imshow("hsv", res_blue)
    cv2.imshow("video", res_red)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()