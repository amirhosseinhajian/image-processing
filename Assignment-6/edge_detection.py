import cv2
import numpy as np
from my_image_processing_function import filter_2D

spider_img = cv2.imread("./inputs/spider.png", cv2.IMREAD_GRAYSCALE)
lion_img = cv2.imread("./inputs/lion.png", cv2.IMREAD_GRAYSCALE)
kernel = np.array([[-1, -1, -1],
                   [-1,  8, -1],
                   [-1, -1, -1]])
spider_blur = filter_2D(spider_img, np.ones((3, 3))/9, 3)
spider_edges = filter_2D(spider_blur, kernel, 3)
lion_edges = filter_2D(lion_img, kernel, 3)
cv2.imwrite("./outputs/spider.png", spider_edges)
cv2.imwrite("./outputs/lion.png", lion_edges)