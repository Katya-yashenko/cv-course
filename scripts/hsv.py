import sys
import cv2

img = cv2.imread(sys.argv[1])
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imwrite(sys.argv[2], hsv)

