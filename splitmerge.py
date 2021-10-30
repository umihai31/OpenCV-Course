import cv2 as cv
import numpy as np

# Imaginea este formata din mai multe canale(matrici de pixeli)
# In OpenCV imagina este blue green red BGR

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

# Se creaza un blank image care este o image de dimensiunea imaginii initiale dar pe un singur layer
blank = np.zeros(img.shape[:2], dtype='uint8')

# Canalele de culoare blue green red
b,g,r = cv.split(img)

# Pentru a vedea imaginile in culoarea lor adevarata , trebuie sa punem imaginea blank in layerele lipsa
# ex: pentru blue , fiind primul layer vom pune blank pe layerele 2 si 3
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

# Display toate cele 3 canale,din cauza ca shape la fiecare dintre cele canale ,imaginile celor 3 vor fi grayscale.
# Grayscale este o imagine cu un singur layer de culoare
cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

# Shape-ul imaginii + celor 3 canale
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merged Image', merged)

cv.waitKey(0)