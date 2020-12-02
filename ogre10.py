# Detecting Faces - Viola Jones
# Using built-in cascade
import cv2

faceCascade = cv2.CascadeClassifier('/home/raxit/anaconda3/share/opencv4/haarcascades/haarcascade_frontalface_default.xml')
img = cv2.imread('res/lena.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y), (x+w, y+h), (0, 255,0), 2)

cv2.imshow("img", img)
cv2.waitKey(0)
