import cv2 as cv
import numpy as np

img = cv.imread('Opencv\images\dogs.jpg')# Read picture
gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)# Convert to grayscale
cv.imshow('Original drawing',img)# Show original
cv.imshow('Grayscale image',gray_img)# Display grayscale image

# 
my_gray_img_data = []
for item in img:
    my_img = []
    for i in item:
        my_img.append(np.uint8(0.299*i[0]+0.587*i[1]+0.114*i[2]))
    my_gray_img_data.append(my_img)
my_gray_img = np.array(my_gray_img_data)
cv.imshow('My grayscale image',my_gray_img)


cv.waitKey(0)# Press the keyboard to stop operation
cv.destroyAllWindows()