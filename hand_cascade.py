
import cv2
import pyautogui as mouse

__author__ = 'Abdullah_Rahman'





hand = cv2.CascadeClassifier('Hand.Cascade.1.xml')
fgbg=cv2.createBackgroundSubtractorMOG2()




cap=cv2.VideoCapture(0)

screen=mouse.size()

while(1):

    ret, frame= cap.read()


    #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #ret,thresholded=cv2.threshold(frame,90,255,cv2.THRESH_TOZERO)
    fgmask=fgbg.apply(frame)
    pos_hand=hand.detectMultiScale(
        fgmask,
        scaleFactor=1.2,
        minNeighbors=3,
        minSize=(60, 60)
    )


    sum_x=0;sum_y=0;


    for (x,y,w,h) in pos_hand:

        mouse.moveTo((screen[0]-x),(screen[1]-y))
        cv2.rectangle(frame, (x,y),(x+w, y+h), (255, 0, 0), 2)
        roi_gray = frame[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]




    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()






