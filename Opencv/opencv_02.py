import cv2
# 采集摄像头图像
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH,800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,600)

while True:
    _,frame = cap.read()

    hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    y_frame = cv2.cvtColor(frame,cv2.COLOR_RGB2YCrCb)

    height,width,_ = hsv_frame.shape

    cx = int(width/2)
    cy = int(height/2)

    print(hsv_frame[cy,cx],frame[cy,cx],y_frame[cy,cx])

    cv2.circle(frame,(cx,cy),5,(255,0,0),3)
    cv2.imshow("Frame",frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
