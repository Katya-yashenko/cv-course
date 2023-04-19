import cv2
import sys

img = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
laplacian = cv2.Laplacian(img, cv2.CV_64F)

# Convert the Laplacian result back to uint8 and normalize the values
laplacian_normalized = cv2.normalize(laplacian, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

cv2.imwrite(sys.argv[2], laplacian_normalized)

