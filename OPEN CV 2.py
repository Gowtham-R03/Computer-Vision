# OPEN CV 2

import cv2

img = cv2.imread("city1.jpg")
img.shape
#resize image (height,width)
height = 100
width = 200
img1 = cv2.resize(img,(width,height))
img1.shape
# crop
img2 = img[50:183,:] #(height,width) we can plot it for reduce confusion
#cropping resized image
img3 = cv2.resize(img2,(img.shape[1],img.shape[0])) #1 for width,0 for height

cv2.imshow("CITY",img)
cv2.imshow("RESIZE",img1)
cv2.imshow("CROP",img2)
cv2.imshow("RCROP",img3)
cv2.waitKey(0)
