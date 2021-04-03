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

def calculateAngle(far,start,end):
    #cosine rule
    a = math.sqrt((end[0]-start[0])**2+(end[1]-start[1])**2)
    b = math.sqrt((far[0]-start[0])**2+(far[1]-start[1])**2)
    c = math.sqrt((end[0]-far[0])**2+(end[1]-far[1])**2)
    angle = math.acos((b**2 + c**2 - a**2)/(2*b*c))
    return angle

def getMaxContour(img,thresh):
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    #choose and draw max Area
    contours = max(contours, key=lambda x: cv2.contourArea(x))
    #find convexity defects (bulged inside)->returnPoints=False
    hull = cv2.convexHull(contours, returnPoints=False)
    # cv2.drawContours(img, [hull], -1, (0,255,255),2)
    cv2.drawContours(img, [contours], -1, (255,0,0), 2)
    defects = cv2.convexityDefects(contours, hull)
    if defects is not None:
        cnt = 0
        for i in range(defects.shape[0]):
            s,e,f,d = defects[i,0]
            start = tuple(contours[s,0])
            end = tuple(contours[e,0])
            far = tuple(contours[f,0])
            angle = calculateAngle(far,start,end)
            if angle<=math.pi/2:
                cnt+=1
    cv2.putText(img,str(cnt),(0,100),cv2.FONT_HERSHEY_COMPLEX,4,(255,255,0),2,cv2.LINE_AA)            
    return img

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