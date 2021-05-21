# OPEN CV Detecting click on image
# warp percpective to bird perpespective

import cv2
import numpy as np

circles = np.zeros([4,2],np.int) # 4-rows 2-columns 
counter = 0


def Mousepoints(events,x,y,flags,parameters):
    global counter
    if events == cv2.EVENT_LBUTTONDOWN:
        # print(x,y)
        circles[counter] = x,y #while click counter will take x,y vcalue and is stored in circle matrix
        counter = counter + 1
        print(circles)


img = cv2.imread("cup.jpg")
while True:
    
    if counter == 4:
        
        width, height = 250,350
        # get the points of card in image by paint 
        #make matrix with the point
        pts1 = np.float32([circles[0],circles[1],circles[2],circles[3]])
        # points 2 for 2d view of warp points
        pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
        matrix = cv2.getPerspectiveTransform(pts1,pts2)
        imgoutput = cv2.warpPerspective(img,matrix,(width,height))        
        cv2.imshow("Cards OUT",imgoutput)
        
    for x in range(0,4):
            cv2.circle(img,(circles[x][0],circles[x][1]),3,(0,0,255),cv2.FILLED)
    
    cv2.imshow("Original Image",img)
    cv2.setMouseCallback("Original Image",Mousepoints)

    cv2.waitKey(1)