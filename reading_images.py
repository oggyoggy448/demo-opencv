import cv2
import numpy as np

img = cv2.imread("logo.jpg")
while True:
    cv2.imshow('img', img)
    px = img[100, 100]
    # print(px)

    # accessing only blue pixel
    blue = img[100, 100, 0]
    # print(blue)

    green = img[100, 100, 1]
    # print(green)

    red = img[100, 100, 2]

    color = [0, 0, 0]
    img[100, 100] = color
    cv2.imshow("img", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
