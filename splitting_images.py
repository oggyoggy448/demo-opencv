import numpy as np
import cv2

black = np.zeros((512, 512, 3), np.float)
# splitting the img
color = cv2.split(black)
# print(color)


b = black[:, :, 0]
# print(b)

# updating all the red values
black[:, :, 2] = 255
