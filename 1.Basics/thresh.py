import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray",gray)

# Simple Thresholding
# Returneaza 2 outputuri. dam imaginea grayscale ,o valoare de threshold (ex155) si o valoare maxima. si un thresholding type.
# Val pixel < 150(threshold) => val = 0 Daca e mai mare sau egala va fi 255
threshold, thresh = cv.threshold(gray,225,255,cv.THRESH_BINARY)
# cv.imshow('Thresholded simple',thresh)

threshold, thresh_inv = cv.threshold(gray,225,255,cv.THRESH_BINARY_INV)# Functia de la final face practic inversul , val < 150 o face 255 si >=150 va fi 0
# cv.imshow('Thresholded invers',thresh_inv) 


# Adaptive threshold
# Lasam sa caute singur valoarea 
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,11,9)
cv.imshow('Adaptive thresholding',adaptive_thresh)
cv.waitKey(0)