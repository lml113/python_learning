import cv2

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH,480)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,320)

while True:
    _,frame = cap.read()

    height,width,_ = frame.shape

    cx = int(width/2)
    cy = int(height/2)

    print(frame[cy,cx])

    cv2.circle(frame,(cx,cy),5,(255,0,0),3)
    cv2.imshow("Frame",frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
