import cv2
import numpy as np
import random

img = cv2.imread("nguynmap.jpg")
cap = cv2.VideoCapture(0)

while True: 
    ret, frame = cap.read()
    # image = np.zeros(cap.shape, np.uint8)
    smaller_frame = cv2.resize(frame,(0,0), fx=0.5, fy=0.5)
    cv2.imshow('video', smaller_frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
