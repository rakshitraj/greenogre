import cv2

###############################
frameWidth = 640
frameHeight = 480
plateCascade = cv2.CascadeClassifier("/home/raxit/anaconda3/share/opencv4/haarcascades/haarcascade_russian_plate_number.xml")
color = (255,0,0)
count = 0
###############################
cap = cv2.VideoCapture(2)
cap.set(3, frameWidth)  # set width
cap.set(4, frameHeight) # set height
cap.set(10, 20) # set brightness
while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    numberPlates = plateCascade.detectMultiScale(imgGray, 1.1, 4)
    for(x,y,w,h) in numberPlates:
        area = w*h
        if area > 500 : # area threshold
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(img, "Plate", (x, y-5),
                        cv2.FONT_HERSHEY_COMPLEX, 1, color, 2)
            imgROI = img[y:y+h, x:x+w]
            cv2.imshow("ROI", imgROI)
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('res/scanned/NoPlate_'+str(count)+".jpg", imgROI)
        cv2.rectangle(img, (0,200), (640,300), (0, 255,0), cv2.FILLED)
        cv2.putText(img, "Scan Saved", (150,255),
                    cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,0), 2)
        cv2.imshow("Result", img)
        cv2.waitKey(500)
        count += 1