import cv2

# local video
cap = None
try:
    cap = cv2.VideoCapture('output.avi')

except FileNotFoundError:
    print("file is not found")
    exit()

if not cap.isOpened():
    cap.open("vtest.avi")

while True:
    ret, frame = cap.read()
    # frame = cap.read()[1]

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
