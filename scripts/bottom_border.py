import sys
import cv2

img = cv2.imread(sys.argv[1])
flipped = cv2.flip(img, 0)

cv2.imwrite(sys.argv[2], flipped)

