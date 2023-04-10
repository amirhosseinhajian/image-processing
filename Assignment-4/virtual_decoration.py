import cv2
import numpy as np

main_decoration = cv2.imread("./source_images/room_background.jpg").astype(np.float32)
new_forground = cv2.imread("./source_images/room_foreground.jpg").astype(np.float32)
mask = cv2.imread("./source_images/room_mask.jpg") / 255
result = np.multiply(new_forground, mask)
result = np.add(result, np.multiply(main_decoration, 1-mask)).astype(np.uint8)
cv2.imwrite("./outputs/virtual_decoration.jpg", result)