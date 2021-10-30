import cv2 as cv

# Smooth se face in momentul in care avem mult zgomot in imagine
# Definim kernel sau window , este un window ce reprezinta o parte din imagine.Acest window are un size, acesta se numeste kernel size.
# Daca acest window este luat de 3x3 atunci kernelul il vom da de 3x3 
# O metoda de blur este de a lua acest 3x3 si de a face pixelul din interior ca si o medie dintre pixelii vecini.

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

# Averaging -> definim un kernel ex 3x3 si pixelul din interior se media pixelilor vecini
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# Gaussian Blur -> Este unul dintre cele mai folosite 
# Face acelasi lucru ca si agerage , doar ca in loc de media valorii pixelilor, fiecare dintre pixelii vecini primeste un weight si se calculeaza media acestor weights.
# Este un filtru mai natural decat average.
gauss = cv.GaussianBlur(img, (3,3), 0) # imaginea , kernel size, sigmaX sau deviatia standard
cv.imshow('Gaussian Blur', gauss)

# Median Blur -> este ca si average doar ca in loc sa gaseasca media pixelilor , cauta mijlocul lor
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral -> cel mai eficient. Dam un diametru (ex 10) sigmaColor cu cat este o valoare mai mare cu atat sunt mai multe culori luate in considerare in vecinatate
# SigmaSpace cu cat valoarea e mai mare cu atat influenteaza mai multi pixeli valoarea de blurring.
# Seamana cu median blur
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)