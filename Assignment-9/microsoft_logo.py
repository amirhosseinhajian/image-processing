import cv2
import numpy as np

microsoft_logo = np.ones([720, 1280, 3], dtype=np.uint8)*85
r = np.ones((310, 310), dtype=np.uint8)*85
g = np.ones((310, 310), dtype=np.uint8)*85
b = np.ones((310, 310), dtype=np.uint8)*85
r[0:150, 0:150] = 242
g[0:150, 0:150] = 80
b[0:150, 0:150] = 34
r[0:150, 160:310] = 127
g[0:150, 160:310] = 186
b[0:150, 160:310] = 0
r[160:310, 0:150] = 0
g[160:310, 0:150] = 164
b[160:310, 0:150] = 239
r[160:310, 160:310] = 255
g[160:310, 160:310] = 185
b[160:310, 160:310] = 0
microsoft_logo[205:515, 120:430] = cv2.merge([b, g, r])
cv2.putText(microsoft_logo, 'Microsoft', (450, 400), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 255, 255), 7)
cv2.imwrite("./outputs/microsoft.jpg", microsoft_logo)