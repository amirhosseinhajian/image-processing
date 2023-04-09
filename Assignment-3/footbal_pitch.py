import cv2
import numpy as np

border_color = (255, 255, 255)
pitch = np.zeros((400, 600, 3), np.uint8)
for i in range(0, 6, 2):
    cv2.rectangle(pitch, (i*100, 0), ((i+1)*100, 400), (0, 175, 0), -1)
    cv2.rectangle(pitch, ((i+1)*100, 0), ((i+2)*100, 400), (0, 135, 0), -1)
cv2.rectangle(pitch, (20, 20), (580, 380), border_color, 2)
cv2.line(pitch, (300, 20), (300, 380), border_color, 2)
cv2.circle(pitch, (300, 200), 65, border_color, 2)
cv2.circle(pitch, (300, 200), 5, border_color, -1)
cv2.rectangle(pitch, (20, 160), (65, 240), border_color, 2)
cv2.rectangle(pitch, (20, 120), (110, 280), border_color, 2)
cv2.rectangle(pitch, (535, 160), (580, 240), border_color, 2)
cv2.rectangle(pitch, (490, 120), (580, 280), border_color, 2)
cv2.imwrite("./processed_images/footbal_pitch.jpg", pitch)