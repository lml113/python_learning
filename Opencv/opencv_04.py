import cv2
import numpy as np

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH,480)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,320)
while True:
    _,frame = cap.read()# RGB image

# hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    hsv_frame = list()

    for i in range(320):
        item = []
        for j in range(480):
            B,G,R = frame[i,j]
            item = item+[[R,G,B]]
    
        hsv_frame = hsv_frame+[item]

    hsv_frame = np.array(hsv_frame)

    # print("frame:",type(frame))
    # print("hsv_frame:",type(hsv_frame))

    # print("frame:",frame[160,240])
    # print(hsv_frame)
    # print("hsv_frame:",hsv_frame[160,240])

    cv2.imshow("Frame",hsv_frame)

    key = cv2.waitKey(1)
    if key == 27:
        break


cap.release()
cv2.destroyAllWindows()

