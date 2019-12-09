import cv2

# read img in gray scale mode
img = cv2.imread("logo.jpg", 0)
cv2.imshow('img', img)
# print(img)

# reading img in rgb.
rgb_img = cv2.imread("logo.jpg")
print(rgb_img)
cv2.imshow('rgb', rgb_img)
cv2.waitKey(0)
