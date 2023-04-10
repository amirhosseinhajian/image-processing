import os
import cv2
import numpy as np

def read_images(images_path, directory_series):
    images = []
    for image_path in images_path:
        img = cv2.imread("./source_images/black_hole/" + directory_series + "/" + image_path).astype(np.float32)
        images.append(img)
    return images

def reduce_noise(images):
    return np.mean(images, axis=0).astype(np.uint8)

img_serries_1 = reduce_noise(read_images(os.listdir("./source_images/black_hole/1"), "1"))
img_serries_2 = reduce_noise(read_images(os.listdir("./source_images/black_hole/2"), "2"))
img_serries_3 = reduce_noise(read_images(os.listdir("./source_images/black_hole/3"), "3"))
img_serries_4 = reduce_noise(read_images(os.listdir("./source_images/black_hole/4"), "4"))
result = np.concatenate((np.concatenate((img_serries_1, img_serries_2), axis=1), np.concatenate((img_serries_3, img_serries_4), axis=1)))
cv2.imwrite("./outputs/black_hole.jpg", result)