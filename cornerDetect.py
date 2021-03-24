import cv2 
import numpy as np 

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)

    corners = cv2.goodFeaturesToTrack(gray, 100, 0.1, 10)
    corners = np.int0(corners)

    for i in corners:
        x,y = i.ravel()
        cv2.circle(frame,(x,y),3,(0,0,255),-1)
    # thresh = 0.1*corners.max()
    # corner_img = np.copy(frame)
    # for i in range(0,corners.shape[0]):
    #     for j in range(0,corners.shape[1]):
    #         if(corners[i][j]>thresh):
    #             cv2.circle(corner_img, (i,j),1,255,-1)

    cv2.imshow("corner", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
