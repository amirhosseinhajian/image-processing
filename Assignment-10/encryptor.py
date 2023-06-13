import numpy as np
import cv2

def encrypt(img_path):
    img = cv2.imread(img_path)
    secret_key = np.random.randint(0, 256, size=[img.shape[0], img.shape[1], img.shape[2]], dtype=np.uint8)
    cipher_img = secret_key + img
    cv2.imwrite("./outputs/cipher_img.bmp", cipher_img)
    np.save("secret_key.npy", secret_key)