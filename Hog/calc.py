import numpy as np


__author__ = 'Abdullah_Rahman'



class calc:
    def __init__(self):
        pass


    def angle_descriptor(self,local_clusters,global_cluster):
        R=[]
        Angles=[]
        if len(global_cluster)==1:
            (X,Y)=global_cluster[0]
            for (x,y) in local_clusters:
                R.append((X-x,Y-y))

            for i in range(0,len(R)-1):

                V1=R[i]
                V2=R[i+1]
                Angles.append(np.dot(V1,V2))





            return Angles

        else:
            print "global cluster can't be greater than 1 "
            return -1




A=[[8 ,5]]

B=[(1,2),(5,6),(3,4),(10,29),(20,2)]


test_calculation=calc()

print test_calculation.angle_descriptor(B,A)
