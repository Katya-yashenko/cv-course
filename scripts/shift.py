import sys
import cv2
import numpy as np

img = cv2.imread(sys.argv[1])
(h, w) = img.shape[:2]

translation_matrix = np.float32([[1, 0, 10], [0, 1, 0]])
shifted = cv2.warpAffine(img, translation_matrix, (w, h))

cv2.imwrite(sys.argv[2], shifted)

