import numpy as np
import cv2

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 1, cv2.LINE_AA)

#  show img
cv2.imshow("img", img)
if cv2.waitKey(0) & 0xFF == ord('q'):
    exit()
