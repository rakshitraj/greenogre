import cv2
import numpy as np
import glob
import os

# Function to stack images
def stackImages(self, scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver

plateCascade = cv2.CascadeClassifier("/home/raxit/anaconda3/share/opencv4/haarcascades/haarcascade_russian_plate_number.xml")
images = [cv2.imread(file) for file in glob.glob("/home/raxit/shrek/res/cars/*.png")]
count = 0

# path = glob.glob("/home/raxit/shrek/res/cars/*.jpg")
# cv_img = []
# for img in path:
#     n = cv.imread(img)
#     cv_img.append(n)

for img in images:
    kernel = np.ones((5, 5), np.uint8)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7, 7), 0)
    imgCanny = cv2.Canny(gray, 150, 200)

    imgStack = stackImages(1,[img, gray])#, [blur, imgCanny]]))
    cv2.imwrite('/home/raxit/shrek/res/out/prep_cars' + str(count) + ".jpg", imgStack)

# Detection
    
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    numberPlates = plateCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in numberPlates:
        area = w * h
        if area > 500:  # area threshold
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "Plate", (x, y - 5),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,255), 2)
            imgROI = img[y:y + h, x:x + w]
            #cv2.imshow("ROI", imgROI)
    cv2.imwrite('/home/raxit/shrek/res/out/out_' + str(count) + ".jpg", img)
    cv2.imwrite('/home/raxit/shrek/res/out/NoPlate_' + str(count) + ".jpg", imgROI)
    count+=1