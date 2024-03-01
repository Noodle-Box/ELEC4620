import cv2 as cv
import numpy as np

cap = cv.VideoCapture('___')

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    img = img[0:-200, 400:-400]
    


