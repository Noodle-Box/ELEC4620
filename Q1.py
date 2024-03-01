import cv2 as cv
import numpy as np

#import image and show on screen
img = cv.imread("StreetSigns/Image0.jpg")

#convert to grey scale
#img_gray=cv.cvtColour(img, cv.COLOUR_BGR2GRAY)


#edge detector. Look at OpenCV documentation
#edges = cv.Canny(img_gray, 150, 250)
#grad_x = cv.Sobel(img_gray, cv.CV_16F, 1, 0, ksize = 3)
#grad_x = (grad_x - np.min(grad_x))/(np.max(grad_x - np.min(grad_x)))

#grad_y = cv.Sobel(img_gray, cv.CV_16F, 1, 0, ksize = 3)
#grad_y = (grad_y - np.min(grad_y))/(np.max(grad_y - np.min(grad_y)))

#combine!
#grad_xy_norm = (grad)

#print image and show
#print(img.shape)
#cv.imshow("Image", grad_x)
#cv.waitKey()
