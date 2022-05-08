# 高斯滤波5x5算子

import numpy as np
import cv2

g = np.array([[1,1,2,1,1],
             [1,3,4,3,1],
             [2,4,8,4,2],
             [1,3,4,3,1],
             [1,1,2,1,1]]
             )
g_sum = sum(sum(g))
g = g/g_sum

frame = cv2.imread(r'F:\vscode\python\python_learning\Opencv\images\Original1.jpg')

Higth,width,_ = frame.shape
print(Higth,width)

v_frame = []
for x in range(2,Higth-2):
    item = []
    for y in range(2,width-2):
        data = np.array([[frame[x-2,y-2],frame[x-1,y-2],frame[x,y-2],frame[x+1,y-2 ],frame[x+2,y-2 ]],
                      [frame[x-2,y-1 ],frame[x-1,y-1 ],frame[x,y-1 ],frame[x+1,y-1 ],frame[x+2,y-1 ]],
                      [frame[x-2,y ],  frame[x-1,y ],  frame[x,y ],  frame[x+1,y ],  frame[x+2,y ]],
                      [frame[x-2,y+1 ],frame[x-1,y+1 ],frame[x,y+1 ],frame[x+1,y+1 ],frame[x+2,y+1 ]],
                      [frame[x-2,y+2 ],frame[x-1,y+2 ],frame[x,y+2 ],frame[x+1,y+2 ],frame[x+2,y+2 ]]])
        R = data[:,:,0]*g
        G = data[:,:,1]*g
        B = data[:,:,2]*g
        a = [np.uint8(sum(sum(R))),np.uint8(sum(sum(G))),np.uint8(sum(sum(B)))]
        item = item+[np.uint8(a)]
    v_frame = v_frame + [item]

v_frame = np.array(v_frame)
print(type(v_frame))
print(type(frame))
print(v_frame)
print(frame)

while True:
    cv2.imshow('Original',frame)
    cv2.imshow('v_frame',v_frame)
    cv2.imwrite(r'F:\vscode\python\python_learning\Opencv\images\Gaussian_filter_image1.jpg',v_frame)
    key = cv2.waitKey(1)
    if(key == 27):
        break

cv2.destroyAllWindows()