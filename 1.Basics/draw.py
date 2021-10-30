import cv2 as cv
import numpy as np

# Crearea unei imagini blank
blank = np.zeros((500,500,3), dtype='uint8') # trebuie sa ii dam un shape de 3 , pentru fiecare canal de culoare
cv.imshow('BLANK',blank)

# 1. Paint imagine in a color
# blank[:] = 0,0,255 # Pentru fiecare canal ii dam culoare care vrem sa o facem
# blank[200:300, 300:400] = 0,0,255 # se foloseste pentru a schimba culoare intr-un range specific de pixeli
# cv.imshow("GREEN",blank)

# 2 Draw a rectangle

# im imaginea blank face un rectangle de la punctul (0,0) pana la punctul(250,250) de culoare (0,255,0) -> VERDE thickness e folosit pentru grosime ,-1 sau cv.FILLED va umple 
# cv.rectangle(blank,(0,0),(250,500),(0,255,0), thickness=cv.FILLED)  
# o alta alternativa de a umple pe jumatate width si jumatate din height 
cv.rectangle(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2),(0,255,0), thickness=cv.FILLED) 
cv.imshow('Rectangle',blank)


# 3. Draw a circle

# in imaginea blank ii dam punctul de mijloc al cercului (250, 250), o raza de 40, si o culoare(0,0,255)-> RED
cv.circle(blank,(250,250), 40,(0,0,255), thickness=3) 
# alternativ putem sa da centru imaginii ca si jumatate din width si jumatate din height, thickness poate fi -1 pentru a fi filled
cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2), 40,(0,0,255), thickness=-1) 
cv.imshow('Circle',blank)


# 4 Draw a line
# Pentru a desena o linie in imagine blank , punctul de inceput, final , culoare si thickness
cv.line(blank,(100,250),(300, 400),(255,255,255), thickness= 3)
cv.imshow('Line',blank)

# 5 Write text in a image
# in imaginea blank punem textul Hello de la poz (225,225) cu fontul specificat si culoarea specificata
cv.putText(blank,'Hello',(225,225),cv.FONT_HERSHEY_TRIPLEX,1.0, (0,255,0), thickness=2)
cv.imshow('Text',blank)

cv.waitKey(0)