# CV-8

# VIRTUAL PAINT

import cv2
import numpy as np

cap = cv2.VideoCapture(1)
cap.set(3,640)
cap.set(4,480)
cap.set(10,150) #10 fro brightness


myColor = [[68,39,0,112,255,255],
           [14,33,0,128,255,255],
           [112,19,0,142,255,255]]

myColorValues =[[255,178,102],        #BGR
               [0,255,255],
               [102,0,51]]

myPoints = []

def findColor(img,myColor,myColorValues):
    imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count = 0
    newPoints=[]
    for color in myColor:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHsv,lower,upper)
        x,y=getContours(mask)
        cv2.circle(imgContour,(x,y),10,myColorValues[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count +=1
        #cv2.imshow(str(color[0]),mask)
    return newPoints

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # retrevel method - external :Retrives only outer extreme contours
    # retrevel - Tree : Retreves and constructs fully
    x,y,w,h = 0,0,0,0
    for cnt in contours: #to reduce noise this loop wil be helpful
        area = cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(imgContour, cnt,-1, (255,0,255), 2) # 7width of boundary
            # to get corner points of our shape object
            para = cv2.arcLength(cnt,True) # true for closed contours
            # to approximate the points to get what shape is this
            approx = cv2.approxPolyDP(cnt,0.02*para,True) #0.02*para = resolution
            # create bounding box over a getten shape
            x,y,w,h = cv2.boundingRect(approx)
    return x+w//2,y

def drawOnCanvas(myPoints,myColorValues):
    for point in myPoints:
        cv2.circle(imgContour, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)


while True:
    sucess,img = cap.read()
    imgContour = img.copy()
    newPoints = findColor(img, myColor,myColorValues)
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints,myColorValues)
 
    cv2.imshow("Video",imgContour)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()