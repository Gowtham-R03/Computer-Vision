# OPEN CV Tutorial

import cv2

cap = cv2.VideoCapture(1)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100) #10 fro brightness
while True:
    sucess,img = cap.read()
    cv2.imshow("Video",img)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()

