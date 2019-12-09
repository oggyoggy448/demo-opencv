import cv2
import numpy as np


def nothing(x):
    pass


# mouse callback function
def draw_cirlce(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), rad, (b, g, r), -1)


# Create a black image, a window
img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)
cv2.createTrackbar('Radius', 'image', 0, 100, nothing)

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_cirlce)

while True:
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break

    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    rad = cv2.getTrackbarPos("Radius", "image")

cv2.destroyAllWindows()
