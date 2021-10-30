import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)
# Open CV functioneaza in BGR (Blue Green RED)

# plt.imshow(img)
# plt.show()

# BGR in Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR in HSV 
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR in L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR in RGB
# OpenCV functioneaza in BGR daca folosim cv.imshow(img) va returna imaginea normala, dar in BGR. Daca apelam aceeasi functie pe imaginea transformata in RGB.
# Aceasta va fi schimbata, rosu cu albastru. Daca folosit mathplotlit , si apelam functia pyplot. imaginea RGB va semana cu imaginea importata in BGR(in openCV)
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)


# HSV in BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR', lab_bgr)

cv.waitKey(0)