# CV-3

import cv2

img = cv2.imread("lena.png")

print(img.shape)
imgResize = cv2.resize(img,(150,100))

imgCrop = img[0:50,40:90]
cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCrop)


cv2.waitKey(0)

