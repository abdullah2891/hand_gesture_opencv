import cv2
import pyautogui as mouse

__author__ = 'Abdullah_Rahman'


#your mouse will go banana don't run it yet








hand = cv2.CascadeClassifier('Hdetector.xml')
fgbg=cv2.createBackgroundSubtractorMOG2()






#cap=cv2.VideoCapture(0)
cap=cv2.VideoCapture("vtest.mp4")

screen=mouse.size()

X=[];Y=[];H=[];W=[]


while(1):

    ret, frame= cap.read()


    #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #ret,thresholded=cv2.threshold(frame,90,255,cv2.THRESH_TOZERO)
    fgmask=fgbg.apply(frame)

    pos_finger=hand.detectMultiScale(
            fgmask,
            scaleFactor=1.1,
            minNeighbors=40,
            minSize=(200, 200)
        )



    try:
        a=pos_finger[0]
        (x,y,w,h)=a
        cv2.rectangle(frame, (x, y), (x+w,y+h), (0, 255, 0), 2)

    except IndexError:
        pass




    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()






