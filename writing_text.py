import cv2
import numpy

img = numpy.zeros((512, 512, 3))
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow("img", img)

if cv2.waitKey(0) & 0xFF == ord("q"):
    exit()