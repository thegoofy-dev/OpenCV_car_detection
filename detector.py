# Importing the neccesarry library
import cv2
import time
import numpy as np

# Reading the Video
capture = cv2.VideoCapture('video2.avi')

# Functions to Re-size the frame 
def rescaleFrame(frame, scale=2):

    # Doubling the original frame
    width = int(frame.shape[1] * scale)
    heigth = int(frame.shape[0] * scale)

    # setting the (width, height) =  (x, y)
    dimensions = (width, heigth)

    # returning the resized frame
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

car_classifier = cv2.CascadeClassifier('cars.xml')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    # Original Frame
    cv2.imshow("Media Player", frame)

    # Resized Frame
    cv2.imshow("Resized Media Player", frame_resized)
    
    # Converting the Resized_frame color BGR to Grayscale 
    gray = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)

    # Passing our frames to our car classifier!
    cars = car_classifier.detectMultiScale(gray, 1.4, 2)

    # Extract bounding bpxes for any bodies identified
    for (x,y,w,h) in cars:
        cv2.rectangle(frame_resized, (x,y),(x+w, y+h), (0,0,255), 2)
        cv2.imshow("Car Detector", frame_resized)

    # Breakpoint of the VideoScreen (By pressing 'x' or 'X' video will close)
    if cv2.waitKey(20) & 0xFF== ord('x'):
        break

capture.release()
cv2.destroyAllWindows()