import cv2
import numpy as np
import matplotlib.pyplot as plt

def make_coordinates(image, line_parameters):
    scale_factor = (1/2) # ideally use 3/5, scales line to 3/5th height of image
    slope, intercept = line_parameters
    # try:
    #     slope, intercept = line_parameters
    # except TypeError:
    #     slope, intercept = 1, 0
    y1 = image.shape[0]
    y2 = int(y1*scale_factor)
    x1 = int((y1 - intercept)/slope)
    x2 = int((y2 - intercept) / slope)
    return np.array([x1,y1, x2, y2])

def average_slope_intercept(image, lines):
    left_fit = []
    right_fit = []
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        parameters = np.polyfit((x1, x2), (y1, y2), 1)
        slope = parameters[0]
        intercept = parameters[1]
        if slope < 0:
            left_fit.append((slope, intercept))
        else:
            right_fit.append((slope, intercept))
    left_fit_avg = np.average(left_fit, axis=0)
    right_fit_avg = np.average(right_fit, axis=0)
    left_line = make_coordinates(image, left_fit_avg)
    right_line = make_coordinates(image, right_fit_avg)
    return np.array([left_line, right_line])


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
        for x1, y1, x2, y2 in lines:
            # x1, y1, x2, y2= line.reshape(4)
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)
    return line_image


image_array = []
h,w = 0, 0
cap = cv2.VideoCapture("test2.mp4")
while(cap.isOpened()):
    _, frame = cap.read()
    h,w,_ = frame.shape
    # Canny edge detection
    canny_img = canny(frame)
    # Region of interest  #
    roi = region_of_interest(canny_img)
    # Finding straight lines in image using Hough Transform
    lines = cv2.HoughLinesP(roi, 1, np.pi / 360, 100, np.array([]), minLineLength=40, maxLineGap=5)

    # Optimization
    averaged_lines = average_slope_intercept(frame, lines)

    line_image = display_lines(frame, averaged_lines)

    # overlay lines over original image
    combined_image = cv2.addWeighted(frame, 0.8, line_image, 1, 0)
    image_array.append(combined_image)
    cv2.imshow('Result', combined_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):# masking with 0xFF to ensure cross platlorm performance
        break
cap.release()

#out = cv2.VideoWriter('project.mp4', cv2.VideoWriter_fourcc(*'XVID'), 15, (h,w))
# fourcc = cv2.cv.CV_FOURCC(*'XVID')
# out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
out = cv2.VideoWriter('project.avi',
                cv2.VideoWriter_fourcc(*'MJPG'),
                10, (h,w))
for i in range(len(image_array)):
    out.write(image_array[i])
out.release()

cv2.destroyAllWindows()