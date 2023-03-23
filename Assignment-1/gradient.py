import cv2
import numpy as np

gradient = np.zeros((480, 480), np.uint8)
for i in range(0, len(gradient), 5):
    gradient[i:i+5, :] = round(i*255/480)
cv2.imwrite("./processed images/gradient.jpg", gradient)