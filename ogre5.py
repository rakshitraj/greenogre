import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
print(img.shape)

# color image
# img[100:300, 200:300] = 0,0,255

# lines
cv2.line(img,(0,0), (img.shape[1],img.shape[0]), (0,255,0), 3)
# rectangle
cv2.rectangle(img, (0,0), (250,350), (0,0,255), 2)
# circle
cv2.circle(img, (450,50), 30, (255,0,0), 5)
# text
cv2.putText(img, " OPENCV ", (300, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)


cv2.imshow("Img", img)
cv2.waitKey(0)