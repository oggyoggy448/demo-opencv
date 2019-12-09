import cv2

# camera number is mentioned in videocapture class or file name which you have to read
camera = cv2.VideoCapture(0)

# reading images
while True:
    ret,frame = camera.read()
    cv2.imshow("window",frame)

    # to stop the camera
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# when you close the camera do it.
camera.release()
cv2.destroyAllWindows()
