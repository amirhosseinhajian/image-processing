import numpy as np
import cv2

def decrypt(cipher_img_path, secret_key_path):
    cipher_img = cv2.imread(cipher_img_path)
    secret_key = np.load(secret_key_path)
    decrypt_img = cipher_img - secret_key
    cv2.imwrite("./outputs/decrypted.jpg", decrypt_img)