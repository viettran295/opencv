import cv2
import numpy as np 

img = cv2.imread("noiseImg.jpg")

kernel = np.ones((5,5),np.float32)/25
smooth = cv2.filter2D(img, -1, kernel)
gauss = cv2.GaussianBlur(img,(5,5),0)
median = cv2.medianBlur(img,5)
bilateral = cv2.bilateralFilter(img,5,75,75)

img_con = np.concatenate((img,bilateral,gauss,median), axis=1)

cv2.imshow("img",img_con)
cv2.waitKey(0)
cv2.destroyAllWindows()

