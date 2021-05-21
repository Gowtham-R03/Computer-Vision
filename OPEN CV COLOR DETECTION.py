# COLOR DERECTION 
# HSV - HUE saturation value used better than BGR and RGB
# from hsv we can detect which color we want
import cv2
import numpy as np

frame_width = 640
frame_height = 480
cap = cv2.VideoCapture(0)
cap.set(3,frame_width)
cap.set(4,frame_height)

def empty(a):
    pass

# trackbar which used to track color in object all over
cv2.namedWindow("HSV") #new window
cv2.resizeWindow("HSV",640,240)
cv2.createTrackbar("HUE MIN","HSV",0,179,empty)
cv2.createTrackbar("HUE MAX","HSV",179,179,empty)
cv2.createTrackbar("SAT MIN","HSV",0,255,empty)
cv2.createTrackbar("SAT MAX","HSV",255,255,empty)
cv2.createTrackbar("VALUE MIN","HSV",0,255,empty)
cv2.createTrackbar("VALUE MAX","HSV",255,255,empty)


while True:
    _, video = cap.read()
    hsv = cv2.cvtColor(video,cv2.COLOR_BGR2HSV)
    
    h_min = cv2.getTrackbarPos("HUE MIN","HSV") #getting pos for color detect
    h_max = cv2.getTrackbarPos("HUE MAX","HSV")
    s_min = cv2.getTrackbarPos("SAT MIN","HSV")
    s_max = cv2.getTrackbarPos("SAT MAX","HSV")
    v_min = cv2.getTrackbarPos("VALUE MIN","HSV")
    v_max = cv2.getTrackbarPos("VALUE MAX","HSV")
    
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(hsv,lower,upper)
    result = cv2.bitwise_and(video,video, mask = mask)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hstack = np.hstack([video,mask,result])
    
    # cv2.imshow("WEBCAM",video)
    # cv2.imshow("WEBCAM hsv",hsv)
    # cv2.imshow("MASK",mask)
    # cv2.imshow("RESULT",result)
    cv2.imshow("Horizontal Stack",hstack)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
