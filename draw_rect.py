import cv2
import numpy

img = numpy.zeros((512, 512, 3))

img = cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 2)

cv2.imshow("img", img)

if cv2.waitKey(0) & 0xFF == ord("q"):
    exit()
