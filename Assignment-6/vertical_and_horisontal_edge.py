import cv2
import numpy as np
from my_image_processing_function import filter_2D

house_img = cv2.imread("./inputs/house.png", cv2.IMREAD_GRAYSCALE)
horisintal_kernel = np.array([[-1, -1, -1],
                               [0, 0, 0],
                               [1, 1, 1]])
vertical_kernel = np.array([[2, 0, -2],
                            [2, 0, -2],
                            [2, 0, -2]])
horisontal_edges = filter_2D(house_img, horisintal_kernel, 3)
vertical_edges = filter_2D(house_img, vertical_kernel, 3)
cv2.imwrite("./outputs/house_horisontal.png", horisontal_edges)
cv2.imwrite("./outputs/house_vertical.png", vertical_edges)