import cv2 
import numpy as np
import pandas as pd

img = cv2.imread("palette.jpg")
palette = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

index = ["color","color_name","hex","R","G","B"]
csv = pd.read_csv("colors.csv", names=index)

clicked = False
b = g = r = x_pos = y_pos = 0

def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R-int(csv.loc[i,"R"])) + abs(G-int(csv.loc[i,"G"]))+ abs(B-int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname
def draw_fucntion(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global r, g, b, clicked, x_pos, y_pos
        clicked = True
        x_pos = x
        y_pos = y
        b, r, g = palette[y,x]
        # b = int(b)
        # r = int(r)
        # g = int(g)
        # print(f"b = {b}, r = {r}, g = {g}")

cv2.namedWindow("palette")
cv2.setMouseCallback("palette", draw_fucntion)
while True: 
    cv2.imshow("palette", palette)
    if(clicked):
        cv2.rectangle(palette, (10,20),(750,60),(b,r,g),-1)
        # note: sequence from color
        text = getColorName(g,r,b)
        cv2.putText(palette,text, (50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
        clicked = False
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()