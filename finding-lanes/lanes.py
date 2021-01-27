import cv2
import numpy as np

def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    edge = cv2.Canny(blur, 50, 150)
    return edge

# Read the image
image = cv2.imread('test_image.jpg')
cpy_image = image
cv2.imshow('image', image)

# Canny edge detection
canny = canny(cpy_image)
cv2.imshow('Edges', canny)

cv2.waitKey(0)