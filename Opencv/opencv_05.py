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

frame = cv2.imread(r'F:\vscode\python\python_learning\Opencv\images\1.jpg')

hsv_frame_b = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

lower = [60, 155, 215]     # 适用于橙色乒乓球4<=h<=32
upper = [80, 175, 235]

Higth,width,_ = frame.shape

hsv_frame = []
binary = []
for i in range(Higth):
        item = []
        bin_itrm=[]
        for j in range(width):
            B,G,R = frame[i,j]
            hsv = my_bgr2hsv([B,G,R])
            item =item + [hsv]
            if((hsv < upper) & (hsv > lower)):
                bi = [np.uint8(255)]
            else:
                bi=[np.uint8(0)]
            bin_itrm = bin_itrm+bi
            
        hsv_frame = hsv_frame+[item]
        binary = binary + [bin_itrm] 

hsv_frame = np.array(hsv_frame)
binary = np.array(binary)

while True:
    cv2.imshow('Frame',frame)
    cv2.imshow('HSV_Frame',hsv_frame)
    # cv2.imshow('hsv_frame_b',hsv_frame_b)
    cv2.imshow('binary',binary)
    key = cv2.waitKey(1)
    if(key == 27):
        break

cv2.destroyAllWindows()

