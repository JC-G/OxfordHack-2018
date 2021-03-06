import keras
from keras.preprocessing.image import img_to_array
import imutils
import cv2
from keras.models import load_model
import numpy as np
import time
from pathlib import Path

detection_model_path = ""
emotion_model_path = ""
face_detection = ""
emotion_classifier = ""
camera = 0
go = True
value = ((0,0))
EMOTIONS = ["angry", "disgust", "scared", "happy", "sad", "surprised",
            "neutral"]
def toReturn(lst):

    if lst.index(max(lst)) == 3:
        return 1
    elif lst.index(max(lst)) == 4 or lst.index(max(lst)) == 6:
        return 0
    else:
        return -1


def destroy():

    camera.release()
    cv2.destroyAllWindows()
#feelings_faces = []
#for index, emotion in enumerate(EMOTIONS):
   # feelings_faces.append(cv2.imread('emojis/' + emotion + '.png', -1))


def initControl(addloc = ""):
    global detection_model_path,emotion_model_path,face_detection,emotion_classifier,camera
    detection_model_path = addloc + "haarcascade_files/haarcascade_frontalface_default.xml"
    emotion_model_path = addloc + 'models/_mini_XCEPTION.102-0.66.hdf5'

    face_detection = cv2.CascadeClassifier(detection_model_path)
    emotion_classifier = load_model(emotion_model_path, compile=False)
    camera = cv2.VideoCapture(0)

def captureFrame():
    initControl("EmotionRecognitionMaster/")
    global go, value
    go = True
    while go:

        time.sleep(0.01)
        # parameters for loading data and images


        # hyper-parameters for bounding boxes shape
        # loading models


        #cv2.namedWindow('your_face')
        # starting video streaming

        frame = camera.read()[1]
        #reading the frame
        frame = imutils.resize(frame,width=600)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detection.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)

        canvas = np.zeros((500, 600, 3), dtype="uint8")
        frameClone = frame.copy()
        if len(faces) > 0:
            faces = sorted(faces, reverse=True,
            key=lambda x: (x[2] - x[0]) * (x[3] - x[1]))[0]
            (fX, fY, fW, fH) = faces
                        # Extract the ROI of the face from the grayscale image, resize it to a fixed 28x28 pixels, and then prepare
                # the ROI for classification via the CNN
            roi = gray[fY:fY + fH, fX:fX + fW]
            roi = cv2.resize(roi, (64, 64))
            roi = roi.astype("float") / 255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis=0)


            preds = emotion_classifier.predict(roi)[0]
            emotion_probability = np.max(preds)
            label = EMOTIONS[preds.argmax()]

            resList = preds.tolist()

            for (i, (emotion, prob)) in enumerate(zip(EMOTIONS, preds)):
                        # construct the label text
                        text = "{}: {:.2f}%".format(emotion, prob * 100)

                        # draw the label + probability bar on the canvas
                    # emoji_face = feelings_faces[np.argmax(preds)]

                        w = int(prob * 600)

                        #ORIGINAL width of screen is 600
                        # width of screen is 300

                        acc = 0
                        errprop = 1/15
                        err = 600 * errprop
                        if fX+fW/2 > 600/2 + err/2:
                            acc = (600/2 + err/2 - (fX+fW/2))/(600-err)*20
                        elif fX+fW/2 < 600/2 - err/2:
                            acc = (600/2 - err/2 - (fX+fW/2))/(600-err)*20

                        # cv2.rectangle(canvas, (7, (i * 35) + 5),
                        # (w, (i * 35) + 35), (0, 0, 255), -1)
                        # cv2.putText(canvas, text, (10, (i * 35) + 23), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 2)
                        # cv2.putText(frameClone, label+" "+str(acc), (fX, fY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
                        # cv2.rectangle(frameClone, (fX, fY), (fX + fW, fY + fH), (0, 0, 255), 2)
        #cv2.imshow('your_face', frameClone)
        #cv2.imshow("Probabilities", canvas)
        if len(faces)>0:
            value = ((toReturn(resList),acc))
        else:
            value = ((0,0))

    destroy()

#    for c in range(0, 3):
#        frame[200:320, 10:130, c] = emoji_face[:, :, c] * \
#        (emoji_face[:, :, 3] / 255.0) + frame[200:320,
#        10:130, c] * (1.0 - emoji_face[:, :, 3] / 255.0)


    


