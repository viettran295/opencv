import cv2
import numpy as np 

img = cv2.imread("contourImg.png")
height = 640
width = 320
img_resize = cv2.resize(img,(height,width))
img_gray = cv2.cvtColor(img_resize, cv2.COLOR_BGR2GRAY)
contours, hierarchy = cv2.findContours(img_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("before: ", contours)
contours = max(contours, key= lambda x: cv2.contourArea(x))
print(x)
print("after: ", contours)

cv2.imshow("gray",img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()