import cv2
import numpy as np 
import math

cap = cv2.VideoCapture(0)

def preprocess(img):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #color of skin
    lower = np.array([0,48,80])
    upper = np.array([20,255,255])
    mask = cv2.inRange(img_hsv,lower,upper)
    # hand = cv2.bitwise_and(img,img, mask=mask)
    return mask
def threshhold(mask):   
    blurred = cv2.blur(mask,(2,2))
    ret, thresh = cv2.threshold(blurred,0,255,cv2.THRESH_BINARY)
    return thresh
    
def getMaxContour(img,thresh):
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = max(contours, key=lambda x: cv2.contourArea(x))
    hull = cv2.convexHull(contours)
    cv2.drawContours(img, [hull], -1, (0,255,255),2)
    cv2.drawContours(img, [contours], -1, (255,0,0), 2)
    return img
    # defects = cv2.convexityDefects(contours,hull)
    # if defects is not None:
    #     print("defect")

def calculateAngle(far,start,end):
    #cosine rule
    a = math.sqrt((end[0]-start[0])**2+(end[0]-start[0])**2)
    b = math.sqrt((far[0]-start[0])**2+(far[0]-start[0])**2)
    c = math.sqrt((end[0]-far[0])**2+(end[0]-far[0])**2)
    angle = math.acos((b**2+c**2-a**2)/(2*b*c))
    return angle

# def countFinger(contour):
#     hull = cv2.convexHull(contour)
#     if len(hull)>3:
#         defects = cv2.convexityDefects(contour, hull)
#         cnt = 0
#         if defects is not None:
#             for i in range(defects.shape[0]):
#                 s,e,f,d = defects[i,0]
#                 start = tuple(contour[s,0])
#                 end = tuple(contour[e,0])
#                 far = tuple(contour[f,0])
#                 angle = calculateAngle(far,start,end)
#                 if d>1000 and angle<=math.pi/2:
#                     cnt+=1
#         return cnt
#     return 0

while True:
    _,frame = cap.read()
    mask = preprocess(frame)
    thresh = threshhold(mask)
    contour = getMaxContour(frame,thresh)
    
    cv2.imshow("origin",contour)
    cv2.imshow("thresh",thresh)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()