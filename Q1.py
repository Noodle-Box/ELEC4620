import cv2 as cv
import numpy as np

#import image and show on screen
img = cv.imread("")

#convert to grey scale
img_gray = cv.cvtColour(img, cv.COLOUR_BGR2GRAY)

#blur image
img_blur = cv.GaussianBlur(img_gray, (5,5), 0)


#edge detector. Look at OpenCV documentation
#edges = cv.Canny(img_gray, 150, 250)
grad_x = cv.Sobel(img_gray, cv.CV_16F, 1, 0, ksize = 3)
grad_x_norm = (grad_x - np.min(grad_x))/(np.max(grad_x - np.min(grad_x)))

grad_y = cv.Sobel(img_gray, cv.CV_16F, 1, 0, ksize = 3)
grad_y_norm = (grad_y - np.min(grad_y))/(np.max(grad_y - np.min(grad_y)))

#combine!
grad = np.abs(grad_x) + np.abs(grad_y)
grad_norm = (grad - np.min(grad)) / (np.max(grad) - np.min(grad))


#print image and show

cv.imshow("Out", np.hstack([grad_x_norm,grad_y_norm, grad_norm]))
cv.waitKey()

# Download the Images/Video off blackboard
# Read in the images/video