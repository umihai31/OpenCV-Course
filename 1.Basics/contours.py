import cv2 as cv
import numpy as np


img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

# Este linia care inconjoara un obiect , matematic vorbind este diferit de edges

blank = np.zeros(img.shape, dtype='uint8') # O imagine de marimea img. neagra
# cv.imshow('Blank', blank)

# 1. Convertim imaginea la grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# 2. Se cauta marginile imaginii , folosind canny
# Din pacate la imshow sunt mult prea multe imagini. si trebuie blurata imaginea pentru a scapa de cele care nu sunt necesare
canny = cv.Canny(blur, 125, 175) # S-au gasit 380 contours, este mai bun decat daca am face o imagine binarizata
cv.imshow('Canny Edges', canny)

# Se uita in imagine si incearca sa o binarizeze .Daca valoarea pixelului este < 125 o va face 0 si daca este mai mare sau egala de cat 125 va fi  1
# Sa folosit pentru a face un compare cu canny  pentru a vedea cate contours s-au gasit (839 contours)
# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) 
# cv.imshow('Thresh', thresh)


# 3. Se cauta contours. Functia findContours returneaza 2 variabile , contours( o lista cu toate conturile) si herarchies(reprezentarea ierarhica).
# se da imaginea cu marginile gasite. mode ex cv.RETR_LITS - pentru o lista cu acestea cv.RETRE_EXTERNAL returneaza toate contururile externe.RETRE_TREE returneaza toate contururile ierarhice. Aproximarea conturilor. CHAIN_ARPOX_NONE doar returneaza contururile. CHAIN_APRX_SIMPLE -> daca avem o linie compreseaza aceasta linie in 
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

# Vom desena peste imaginea blank(ce este neagra) contours gasite. 
cv.drawContours(blank, contours, -1, (0,0,255), 1) # functia ia imaginea pe care vrem sa desenam , o lista(cazul nostru contours) . -1 reprezinta ca vrem sa desenam pe toate, daca am fi vrut un numar specific am fi spus exact, urmeaza culoarea si thickness
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)