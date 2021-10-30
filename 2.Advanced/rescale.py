import cv2 as cv

# pentru a face rescale la un frame creem o functie
def rescaleFrame(frame, scale=0.75):
    # Metoda functioneaza la imagini si la video care exista deja
    width = int(frame.shape[1] * scale) # frame.shape[1] -> width din imagine Sunt valori floating points trebuie convertite in int
    height = int(frame.shape[0] * scale) # frame.shape[0] -> height din imagine

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) # va face resize la un frame la o anumita dimensiune 


def changeRes(width,height):
    # metoda functioneaza pentru live videos
    capture.set(3,width) # 3 referenteaza width
    capture.set(4,height) # 4 referentiaza height


# -------------------------------------CITIRE IMAGINE---------------------------------
img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)
#-------------------RESIZE IMAGINE--------------------
resized_image = rescaleFrame(img)
cv.imshow('Image',resized_image)


#-------------------------------------CITIRE VIDEO------------------------------------
capture = cv.VideoCapture('Videos/dog.mp4') # are 2 tipuri de inputuri int - se foloseste de exemplu cand este conectata o camera web 0 va fi pentru web 1 pentru o camera externa etc. 
# sau poate fi dat un path 

while True:
    isTrue, frame = capture.read() # citeste frame by frame
#-----------------RESIZE FRAME VIDEO-----------------------------
    frame_resized = rescaleFrame(frame, scale=.2)

    cv.imshow('Video',frame) # display fiecare frame
    cv.imshow('Video Resized',frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'): # pentru a iesi din while -> daca este apasat butonul d se opreste
        break
capture.release()
cv.destroyAllWindows