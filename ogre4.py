import cv2
import numpy as np

img = cv2.imread("res/lambo.jpg")
print(img.shape) # (height, width, number of channels)

imgResize = cv2.resize(img, (300, 300))
print(imgResize.shape)

# Crop image
## opencv convention    --> (width, height)
## matrix/np convention --> (height, width)
imgCropped = img[100:300, 200:500]

cv2.imshow("Image", img)
cv2.imshow("Image Resizes", imgResize)
cv2.imshow("Image Crop", imgCropped)
cv2.waitKey(0)