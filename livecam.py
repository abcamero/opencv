import cv2

capture = cv2.VideoCapture(0)

while(True):
    ret, frame = capture.read() #ret is for getting the information about camera working properly

    grayFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow('Video Gray',grayFrame)
    cv2.imshow('video orignal', frame)

    if cv2.waitKey(1) == 27:
        break

capture.release()
cv2.destroyAllWindows()
