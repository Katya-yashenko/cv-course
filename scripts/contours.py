import sys
import cv2

img = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
_, thresholded = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

contour_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 2)

cv2.imwrite(sys.argv[2], contour_img)

