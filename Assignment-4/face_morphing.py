import cv2
import numpy as np

ana_img = cv2.imread("./source_images/female-01.jpg").astype(np.float32)
david_img = cv2.imread("./source_images/male-01.jpg").astype(np.float32)
result = ana_img
for i in range(1, 5):
    morph_img = cv2.add(david_img*(i/4), ana_img*((4-i)/4))
    result = np.concatenate((result, morph_img), axis=1)
result = result.astype(np.uint8)
cv2.imwrite("./outputs/morph.jpg", result)