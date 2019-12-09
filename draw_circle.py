import cv2
import numpy

img = numpy.zeros((512, 512, 3), numpy.float)

# first coordinates represent location and third parameter specify radius
img = cv2.circle(img, (200, 100), 100, (0, 0, 255), -1)

cv2.imshow("img", img)

if cv2.waitKey(0) & 0xFF == ord("q"):
    exit()
