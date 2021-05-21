# OPEN CV STACK OF MANY IMAGES IN ONE DIAPLAY

import cv2
import numpy as np
import stack

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)



while True:
    success, img = cap.read()
    kernel = np.ones((5,5),np.uint8)
    print(kernel)
    #path = "Resources/lena.png"
    #img =  cv2.imread(path)
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
    imgCanny = cv2.Canny(imgBlur,100,200)
    imgDilation = cv2.dilate(imgCanny,kernel , iterations = 2)
    imgEroded = cv2.erode(imgDilation,kernel,iterations=2)

#     #imgBlank = np.zeros((200,200),np.uint8)
    StackedImages = stack.stackImages(0.3,([img,imgGray,imgBlur],
                                   [imgCanny,imgDilation,imgEroded]))
    cv2.imshow("Staked Images", StackedImages)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

################### Stacking images  ################
# import cv2
# import numpy as np
# import stack

# #kernel is matrix 
# kernel = np.ones((5,5),np.uint8)
# img = cv2.imread("Elon.jpg") # 0 for gray scale
# img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #for converting img colour
# #for bluring image
# img2 = cv2.GaussianBlur(img,(9,9),0) # (5,5)-kernal value by increasing it we can get more blur 0-sigma value

# #edge detector
# img_edgedetection = cv2.Canny(img2,100,100) #100 are thershold 1 & 2 
# img_edge = cv2.Canny(img2,50,50) # if we rduce it we can lot more edges
# # after geting edge of image we can do dilation and erosion with it means resizing
# img_dailation = cv2.dilate(img_edgedetection ,kernel,iterations=1)
# #reverse of dilation is erosion
# img_erosion = cv2.erode(img_dailation,kernel,iterations=1)


# #to coimbine all images in one we can use numpy library using stack fn in it
# # it has vertical stack and horizontal stack, this used for display many images in same
# StackedImages = stack.stackImages(([img,img_edgedetection,img_edge],[img_dailation,img_erosion,img2]),0.6)
# cv2.imshow("Staked Images", StackedImages)
# cv2.waitKey(0)




################### Stacking images without Function ################
# import cv2
# import numpy as np
# img1 = cv2.imread('../Resources/lena.png',0)
# img2 = cv2.imread('../Resources/land.jpg')
# print(img1.shape)
# print(img2.shape)
# img1 = cv2.resize(img1, (0, 0), None, 0.5, 0.5)
# img2 = cv2.resize(img2, (0, 0), None, 0.5, 0.5)
# img1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)
# hor= np.hstack((img1, img2))
# ver = np.vstack((img1, img2))
# cv2.imshow('Vertical', ver)
# cv2.imshow('Horizontal', hor)
# cv2.waitKey(0)