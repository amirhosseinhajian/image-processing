import cv2
import numpy as np

rainbow = np.ones([720, 1280, 3], dtype=np.uint8)*255
cv2.circle(rainbow, (600, 640), 150, (133, 0, 141), 40)
cv2.circle(rainbow, (600, 640), 190, (255, 0, 0), 40)
cv2.circle(rainbow, (600, 640), 230, (255, 250, 0), 40)
cv2.circle(rainbow, (600, 640), 270, (0, 130, 0), 40)
cv2.circle(rainbow, (600, 640), 310, (0, 255, 255), 40)
cv2.circle(rainbow, (600, 640), 350, (0, 160, 255), 40)
cv2.circle(rainbow, (600, 640), 390, (0, 0, 255), 40)
rainbow[601:, :] = 255
cv2.imwrite("./outputs/rainbow.jpg", rainbow)