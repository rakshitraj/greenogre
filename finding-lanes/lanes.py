import cv2
import numpy as np
import matplotlib.pyplot as plt

def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    edge = cv2.Canny(blur, 50, 150)
    return edge

def region_of_interest(image):
    height = image.shape[0]
    triangle = np.array([(200, height), (1100, height), (500, 250)])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, triangle, 255)
    return mask


# Read the image
image = cv2.imread('test_image.jpg')
cpy_image = np.copy(image)
# cv2.imshow('image', image)

# Canny edge detection
canny = canny(cpy_image)
# cv2.imshow('Edges', canny)

# Region of interest  #
# ------------------- #
plt.imshow(canny)
plt.show()

# cv2.waitKey(0)