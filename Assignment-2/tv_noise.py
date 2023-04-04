import copy
import cv2
import numpy as np
import imageio

tv_img = cv2.imread("./source images/tv.jpg")
frames = [copy.deepcopy(tv_img) for _ in range(10)]
for frame in frames:
    new_noise = np.random.random((197, 352, 3)) * 255
    new_noise = np.array(new_noise, dtype=np.uint8)
    frame[251:448, 198:550] = new_noise
imageio.mimsave('./processed_images/tvnoise.gif', frames, duration=0.08)