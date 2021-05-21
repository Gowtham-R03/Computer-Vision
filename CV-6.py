# CV-6

# Shape Detection

import cv2
import numpy as np
import stack

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # retrevel method - external :Retrives only outer extreme contours
    # retrevel - Tree : Retreves and constructs fully
    
    for cnt in contours: #to reduce noise this loop wil be helpful
        area = cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(imgContour, cnt,-1, (255,0,255), 2) # 7width of boundary
            # to get corner points of our shape object
            para = cv2.arcLength(cnt,True) # true for closed contours
            # to approximate the points to get what shape is this
            approx = cv2.approxPolyDP(cnt,0.02*para,True) #0.02*para = resolution
            print(len(approx)) # here we get ex:4 it indicates it is square or rectangle
            objCor = len(approx)
            # create bounding box over a getten shape
            x,y,w,h = cv2.boundingRect(approx)
            
            if objCor == 3: objectType = "Tri"
            elif objCor == 4:
                aspRatio = w/float(h)
                if aspRatio > 0.80 and aspRatio < 1.25: objectType ="Sqr"
                else:objectType = "Rect"
            elif objCor > 4: objectType = "Circle"
            else: objectType = "None"
            
            cv2.rectangle(imgContour, (x,y),(x+w,y+h), (0,255,0),2)
            cv2.putText(imgContour, objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,0,255),2)
            

img = cv2.imread('shapes.jpg')
img = cv2.resize(img,(400,400))
imgContour = img.copy()
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgEdge = cv2.Canny(imgGray,100,100)
getContours(imgEdge)
imgStack = stack.stackImages(([img,imgGray,imgContour],[imgBlur,imgEdge,img]),0.3)

cv2.imshow("Images",imgStack)
cv2.waitKey(0)

