import numpy as np
import cv2

blacked_img = np.zeros((512, 512, 3), np.uint8)
cv2.imshow("custom img", blacked_img)

white_img = np.ones((512, 512, 3), np.float)
cv2.imshow("white img", white_img)

# to stop images pass 0 as a parameter
if cv2.waitKey(0) & 0xFF == ord("q"):
    exit()
