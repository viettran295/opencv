import cv2
import numpy as np 

img = cv2.imread("nguynmap.jpg")
img = cv2.rectangle(img, (320,320),(600,600),(114,188,212), -1)

cv2.imshow("img",img)
cv2.waitKey(0)