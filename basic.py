import cv2 as cv
img = cv.imread('Photos/park.jpg') # IMaginea de BGR image (Blue Green Red)

cv.imshow('Park',img)

# 1 Convert to greyscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)


# 2 Blur an iamge -> Reduce zgomotul
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('BLUR',blur)


# Edge cascade -> detectarea marginilor.
canny = cv.Canny(img, 125,175) 
cv.imshow('Canny Edges',canny) # Se observa ca sunt multe margini in imagine
# pentru a reduce asta putem sa dam ca si imagine de referinta imaginea blurata
canny_blur = cv.Canny(blur,125,175)
cv.imshow('canny blured',canny_blur)



# Dilatarea imaginii
dilated = cv.dilate(canny_blur ,(7,7), iterations=2)
cv.imshow('Dilated',dilated)

# 5 Eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded',eroded)



# 6. Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC) 
cv.imshow("Resized",resized)

# 7. Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)