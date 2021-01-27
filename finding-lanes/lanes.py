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
    # Region of interest is a polygon - triangle
    polygons = np.array([
        [(200, height), (1100, height), (500, 250)]
    ])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    roi = cv2.bitwise_and(image, mask)
    return roi

def display_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None: # checking if any lines were detected at all
        for line in lines:
            print(line)


# Read the image
image = cv2.imread('test_image.jpg')
# Create copy
cpy_image = np.copy(image)
# Canny edge detection
canny = canny(cpy_image)
# Region of interest  #
roi = region_of_interest(canny)
# Finding straight lines in image using Hough Transform
lines = cv2.HoughLinesP(roi, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)
line_image = display_lines(cpy_image, lines)

cv2.imshow('Result', roi)
cv2.waitKey(0)