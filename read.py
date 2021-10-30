import cv2 as cv

# citire imagine
# img = cv.imread('Photos/cat_large.jpg')  # o imagine mare are posibilitatea de a se afisa pe mai multe ecrane

# afisare imagine, primul parametru este numele figurii si matricea ce va fi afisata
# cv.imshow('Cat', img)

# cv.waitKey(0) # este un delay daca este 0 va fi infinit iar daca este specificat (!= 0) se asteapta pana cand se poate apasa 

# Read videos

capture = cv.VideoCapture('Videos/dog.mp4') # are 2 tipuri de inputuri int - se foloseste de exemplu cand este conectata o camera web 0 va fi pentru web 1 pentru o camera externa etc. 
# sau poate fi dat un path 

while True:
    isTrue, frame = capture.read() # citeste frame by frame
    cv.imshow('Video',frame) # display fiecare frame

    if cv.waitKey(20) & 0xFF == ord('d'): # pentru a iesi din while -> daca este apasat butonul d se opreste
        break
capture.release()
cv.destroyAllWindows

# se observa ca dupa ce se termina video se obtine eroarea -215 o eroare negativa . nu se mai gasesc frame-uri. La imagini eroarea apare cand este gresit pathu-l cand nu gaseste img
