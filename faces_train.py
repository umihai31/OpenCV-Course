import os
import cv2 as cv
import numpy as np

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
DIR = r'E:\Projects\PythonVisualStudio\OpenCV\Faces\train'

features = [] # contine fiecare fata din poze
labels = [] # contine labelurile pentru fiecare fata din features

haar_cascade = cv.CascadeClassifier('haar_face.xml')

def create_train():
    for person in people:
        path = os.path.join(DIR,person)
        label = people.index(person)

        # Suntem in folderul fiecarei persoane
        for img in os.listdir(path):
            img_path = os.path.join(path,img)
            # luam fiecare imagine si o transformam in gray
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            # Cautam fetele
            
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4) 
            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)


create_train()

# convertim la numpy
features = np.array(features,dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
# Antrenarea recognizerului pe lista de features si labels
face_recognizer.train(features,labels)

# Putem salva modelul antrenat
face_recognizer.save('face_traine.yml')

np.save('features.npy',features)
np.save('Labels.npy',labels)

