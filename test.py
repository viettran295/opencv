import cv2
import numpy as np 

img = cv2.imread("Lenna.png")

width = int(img.shape[0]*50/100)
height = int(img.shape[1]*50/100)
dim = (width, height)

img_resize = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
img_resize1 = cv2.resize(img, dim, interpolation=cv2.INTER_LINEAR)

img_hsv = cv2.cvtColor(img_resize, cv2.COLOR_BGR2HSV)
img_hsv = cv2.rectangle(img_resize, (0,0), (100,100), (0,150,150), -1)
img_cat = np.concatenate((img_resize, img_hsv, img_resize1), axis=1)

cv2.imshow("ori", img)
cv2.imshow("cat", img_cat)
cv2.waitKey(0)
cv2.destroyAllWindows()