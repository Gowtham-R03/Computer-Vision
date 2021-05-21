# OPEN CV CV- computer vision
import cv2

img = cv2.imread("Elon.jpg")

cv2.imshow("ELON",img)
#for window to wait 
cv2.waitKey(0) 

# for video and webcam display it is different from image reading
# for video and cam we need loop for keep on running that showing each frame of video
cap = cv2.VideoCapture(0) # incase of zero we can give our videos

# we can give parameters for video capyuring
frame_width = 640
frame_height = 480 # we should give parameter which our default camera accepts

#we can set it in capture of video
cap.set(3,frame_width) # 3 for width which opencv default number for width
cap.set(4,frame_height) # 4  opencv default number for height

while True:
    sucess,video = cap.read() #from cap it will reada nd stores in video if this condition sucess is true if not false
    cv2.imshow("WEBCAM",video)
    
    if cv2.waitKey(1) & 0xff == ord('q'): # if i press q it will break from loop
        break
# in web camera we cant resize it resolution but in our video we can do it
import cv2
cap = cv2.VideoCapture("kod.mp4")
frame_width = 1080
frame_height = 2400

while True:
    sucess,video = cap.read()
    #resize video
    video = cv2.resize(video,(frame_width,frame_height))
    cv2.imshow("KOD",video) 
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
# ctrl + / to make the number of line as comments