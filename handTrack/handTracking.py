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
        res = self.hands.process(imgRGB)
        print(res.multi_hand_landmarks)
        #hand detect
        if res.multi_hand_landmarks:
            #show detected hands
            for hand in res.multi_hand_landmarks:
                #detect 20 points per hand
                for id, lm in enumerate(hand.landmark):
                    h,w,c = frame.shape
                    #convert float to pixel
                    cx, cy = int(lm.x*w), int(lm.y*h)
                    print(id,cx,cy)
                    #detect the point number 0
                    if id == 0:
                        cv2.circle(frame,(cx,cy),5,(255,0,255),-1)
                if draw:
                    self.mp_draw.draw_landmarks(frame, hand, self.mp_hands.HAND_CONNECTIONS)
        return frame

def main():
    cap = cv2.VideoCapture(0)
    detect = handDetect()
    while True:
        _, frame = cap.read()
        detect.findHands(frame)
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) == ord('q'):
            break
    
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
