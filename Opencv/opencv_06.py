import cv2
import numpy as np

frame = cv2.imread(r'F:\vscode\python\python_learning\Opencv\images\bol.jpg')

gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

ret, binary = cv2.threshold(gray_frame, 80, 255, cv2.THRESH_BINARY)
print(binary)
print(type(binary))

for item in binary:
    print(item)




while True:
    cv2.imshow('Frame',frame)
    cv2.imshow('gray_frame',gray_frame)
    cv2.imshow('binary',binary)
    key = cv2.waitKey(1)
    if(key == 27):
        break

cv2.destroyAllWindows()