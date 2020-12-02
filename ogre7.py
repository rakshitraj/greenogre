# Joining images
import cv2
import numpy as np
img = cv2.imread('res/lena.jpg')

# Both images have to have the same number of channels
# Horizontal Stacking
imgHor = np.hstack((img,img))
# Vertical Stack
imgVer = np.vstack((img,img))

cv2.imshow("Horizontal Stack", imgHor)
cv2.imshow("Vertical Stack", imgVer)
cv2.imshow("Img", img)
cv2.waitKey(0)