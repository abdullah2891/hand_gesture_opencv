import cv2
import pyautogui as mouse

__author__ = 'Abdullah_Rahman'


hand = cv2.CascadeClassifier('Hand.Cascade.1.xml')
cap=cv2.VideoCapture(0)



while(1):
    ret, frame= cap.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    pos_hand=hand.detectMultiScale(
        frame,
        scaleFactor=1.5,
        minNeighbors=6,
        minSize=(40, 40)
    )




    for (x,y,w,h) in pos_hand:
        mouse.moveTo(x,y)
        cv2.rectangle(frame, (x,y),(x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]



    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()






