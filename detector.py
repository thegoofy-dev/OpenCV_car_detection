# Importing the neccesarry library
import cv2
import time
import numpy as np

# Reading the Video
capture = cv2.VideoCapture('video2.avi')

while True:
    isTrue, frame = capture.read()

    # Original Frame
    cv2.imshow("Media Player", frame)

    # Breakpoint of the VideoScreen (By pressing 'x' or 'X' video will close)
    if cv2.waitKey(20) & 0xFF== ord('x'):
        break

capture.release()
cv2.destroyAllWindows()

