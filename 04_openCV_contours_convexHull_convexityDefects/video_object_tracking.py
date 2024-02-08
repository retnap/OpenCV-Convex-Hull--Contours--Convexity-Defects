import cv2 
import numpy as np 

cap = cv2.VideoCapture("C:\\Users\\Selman\\Desktop\\Tasarim-1\\dog.mp4")

while(1):
    _, frame = cap.read()
    # _ a definition made to avoid errors, it throws the resulting 1s and 0s there

    #We cannot detect objects as rgb or bgr, so we will convert it to hsv.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #In the video, the white object will be tracked, find the white code range of HSV on Google.
    sensitivity = 15
    lower_white = np.array([0,0,255 - sensitivity])
    upper_white = np.array([255,sensitivity,255])

    mask = cv2.inRange(hsv, lower_white, upper_white)
    #Apply mask to the parts between lower_white and upper_white and delete the rest

    res = cv2.bitwise_and(frame, frame, mask = mask)
    #The reason why frame and mask are written twice is for special use.

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    
cv2.destroyAllWindows()
