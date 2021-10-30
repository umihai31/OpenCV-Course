import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

# Convertim la grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Laplacian

lap = cv.Laplacian(gray, cv.CV_64F) # Calculeaza gradientii imaginii grayscale
lap = np.uint8(np.absolute(lap)) # Toti pixelii vor fi convertiti la valori absolute sa nu fie valori negative
cv.imshow('Laplacian', lap)

# Sobel 
# Calculeaza gradientii in 2 directii
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0) # directia pe x 
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1) # directia pe y
combined_sobel = cv.bitwise_or(sobelx, sobely) # 

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)

canny = cv.Canny(gray, 150, 175) # threshold 150 si val maxima 175
cv.imshow('Canny', canny)
cv.waitKey(0)