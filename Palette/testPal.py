import cv2 
import numpy as np
import pandas as pd

index = ["color","color name", "hex", "R", "G", "B"]
csv = pd.read_csv("colors.csv", names=index)

for i in range(10):
    R = 0
    G = 66
    B = 66
    d = abs(R-int(csv.loc[i,"R"])) + abs(G-int(csv.loc[i,"G"])) + abs(B-int(csv.loc[i-"B"]))
    print(d)