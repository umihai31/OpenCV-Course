import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# Histograma ajuta la vizualizarea intensitatii pixelilor 

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

mask = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)

masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('Mask', masked)

# Histograma grayscale 
# Lista de histograme , lista de indexi , mask , histSize - numarul de bins ca si lista, range-ul pixelilor
# gray_hist = cv.calcHist([img], [0], mask, [256], [0,256] )

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# Histograma pentru culori, rgb

plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Intensitate')
plt.ylabel('NR pixels')
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)