import cv2

__author__ = 'Abdullah_Rahman'


hog=cv2.HOGDescriptor()
img=cv2.imread("test.jpg")

h=hog.compute(img)

print h,len(h)