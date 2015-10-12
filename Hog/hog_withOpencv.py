import numpy as np
import cv2
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans



img = cv2.imread('test.jpg',0)


c=KMeans()
c1=KMeans(n_clusters=1)

# Initiate STAR detector
orb = cv2.ORB_create()



kp=orb.detect(img,None)

X=[]
for points in kp:
    X.append(points.pt)

print X

print "Finding cluster centers"
c.fit(X)

centers= c.cluster_centers_

print  "Finding the centroid of hand"
centroidObj=c1.fit(centers)


centroid=centroidObj.cluster_centers_

(X,Y)=centroid[0]


kp,des=orb.compute(img,kp)

print "Drawing the clusters"
for (x,y) in centers:
    cv2.rectangle(img,(int(x),int(y)),(int(x)+10,int(y)+10), (0, 255, 0),4)
    cv2.rectangle(img,(int(X),int(Y)),(int(X)+40,int(Y)+40),(0,255,0),4)

#output=cv2.drawKeypoints(img,kp,None,color=(0,255,0), flags=0)

plt.imshow(img)
plt.show()
