import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    
    #in Laplace convert
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    #Edge detect with Canny
    edge = cv2.Canny(frame, 100, 100)

    cv2.imshow("origin",frame)
    cv2.imshow("Lap64", laplacian)
    cv2.imshow("canny",edge)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows() 
cap.release()