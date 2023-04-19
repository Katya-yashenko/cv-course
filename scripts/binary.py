import sys
import cv2

img = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
_, thresholded = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

cv2.imwrite(sys.argv[2], thresholded)

