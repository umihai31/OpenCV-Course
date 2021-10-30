import cv2 as cv
import numpy as np


img = cv.imread('Photos/park.jpg') # IMaginea de BGR image (Blue Green Red)
cv.imshow('Park',img)

# Translation -> shiftarea imaginii pe axele x si y (stanga dreapta sus jos)
def translate(img, x, y):
    # -> avem nevoie de o matrice de translatie formata dintr-o lista ,formata la randul ei din 2 liste 
    transMat = np.float32([[1,0,x],[0,1,y]]) 
    # -> touple de dimensiuni formata din img.shape[1] -> width si img.shape[0]-> height
    dimensions = (img.shape[1], img.shape[0]) 
    # Functia warpAffine transforma imaginea sursa (img) folosind o matrice specifica
    return cv.warpAffine(img,transMat,dimensions)

# Daca vem valori negative pe x ,imaginea se translateaza la stanga, daca avem pe y va fi in sus,POzitive vor fi in dreapta si jos


transalted = translate(img, -100, 100)
cv.imshow('Translated',transalted)


# Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2] # ia primele 2 valori din img.shape
    # Daca nu specificam punctul de rotatie, acesta va fi automat la jumatatea imaginii.
    if rotPoint is None:
        rotPoint = (width//2,height//2)
    # Se creeaza matricea de rotatie, cu functia getRoationMatrix2D care va lua punctul de rotatie, unghiul si un scale(pentru a scala imaginea.)    
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width,height)
    # Functia warpAffine transforma imaginea sursa (img) folosind o matrice specifica
    return cv.warpAffine(img,rotMat,dimensions)

rotated = rotate(img,-45)
cv.imshow('Rotated',rotated)
rotated_rotated = rotate(rotated,-45)
# cv.imshow('rotated_rotated',rotated_rotated) 
# imaginea rotita inca o data va avea parti lipsa din imaginea veche, deoarece prima data cand o rotim aceasta va iesi din dimensiunea imaginii si python o va considera ca nu este o imagine
rotated_rotated_rotated = rotate(rotated_rotated,-45)
# cv.imshow('rotated_rotated_rotated',rotated_rotated_rotated) 

# Resizing 
# Pentru a face imaginea mai mica vom folosit interpolatrea INTER_AREA,daca vrem sa marim imaginea folosim INTER_LINEAR sau INTER_CUBIC
resized = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC) 
cv.imshow('Resized',resized)

# Flipping
# flip code , poate fi 0 -> flip vertical, 1 flip horizontally, -1 flip pe x si y
flip = cv.flip(img,-1)
cv.imshow('Flip',flip)


# Cropping
crop = img[200:400, 300:400]
cv.imshow('Cropped',crop)
cv.waitKey(0)