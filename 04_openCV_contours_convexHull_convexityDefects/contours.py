import cv2

img = cv2.imread("C:\\Users\\Selman\\Desktop\\Tasarim-1\\contour1.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_,thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours ,_ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# Defining _ is because that value will not be used, cv2.RETR_TREE and cv2.CHAIN ​​are used to make the contour finding process more accurate.

print(contours) #gave a pretty long list of coordinates

# Now we need to draw these contours

cv2.drawContours(img, contours, -1, (0,0,255), 3)
# Which image will be processed, coordinates are kept in contours, colors and thickness

cv2.imshow("Contour", img)
cv2.waitKey(0)
cv2.destroyAllWindows()