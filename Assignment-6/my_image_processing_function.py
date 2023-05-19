import numpy as np
import cv2

def filter_2D(src, kernel, dimension):
    rows, cols = src.shape
    result = np.zeros((rows, cols), dtype=np.uint8)
    num = dimension//2
    for i in range(num, rows-num):
        for j in range(num, cols-num):
            cell = src[i-num:i+num+1, j-num:j+num+1]
            result[i, j] = np.abs(np.sum(kernel * cell))
    return result

def make_mask(src, thresh):
    _, thresh = cv2.threshold(src, thresh, 255, cv2.THRESH_BINARY)
    mask = thresh//255
    return mask, cv2.bitwise_not(mask)//255