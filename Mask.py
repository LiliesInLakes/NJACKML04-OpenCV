import cv2 as cv
import numpy as np

img= cv.imread('/Users/avni/Downloads/sea.jpg')
camera= cv.VideoCapture(0)

height, width = img.shape[:2]
blank= np.zeros((height, width), dtype='uint8')
mask1= cv.circle(blank, (250, 250), 50, 255, thickness=-1)
cv.imshow("mask", mask1)

masked= cv.bitwise_and(img, img, mask = mask1)
cv.imshow("Masked image", masked)
cv.imshow("sea", img)

if cv.waitKey(0) & 0xff == ord('q'):
    cv.destroyAllWindows()
    quit()
