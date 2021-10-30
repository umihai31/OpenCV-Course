import cv2 as cv

img = cv.imread('Photos/group 1.jpg')
# cv.imshow('Group',img)

# Schimbam in grayscale , deoarece nu avem nevoie de culori in imagine

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray Group',gray)

# Citim xml haar_face.xml

haar_cascade = cv.CascadeClassifier('haar_face.xml')

# faces_rect este formata din coordonatele fetelor
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1) 


print(f'Number of faces found = {len(faces_rect)}')


for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img)    
cv.waitKey(0)

# Haar cascade este foarte sensibil la zgomot, schimband minNeighbour putem reduce asta.