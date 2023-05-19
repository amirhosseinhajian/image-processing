import cv2
import numpy as np
from my_image_processing_function import filter_2D

chest_img = cv2.imread("./inputs/chest.png", cv2.IMREAD_GRAYSCALE)
board_img = cv2.imread("./inputs/board.png", cv2.IMREAD_GRAYSCALE)
shape_img = cv2.imread("./inputs/image_noisy.png", cv2.IMREAD_GRAYSCALE)
kernel = np.ones((3, 3))/9
chest_noise_less = filter_2D(chest_img, kernel, 3)
board_noise_less = filter_2D(board_img, kernel, 3)
shape_noise_less = filter_2D(shape_img, kernel, 3)
cv2.imwrite("./outputs/chest.png", chest_noise_less)
cv2.imwrite("./outputs/board.png", board_noise_less)
cv2.imwrite("./outputs/shapes.png", shape_noise_less)