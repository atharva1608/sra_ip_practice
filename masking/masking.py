import numpy as np
import cv2
import matplotlib.pyplot as plt
img=cv2.imread('mask.jpg')
hsvframe=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
blue_lower=np.array([94,80,2],np.uint8)
blue_upper=np.array([120,255,255],np.uint8)
blue_mask=cv2.inRange(hsvframe,blue_lower,blue_upper)

kernel=np.ones((5,5),"uint8")
blue_mask=cv2.dilate(blue_mask,kernel)
res_blue = cv2.bitwise_and(img,img,mask=blue_mask)

cv2.imshow("input_image",img)
cv2.imshow("final_image",res_blue)

cv2.waitKey()

