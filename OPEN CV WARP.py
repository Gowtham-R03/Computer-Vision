# OPEN CV WARP
# to make warp perspective image to 2D

import cv2
import numpy as np
width, height = 250,350
img = cv2.imread("card3.jpg")
# get the points of card in image by paint 
#make matrix with the point
pts1 = np.float32([[492,27],[575,203],[245,142],[326,318]])
# points 2 for 2d view of warp points
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgoutput = cv2.warpPerspective(img,matrix,(width,height))
#cv2.circle(img,(pts[0][0],pts[0][1]),5,(0,0,255),cv2.FILLED)
for x in range(0,4):
    cv2.circle(img,(pts1[x][0],pts1[x][1]),5,(0,0,255),cv2.FILLED)
# img1 = np.hstack((imgoutput,imgoutput))
cv2.imshow("Cards",img)
cv2.imshow("Cards OUT",imgoutput)
# cv2.imshow("HORIZONTAL",img1)
cv2.waitKey(0)

