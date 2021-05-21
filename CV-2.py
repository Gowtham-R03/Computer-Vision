# CV-2
# Basic Functions

import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)

img = cv2.imread('man.jpg')

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

imgBlur = cv2.GaussianBlur(img,(5,5),0)

imgEdge = cv2.Canny(img,200,200)
imgDialation = cv2.dilate(imgEdge,kernel,iterations = 1)
imgErosion = cv2.erode(imgDialation,kernel,iterations = 1)

cv2.imshow("GrayImage",imgGray)
cv2.imshow("BlurImage",imgBlur)
cv2.imshow("EdgeImage",imgEdge)
cv2.imshow("DialtedImage",imgDialation)
cv2.imshow("ErosionImage",imgErosion)

cv2.waitKey(0)
cv2.destroyAllWindows()