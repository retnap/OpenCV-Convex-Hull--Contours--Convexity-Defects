# We want to create a convex pattern

import cv2 
import numpy as np 

img = cv2.imread("C:\\Users\\Selman\\Desktop\\Tasarim-1\\map.jpg")

#We will convert the image we have into binary (black and white).
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.blur(gray,(3,3))
ret, thresh = cv2.threshold(blur, 40, 255, cv2.THRESH_BINARY)
  #Some parts of the African continent are completely threshed so lower the min value

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# We found the contours and store them in the contours variable

hull = []

for i in range(len(contours)): #will return the length of the stroke
    hull.append(cv2.convexHull(contours[i], False)) # Since we set the i value of the contour to False, whatever it is,
        # Convex Hull will return its index
        #hull.append will put each value into the hull[] above

bg = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)
# We created a black background 

for i in range(len(contours)):
    cv2.drawContours(bg, contours, i, (255,0,0), 3, 8, hierarchy)
    cv2.drawContours(bg, hull, i, (0,255,0), 1, 8)

cv2.imshow("Image", bg)


# cv2.imshow("original", img)
# cv2.imshow("gray", gray)
# cv2.imshow("blur", blur)
# cv2.imshow("thresh", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()