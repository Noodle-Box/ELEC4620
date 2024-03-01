import cv2 as cv
import numpy as np

cap = cv.VideoCapture('___')

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    img = img[0:-200, 400:-400]

    img_sobel_x = cv.Sobel(img, cv.CV165, 1, 0, None, 3)
    img_sobel_y = cv.Sobel(img, cv.CV165, 1, 0, None, 3)
    img_sobel = np.abs(img_sobel_x) + np.abs(img_sobel_y)

    img_sobel_norm = (img_sobel - np.min(img_sobel)) / (np.max(img_sobel) - np.min(img_sobel))
    cv.imshow("Image", img_show_norm)
    c = cv.waitKey(16)
    if c == ord('q'):
        break



    



