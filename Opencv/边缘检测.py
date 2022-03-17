import cv2 as cv
import numpy as np

img = cv.imread('Opencv\images\girl.jpg',0)# Direct to grayscale
cv.imshow('img',img)
blur = cv.GaussianBlur(img, (3, 3), 0)  # 用高斯滤波处理原图像降噪
for i in range(5):
    blur = cv.GaussianBlur(blur, (3, 3), 0)  # 用高斯滤波处理原图像降噪
# cv.imshow('img',img)
cv.imshow('blur',blur)

canny = cv.Canny(blur, 80, 110)  # 50是最小阈值,150是最大阈值
canny_not = cv.Canny(img,50,100)

# cv.namedWindow("canny",0);#可调大小
# cv.namedWindow("canny_not",0);#可调大小

cv.imshow('canny',canny)
# cv.imshow('canny_not',canny_not)

cv.waitKey(0)# Press the keyboard to stop operation
cv.destroyAllWindows()