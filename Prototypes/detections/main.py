"""
import cv2

#Trained DatatSet

trainedDataset= cv2.CascadeClassifier('venv/haarcascade_frontalface_default.xml')

#Read a Image
img=cv2.imread('venv/img/me.jpg')

# Convert into grayscale
gray=cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
face=trainedDataset.detectMultiScale(gray)
print(face)

for x,y,w,h in face:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('me',img)
#cv2.imshow('Gray',gray)


"""
"""
import cv2

trainedDataset= cv2.CascadeClassifier('venv/haarcascade_frontalface_default.xml')

video=cv2.VideoCapture(0)
while True:
    success,frame=video.read()
    if success==True:
        gray_image=cv2.cvtColor(frame,cv2.COLOR_BGRA2GRAY)
        face = trainedDataset.detectMultiScale(gray_image)
        for x, y, w, h in face:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imshow('video',frame)
        key=cv2.waitKey(1)
        if key == 81 or key == 113:
            break

    else:
        print("Video Completed Or frame Null")
        break
"""
from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("keras_Model.h5", compile=False)

# Load the labels
class_names = open("labels.txt", "r").readlines()

# CAMERA can be 0 or 1 based on default camera of your computer
camera = cv2.VideoCapture(0)

while True:
    # Grab the webcamera's image.
    ret, image = camera.read()

    # Resize the raw image into (224-height,224-width) pixels
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

    # Show the image in a window
    cv2.imshow("Webcam Image", image)

    # Make the image a numpy array and reshape it to the models input shape.
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normalize the image array
    image = (image / 127.5) - 1

    # Predicts the model
    prediction = model.predict(image)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    print("Class:", class_name[2:], end="")
    print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

    # Listen to the keyboard for presses.
    keyboard_input = cv2.waitKey(1)

    # 27 is the ASCII for the esc key on your keyboard.
    if keyboard_input == 27:
        break

camera.release()
cv2.destroyAllWindows()




