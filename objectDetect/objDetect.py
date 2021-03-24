import cv2
import numpy as np 

face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye = cv2.CascadeClassifier('haarcascade_eye.xml')
eyeglass = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h),255,2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]
        # eye = eye.detectMultiScale(roi_gray, 1.3, 5)
        eyeglasses = eyeglass.detectMultiScale(roi_gray, 1.3, 5)
        for(ex,ey,ew,eh) in eyeglasses:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv2.imshow("video",frame)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
cv2.release()