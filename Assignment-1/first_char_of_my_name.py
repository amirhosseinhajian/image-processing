import cv2
import numpy as np

my_name = np.zeros((480, 480), np.uint8)
image_mid_len = int(len(my_name)/2)
j=0
for i in range(120, 360, 10):
    my_name[i:i+10, image_mid_len-5-j:image_mid_len+5-j] = 255
    my_name[i:i+10, image_mid_len-5+j:image_mid_len+5+j] = 255
    j+=6
my_name[240:250, 170:310] = 255
cv2.imwrite("./processed images/my_first_char.jpg", my_name)