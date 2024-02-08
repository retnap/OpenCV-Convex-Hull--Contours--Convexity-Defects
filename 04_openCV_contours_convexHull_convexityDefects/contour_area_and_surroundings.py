import cv2 

img = cv2.imread("C:\\Users\\Selman\\Desktop\\Tasarim-1\\contour.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0] # We reached the first value of M

area = cv2.contourArea(cnt) # found the area of ​​the triangle
print(area)

M = cv2.moments(cnt)  # found the area of ​​the triangle again
print(M["m00"])

perimeter = cv2.arcLength(cnt, True) # found the perimeter of the triangle
print(perimeter)


cv2.imshow("Original", img)
cv2.imshow("Gray", gray)
cv2.imshow("Thresh", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()