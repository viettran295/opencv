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

    #combine mask red and blue
    mask = cv2.bitwise_or(mask_blue, mask_red)

    res_blue = cv2.bitwise_and(frame, frame, mask=mask_blue)
    res_red = cv2.bitwise_and(frame, frame, mask= mask_red)

    #filtered video red and blue
    res = cv2.bitwise_and(frame,frame, mask=mask)

    # #smoothing
    # kernel = np.ones((15,15), np.float32)/225
    # smooth = cv2.filter2D(res, -1, kernel)
    # blur = cv2.GaussianBlur(res, (15,15),0)
    # medianBlur = cv2.medianBlur(res,15)

    #morphological trans
    # kernel = np.ones((5,5),np.uint8)
    # erosion = cv2.erode(frame, kernel, iterations=1)
    # #binary OR
    # dilation = cv2.dilate(frame, kernel, iterations=1)

    cv2.imshow("erosion", erosion)
    cv2.imshow("dialtion", dilation)
    cv2.imshow("res",res)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()