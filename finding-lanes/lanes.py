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
            #line = line.reshape(4)
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)
            return line_image

# Read the image
image = cv2.imread('test_image.jpg')
# Create copy
cpy_image = np.copy(image)
# Canny edge detection
canny_img = canny(cpy_image)
# Region of interest  #
roi = region_of_interest(canny_img)
# Finding straight lines in image using Hough Transform
lines = cv2.HoughLinesP(roi, 1, np.pi/360, 100, np.array([]), minLineLength=40, maxLineGap=5)
line_image = display_lines(cpy_image, lines)

# overlay lines over original image
combined_image = cv2.addWeighted(cpy_image,0.8, line_image, 1, 0)
cv2.imshow('Result', combined_image)
cv2.waitKey(0)