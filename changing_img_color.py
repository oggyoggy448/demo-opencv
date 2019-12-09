import cv2

cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    _, frame = cap.read()

    # display original window
    cv2.imshow("original imags", frame)
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', gray)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow("hsv image", hsv)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
