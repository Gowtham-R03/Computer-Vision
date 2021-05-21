# CV-5

# Color detection

import cv2
import numpy as np
import stack

def empty(a):
    pass

# trackbar which used to track color in object all over
cv2.namedWindow("Trackbars") #new window
cv2.resizeWindow("Trackbars",640,240)
cv2.createTrackbar("Hue Min","Trackbars",168,179,empty)
cv2.createTrackbar("Hue Max","Trackbars",179,179,empty)
cv2.createTrackbar("Sat Min","Trackbars",82,255,empty)
cv2.createTrackbar("Sat Max","Trackbars",255,255,empty)
cv2.createTrackbar("Value Min","Trackbars",61,255,empty)
cv2.createTrackbar("Value Max","Trackbars",255,255,empty)


while True:    
    img = cv2.imread("kod.jpg")
    img = cv2.resize(img,(256,256))
    
    imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    h_min = cv2.getTrackbarPos("Hue Min","Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max","Trackbars")
    s_min = cv2.getTrackbarPos("Sat Min","Trackbars")
    s_max = cv2.getTrackbarPos("Sat Max","Trackbars")
    v_min = cv2.getTrackbarPos("Value Min","Trackbars")
    v_max = cv2.getTrackbarPos("Value Max","Trackbars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHsv,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)
    sImages = stack.stackImages(([img,imgHsv],[mask,imgResult]),0.3)
    # cv2.imshow("Images",img)
    # cv2.imshow("Image HSV",imgHsv)
    # cv2.imshow("Mask",mask)
    cv2.imshow("Stacked",sImages)
    cv2.waitKey(1)

