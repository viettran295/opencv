import cv2
import mediapipe as mp 

cap = cv2.VideoCapture(0)
mp_hand = mp.solutions.hands
hands = mp_hand.Hands()
mp_draw = mp.solutions.drawing_utils

while True:
    _, frame = cap.read()
    imgRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    res = hands.process(imgRGB)
    #if result contain value of landmarks
    if res.multi_hand_landmarks:
        for hand in res.multi_hand_landmarks:
            #position x,y,z of hand
            print(hand)
            mp_draw.draw_landmarks(frame,hand,mp_hand.HAND_CONNECTIONS)
            #convert x,y,z to pixel 
            for id, lm in enumerate(hand.landmark):
                h,w,c = frame.shape
                cx,cy = int(lm.x*w), int(lm.y*h)
                print(id,cx,cy)

    cv2.imshow("frame",frame)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()