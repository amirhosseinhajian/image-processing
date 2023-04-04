import copy
import random
import cv2
import imageio

landscape_img = cv2.imread("./source images/snow_landscape.jpg")
width, height, z = landscape_img.shape
frames = [copy.deepcopy(landscape_img) for _ in range(100)]
snows = [(random.randint(0, height), random.randint(-729, width)) for _ in range(2000)]
for i, frame in enumerate(frames):
    for snow in snows:
        cv2.circle(frame, (snow[0], snow[1]+i*8), 1, (255, 255, 255), -1)
imageio.mimsave('./processed_images/snowfall landscape.gif', frames, duration=0.1)