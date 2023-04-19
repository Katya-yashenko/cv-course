import sys
import cv2
import numpy as np

img = cv2.imread(sys.argv[1])
gamma = 1.5

lookup_table = np.array([((i / 255.0) ** gamma) * 255 for i in np.arange(0, 256)]).astype('uint8')
gamma_corrected = cv2.LUT(img, lookup_table)

cv2.imwrite(sys.argv[2], gamma_corrected)

