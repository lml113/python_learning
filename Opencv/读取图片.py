import cv2 as cv
import numpy as np

img = cv.imread('Opencv\images\dogs.jpg')# Read picture
cv.imshow('Original drawing',img)
cv.waitKey(0)# Press the keyboard to stop operation
cv.destroyAllWindows()