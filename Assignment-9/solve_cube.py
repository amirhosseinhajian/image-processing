import cv2
import numpy as np

cube = cv2.imread('./inputs/cube.jpg')
for i, row in enumerate(cube):
    for j, pixle in enumerate(row):
        b, g, r = cube[i][j]
        if b>128 and g>128 and r>128:
            continue
        if b>128 and g>128:
            cube[i][j] = np.array((0, 0, 255))
        elif b>128 and r>128:
            cube[i][j] = np.array((0, 255, 0))
        elif g>128 and r>128:
            cube[i][j] = np.array((255, 0, 0))
cv2.imwrite("./outputs/cube.jpg", cube)