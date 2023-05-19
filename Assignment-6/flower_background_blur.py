import cv2
import numpy as np
from my_image_processing_function import filter_2D, make_mask

img = cv2.imread("./inputs/flower_input.jpg", cv2.IMREAD_GRAYSCALE)
noise_less_img = filter_2D(img, np.ones((11, 11))/pow(11, 2), 11)
mask, not_mask = make_mask(noise_less_img, 134)
blured_img = filter_2D(img, np.ones((51, 51))/pow(51, 2), 51)
result = blured_img*not_mask + mask*img
cv2.imwrite("./outputs/flower.png", result)