import cv2
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans


__author__ = 'Abdullah_Rahman'


cap=cv2.VideoCapture(0)



while(1):
    ret,img=cap.read()

    c=KMeans()
    c1=KMeans(n_clusters=1)

    # Initiate STAR detector
    orb = cv2.ORB_create()


    print "Starting ORB"
    kp=orb.detect(img,None)

    kp,des=orb.compute(img,kp)

    print "FOUND KEY POINTS"


    X=[]
    for points in kp:
        X.append(points.pt)

    #print X

    print "Finding cluster centers"
    c.fit(X)

    centers= c.cluster_centers_

    print  "Finding the centroid of hand"
    centroidObj=c1.fit(centers)
    centroid=centroidObj.cluster_centers_


    (X,Y)=centroid[0]

    print "Drawing the clusters"
    for (x,y) in centers:
        cv2.rectangle(img,(int(x),int(y)),(int(x)+10,int(y)+10), (0, 255, 0),4)
        cv2.rectangle(img,(int(X),int(Y)),(int(X)+40,int(Y)+40),(0,255,0),4)

    cv2.imshow("test",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

