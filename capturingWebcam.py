import numpy as np
import cv2

__author__ = 'Abdullah_Rahman'


cap = cv2.VideoCapture(0)



while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    gray=np.float32(gray)
    dst=cv2.cornerHarris(gray,2,3,0.04)
    dst=cv2.dilate(dst,None)
    frame[dst>0.001*dst.max()]=[0,0,255]
    print dst


    # Display the resulting frame

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


