import cv2
import numpy as np

# images = []
# paths = ['res/cars/Cars1.png',
#          'res/cars/Cars2.png',
#          'res/cars/Cars3.png',
#          'res/cars/Cars4.png',
#          'res/cars/Cars5.png']
#
# for path in paths:

img = cv2.imread('res/cars/Cars2.png')

kernel = np.ones((5, 5), np.uint8)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7, 7), 0)
imgCanny = cv2.Canny(gray, 150, 200)
# make edges thicker
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
# make edges thinner
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

cv2.imshow("Lena", img)
cv2.imshow("Gray Image", gray)
cv2.imshow("Blur", blur)
cv2.imshow("Canny", imgCanny)
cv2.imshow("Img Dilation", imgDilation)
cv2.imshow("Img Erosion", imgEroded)
cv2.waitKey(0)