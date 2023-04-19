import sys
import cv2

img = cv2.imread(sys.argv[1])
(h, w) = img.shape[:2]
specified_point = (w // 4, h // 4)

rotation_matrix = cv2.getRotationMatrix2D(specified_point, 30, 1.0)
rotated = cv2.warpAffine(img, rotation_matrix, (w, h))

cv2.imwrite(sys.argv[2], rotated)

