import cv2 
import numpy as np 

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)

    corners = cv2.goodFeaturesToTrack(gray, 150, 0.01, 10)
    corners = np.int0(corners)

    for i in corners:
        x,y = i.ravel()
        cv2.circle(frame,(x,y),3,(0,0,255),-1)
    cv2.imshow("corner", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
