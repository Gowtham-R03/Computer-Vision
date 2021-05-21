# OPEN CV SHAPE DETECTION
# outline of something ex:object

import cv2
import numpy as np
import stack

frame_width = 640
frame_height = 360
cap = cv2.VideoCapture(0)
cap.set(3,frame_width)
cap.set(4,frame_height)

def empty(a):
    pass

# trackbar which used to track color in object all over
cv2.namedWindow("Parameters") #new window
cv2.resizeWindow("Parameters",640,240)
cv2.createTrackbar("Thershold1","Parameters",150,255,empty)
cv2.createTrackbar("Thershold2","Parameters",255,255,empty)
cv2.createTrackbar("Area","Parameters",5000,30000,empty)

def getContours(video,videoContour):
    contours, hierarchy = cv2.findContours(video, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # retrevel method - external :Retrives only outer extreme contours
    # retrevel - Tree : Retreves and constructs fully
    
    for cnt in contours: #to reduce noise this loop wil be helpful
        area = cv2.contourArea(cnt)
        areamin = cv2.getTrackbarPos("Area","Parameters") # this for to classify object with areas
        if area > areamin:
            cv2.drawContours(videoContour, contours,-1, (255,0,255), 7) # 7width of boundary
            # to get corner points of our shape object
            para = cv2.arcLength(cnt,True) # true for closed contours
            # to approximate the points to get what shape is this
            approx = cv2.approxPolyDP(cnt,0.02*para,True) #0.02*para = resolution
            print(len(approx)) # here we get ex:4 it indicates it is square or rectangle
            # create bounding box over a getten shape
            x,y,w,h = cv2.boundingRect(approx)
            cv2.rectangle(videoContour, (x,y),(x+w,y+h), (0,255,0),5)
            #to get text on the contour image
            cv2.putText(videoContour,"Points: " + str(len(approx)), (x+w+20,y+h+20), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,0,255),3)
            cv2.putText(videoContour,"Area: " + str(int(area)), (x+w+20,y+h+20), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,0,255),3)
        
    
    
    
while True:
    sucess,video = cap.read()
    videoContour = video.copy()
    videoblur = cv2.GaussianBlur(video,(7,7),1)
    videogray = cv2.cvtColor(videoblur,cv2.COLOR_BGR2GRAY)
    
    thershold1 = cv2.getTrackbarPos("Thershold1","Parameters")
    thershold2 = cv2.getTrackbarPos("Thershold2","Parameters")
    videoCanny = cv2.Canny(videogray,thershold1,thershold2) # remove noise in contour we need to dilation
    kernel = np.ones((5,5))
    videodil = cv2.dilate(videoCanny,kernel,iterations = 1)
    getContours(videodil, videoContour)
    videostack = stack.stackImages(([video,videogray,videoCanny],[videodil,videoContour,videoContour]),0.3)
    
    
    
    cv2.imshow("WEBCAM",videostack)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
 
