import cv2 
import numpy as np
import pandas as pd

green = np.uint8([0,255,0])
hsv = cv2.cvtColor(green,cv2.COLOR_RGB2HSV)
cv2.imshow("green",green)