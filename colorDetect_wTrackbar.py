import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def empty():
    pass
#create Track bar
cv2.namedWindow("Trackbars")
cv2.createTrackbar("Hue min","Trackbars",0,179,empty) #Hue in opencv from 0-179
cv2.createTrackbar("Hue max","Trackbars",179,179,empty)
cv2.createTrackbar("Sat min","Trackbars",0,255,empty)
cv2.createTrackbar("Sat max","Trackbars",255,255,empty)
cv2.createTrackbar("Val min","Trackbars",0,255,empty)
cv2.createTrackbar("Val max","Trackbars",255,255,empty)

while True:
    _,frame = cap.read()
    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #get value from track bars
    h_min = cv2.getTrackbarPos("Hue min","Trackbars")
    h_max = cv2.getTrackbarPos("Hue max","Trackbars")
    sat_min = cv2.getTrackbarPos("Sat min","Trackbars")
    sat_max = cv2.getTrackbarPos("Sat max","Trackbars")
    val_min = cv2.getTrackbarPos("Val min","Trackbars")
    val_max = cv2.getTrackbarPos("Val max","Trackbars")

    #mask
    lower = np.array([h_min,sat_min,val_min])
    upper = np.array([h_max,sat_max,val_max])
    mask = cv2.inRange(img_hsv,lower,upper)
    img_res = cv2.bitwise_and(frame,frame, mask=mask)
    print(h_min,h_max,sat_min,sat_max,val_min,val_max)

    cv2.imshow("mask",mask)
    cv2.imshow("Res",img_res)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.release()
cv2.destroyAllWindows()