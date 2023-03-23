import cv2
import numpy as np

img = cv2.imread("./source images/3.jpg")
img_shape = img.shape
d1 = img_shape[0]-1
new_img = np.empty((d1+1, img_shape[1], img_shape[2]), np.uint8)
for i, x in enumerate(img):
    for j, y in enumerate(x):
        for k, z in enumerate(y):
            new_img[i, j, k] = img[d1-i, j, k]
cv2.imwrite("./processed images/3.jpg", new_img)