import cv2
import numpy as np

img = cv2.imread("./inputs/microsoft.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA).astype(np.float32)
img[(70<img[:, :, 0]) &(img[:, :, 0]<100) & (70<img[:, :, 1]) & (img[:, :, 1]<100) & (70<img[:, :, 2]) & (img[:, :, 2]<100)]\
      *= (1, 1, 1, 0)
img = img.astype(np.uint8)
cv2.imwrite("./outputs/microsof_logo.png", img)