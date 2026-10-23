import numpy as np
import cv2 as cv
blank= np.zeros((500, 500, 3), dtype= 'uint8')
cv.imshow('blank', blank)
cv.waitKey(1000)
blank[:]=0, 0, 0
blank[200:300, 100:300]=1, 255, 100
cv.imshow('colour', blank)
cv.waitKey(100)
blank[:]=0, 0, 0
blank[200:300, 110:310]=1, 255, 100
cv.imshow('colour', blank)
cv.waitKey(100)
blank[:]=0, 0, 0
blank[200:300, 120:320]=1, 255, 100
cv.imshow('colour', blank)
cv.waitKey(100)
blank[:]=0, 0, 0
blank[200:300, 130:330]=1, 255, 100
cv.imshow('colour', blank)
cv.waitKey(100)
blank[:]=0, 0, 0
blank[200:300, 140:340]=1, 255, 100
cv.imshow('colour', blank)
cv.waitKey(100)
blank[:]=0, 0, 0
blank[200:300, 150:350]=1, 255, 100
cv.imshow('colour', blank)
cv.waitKey(100)
blank[:]=0, 0, 0
blank[200:300, 160:360]=1, 255, 100
cv.imshow('colour', blank)
cv.waitKey(100)
blank[:]=0, 0, 0
blank[210:310, 160:360]=1, 255, 100
cv.imshow('colour', blank)
cv.waitKey(100)
blank[:]=0, 0, 0
blank[220:320, 160:360]=1, 255, 100
cv.imshow('colour', blank)
cv.waitKey(100)
blank[:]=0, 0, 0
blank[230:330, 160:360]=1, 255, 100
cv.imshow('colour', blank)
cv.waitKey(100)
blank[:]=0, 0, 0
blank[240:340, 160:360]=1, 255, 100
cv.imshow('colour', blank)
cv.waitKey(100)
blank[:]=0, 0, 0
blank[250:350, 160:360]=1, 255, 100
cv.imshow('colour', blank)
cv.waitKey(100)
cv.rectangle(blank, (0,0), (50,100), (0, 255,0), thickness=cv.FILLED)
#blank[:]=0, 200, 0
cv.imshow('colour', blank)
cv.waitKey(1000)
