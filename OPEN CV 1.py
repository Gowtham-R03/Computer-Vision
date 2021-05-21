# OPEN CV 1

import cv2
import numpy as np
import stack

#kernel is matrix 
kernel = np.ones((5,5),np.uint8)
img = cv2.imread("Elon.jpg") # 0 for gray scale
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #for converting img colour
#for bluring image
img2 = cv2.GaussianBlur(img,(9,9),0) # (5,5)-kernal value by increasing it we can get more blur 0-sigma value

#edge detector
img_edgedetection = cv2.Canny(img2,100,100) #100 are thershold 1 & 2 
img_edge = cv2.Canny(img2,50,50) # if we rduce it we can lot more edges
# after geting edge of image we can do dilation and erosion with it means resizing
img_dailation = cv2.dilate(img_edgedetection ,kernel,iterations=1)
#reverse of dilation is erosion
img_erosion = cv2.erode(img_dailation,kernel,iterations=1)


#to coimbine all images in one we can use numpy library using stack fn in it
# it has vertical stack and horizontal stack, this used for display many images in same
StackedImages = stack.stackImages(([img,img_edgedetection,img_edge],[img_dailation,img_erosion,img2]),0.6)
cv2.imshow("Staked Images", StackedImages)

cv2.imshow("ELON MUSK",img)
cv2.imshow("ELON",img_edgedetection)
cv2.imshow("ELON1",img_edge)
cv2.imshow("ELON_DILATION",img_dailation) #edge line thickness is increased. By iterating more lines thick will increases
cv2.imshow("ELON_EROSION",img_erosion) 
cv2.waitKey(0)