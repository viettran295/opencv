import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = cap.get(3)
    print(width)
    cv2.imshow("video", frame)
    if cv2.waitKey(0) == ord('q'):
        break
