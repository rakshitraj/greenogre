# WARP PERSPECTIVE
# warp perspective on an image to get the birds eye view

import cv2
import numpy as np

img = cv2.imread('res/cards.jpg')

width, height = 250,350
pts1 = np.float32([[345,151],[459,209],[365,394],[251,334]])
pts2 = np.float32([[0,0],[width,0],[width,height],[0,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width,height))

cv2.imshow("Image", img)
cv2.imshow("Output", imgOutput)
cv2.waitKey(0)