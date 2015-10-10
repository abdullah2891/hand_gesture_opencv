import cv2
import pyautogui as mouse
import math

__author__ = 'Abdullah_Rahman'


#your mouse will go banana don't run it yet








hand = cv2.CascadeClassifier('Hand.Cascade.1.xml')
fgbg=cv2.createBackgroundSubtractorMOG2()






#cap=cv2.VideoCapture(0)
cap=cv2.VideoCapture("vtest.mp4")
print cap.get(5)

screen=mouse.size()

X=[];Y=[];H=[];W=[]


while(1):

    ret, frame= cap.read()


    #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #ret,thresholded=cv2.threshold(frame,90,255,cv2.THRESH_TOZERO)
    fgmask=fgbg.apply(frame)

    pos_hand=hand.detectMultiScale(
            fgmask,
            scaleFactor=1.1,
            minNeighbors=8,
            minSize=(100, 100)
        )


    try:
        a=pos_hand[0]
        x=a[0];y=a[1];w=a[0]+a[2];h=a[1]+a[3]
        cv2.rectangle(frame, (x, y), (w,h), (0, 255, 0), 2)
        #print x,y,w,h
    except IndexError:
        pass


    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()






