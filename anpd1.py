import cv2

###############################
frameWidth = 640
frameHeight = 480
nPlateCascade = cv2.CascadeClassifier("")
###############################
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)  # set width
cap.set(4, frameHeight) # set height
cap.set(10, 100) # set brightness
while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break