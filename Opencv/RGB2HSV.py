import cv2
import numpy as np

# 自定义函数
def my_bgr2hsv(bgr):# bgr转hsv
    B,G,R = bgr
    B,G,R = B/255,G/255,R/255
    bgr_max = max(B,G,R)
    bgr_min = min(B,G,R)
    bgr_c = bgr_max - bgr_min

    H,S,V = 0,0,0
    if(bgr_max == bgr_min):
        H = 0
    elif(bgr_max==R):
        H = 60*(G-B)/bgr_c
    elif(bgr_max==G):
        H = 120+60*(B-R)/bgr_c
    elif(bgr_max==B):
        H = 240+60*(R-G)/bgr_c

    if(H<0):
        H = H+360

    H = np.uint8(H/2)

    if(bgr_max == 0):
        S = 0
    else:
        S = bgr_c/bgr_max
    S = np.uint8(S*255)

    V = np.uint8(bgr_max*255)
    return [H,S,V]

frame = cv2.imread(r'F:\vscode\python\python_learning\Opencv\images\bol.jpg')

Higth,width,_ = frame.shape
print(Higth,width)
hsv_frame = []
for i in range(Higth):
        item = []
        for j in range(width):
            B,G,R = frame[i,j]
            item =item + [my_bgr2hsv([B,G,R])]
        hsv_frame = hsv_frame+[item]

hsv_frame = np.array(hsv_frame)

while True:
    cv2.imshow('HSV_Frame',hsv_frame)
    cv2.imshow('Frame',frame)
    key = cv2.waitKey(1)
    if(key == 27):
        break

cv2.destroyAllWindows()


