import cv2
import pyautogui as mouse
import time

__author__ = 'Abdullah_Rahman'


def smoother(l):
    return int(sum(l)/len(l))



hand = cv2.CascadeClassifier('Hdetector.xml')
fgbg=cv2.createBackgroundSubtractorMOG2()



cap=cv2.VideoCapture(0)
#cap=cv2.VideoCapture("vtest.mp4")
print cap.get(3),cap.get(4)

mouse_scale = mouse.size()
print mouse_scale

print "MANUALLY TUNED"
ScaleX = 3
ScaleY = 2

print ScaleX,ScaleY


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
            minSize=(50, 50)
        )

    if len(pos_finger)>3:                               #eliminating false positives(spot detection)
        for (x,y,w,h) in pos_finger:
            #print x,y,w,h
            X.append(ScaleX * x),Y.append(ScaleY * y),W.append(w),H.append(h)
            cv2.rectangle(frame, (x, y), (x+w,y+h), (0, 255, 0), 2)




    if(len(X)>10):
        cv2.rectangle(frame, (smoother(X), smoother(Y)), (smoother(X)+smoother(W),smoother(Y)+smoother(H)), (0, 255, 0), 2)
        mouse.moveTo(smoother(X),smoother(Y),0.2)
        X=[];Y=[];W=[];H=[]



    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()






