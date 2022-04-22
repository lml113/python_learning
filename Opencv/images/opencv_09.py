# 轮廓检测
import cv2


frame = cv2.imread(r'F:\vscode\python\python_learning\Opencv\images\bol_2.jpg')



while True:
    cv2.imshow('Frame',frame)
    key = cv2.waitKey(1)
    if(key == 27):
        break

cv2.destroyAllWindows()