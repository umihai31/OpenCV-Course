import cv2 as cv
import numpy as np

# Masking , ne ajuta se ne focusam pe anumite parti din imagine.
# Daca avem de ex o imagine a oamenilor si vrem sa ne focusam pe fete, aplicam o masca pe fetele oamenilor
img = cv.imread('Photos\cats 2.jpg')
cv.imshow('Cats', img)

# Creem o imagine blank de dimensiunea imaginii.Dimensiunea mastii ar trebui sa fie de aceeasi ca si imaginea referinta
blank = np.zeros(img.shape[:2], dtype='uint8')
# cv.imshow('Blank Image', blank)


circle = cv.circle(blank.copy(), (img.shape[1]//2 + 45,img.shape[0]//2), 100, 255, -1)

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

weird_shape = cv.bitwise_and(circle,rectangle)
# cv.imshow('Weird Shape', weird_shape)

masked = cv.bitwise_and(img,img,mask=weird_shape)
cv.imshow('Weird Shaped Masked Image', masked)

cv.waitKey(0)