import cv2 
import numpy as np

img = cv2.imread("palette.jpg")

palette = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
clicked = False
b = g = r = x_pos = y_pos = 0
def draw_fucntion(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global r, g, b, clicked, x_pos, y_pos
        clicked = True
        x_pos = x
        y_pos = y
        b, r, g = palette[y,x]
        b = int(b)
        r = int(r)
        g = int(g)

cv2.namedWindow("palette")
cv2.setMouseCallback("palette", draw_fucntion)
while True: 
    cv2.imshow("palette", palette)
    if(clicked == True):
        cv2.rectangle(palette, (10,20),(750,60),(b,r,g),-1)
        clicked = False
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()