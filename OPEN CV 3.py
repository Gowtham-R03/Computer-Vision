# OPEN CV 3

import cv2
import numpy as np
import matplotlib.pyplot as plt

# creating a sample image
img  = np.zeros((512,512,3),np.uint8) # 3 for color channels

#img[:] = 255,0,0 #BGR

#for drawing line
cv2.line(img,(0,200),(400,400),(0,0,255),2)
#to get whole line in image
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),2)
# to form rectangle
cv2.rectangle(img,(350,100),(450,200),(0,0,255),cv2.FILLED)
#to get full color in rect for thickness we need to give cv2.FILLED

# to get circle
cv2.circle(img,(150,400),50,(255,0,0),3)

#to get text in image
cv2.putText(img,"Shapes",(200,50),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,180),3)

cv2.imshow("IMAGE",img)
cv2.waitKey(0)
