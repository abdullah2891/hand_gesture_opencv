import numpy as np
import cv2

__author__ = 'Abdullah_Rahman'


cap = cv2.VideoCapture(0)

trainer=cv2.imread('hand6.jpg',0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here


    orb=cv2.ORB_create()

    kp1, des1=orb.detectAndCompute(frame,None)
    kp2, des2=orb.detectAndCompute(trainer,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1, des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    img3 = cv2.drawMatches(frame,kp1,trainer,kp2,matches[:5],outImg=None)

    # Display the resulting frame

    cv2.imshow('frame',img3)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


