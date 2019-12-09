import cv2
import numpy as np

img = cv2.imread("logo.jpg")
# read value from image
red = img.item(100, 100, 2)
print(red)

# set value and returns None
img.itemset((100, 100, 2), 100)
red = img.item(100, 100, 2)
print(red)
