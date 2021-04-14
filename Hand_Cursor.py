import mediapipe as mp
import cv2
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

prev_time =0
def FPS():
    global prev_time
    current_time = time.time()
    fps = 1/(current_time-prev_time)
    prev_time = current_time
    return fps

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            for id, landm in enumerate(handLms.landmark):
                h, w, _ = img.shape
                cx, cy = int(landm.x * w), int(landm.y * h)
                #label2['text'] = 'x = '+str(cx)+' '+'y = '+str(cy)
                if handLms !=0:
                    if id ==8:
                        #rpoints[0].append((cx, cy))
                        cv2.circle(img, (cx, cy), 3, (250, 250, 0), 6)
                    if id ==4:
                        #rpoints[0].append((cx, cy))
                        cv2.circle(img, (cx, cy), 3, (250, 250, 0), 6)
    
    
    fps = FPS()
    cv2.putText(img, 'FPS = ' + str(int(fps)), (10, 100), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
    cv2.imshow("Image",img)
    
   
    
    cv2.waitKey(1)
    
cv2.destroyAllWindows()
cap.release()