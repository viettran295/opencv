import cv2
import mediapipe as mp 
import time 

class handDetect():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon 

        self.mp_hands = mp.solutions.hands
        self.mp_draw = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands(self.mode,self.maxHands,
                                        self.detectionCon,self.trackCon)
    def findHands(self,frame,draw=True):
        imgRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        self.res = self.hands.process(imgRGB)
        #hand detect
        if self.res.multi_hand_landmarks:
            for hand in self.res.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(frame, hand, self.mp_hands.HAND_CONNECTIONS)
        return frame

    def findPosition(self,frame,handNumber=0, draw=True):
        lmlist = []
        if self.res.multi_hand_landmarks:
            myHand = self.res.multi_hand_landmarks[handNumber]
            #detect 20 points per hand
            for id, lm in enumerate(myHand.landmark):
                h,w,c = frame.shape
                #convert float to pixel
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmlist.append([id,cx,cy])
                if draw:
                    cv2.circle(frame,(cx,cy),5,(255,0,255),-1)
        return lmlist
def main():
    cap = cv2.VideoCapture(0)
    detect = handDetect()
    while True:
        _, frame = cap.read()
        detect.findHands(frame)
        lmlist = detect.findPosition(frame)
        if len(lmlist)!=0:
            #position of thumbs
            print(lmlist[4])

        cv2.imshow("frame", frame)
        if cv2.waitKey(1) == ord('q'):
            break 
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
