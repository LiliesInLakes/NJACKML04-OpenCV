import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype = 'uint8')

cv.imshow("Blank image", blank)
blank[200:300, 100:300]=1, 255, 100

cv.imshow("Rectangle image", blank)
cv.waitKey(0)
