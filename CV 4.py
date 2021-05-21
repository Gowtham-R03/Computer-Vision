# CV-4

import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)

# print(img.shape)
# img[:] = 255,0,0

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),2)
cv2.rectangle(img,(100,100),(400,450),(255,0,0),2)
cv2.circle(img,(300,80),40,(0,255,255),cv2.FILLED)
cv2.putText(img,"KOD",(300,500),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,255,0),2)

cv2.imshow("Image",img)
cv2.waitKey(0)
