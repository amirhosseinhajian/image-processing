#----- Thihs program finds white contours in image -----

import numpy as np
import cv2

def find_white_contours(image):
    _, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    contours = []
    visited = np.zeros_like(thresh)
    for i in range(thresh.shape[0]):
        for j in range(thresh.shape[1]):
            if thresh[i,j] == 255 and visited[i,j] == 0:
                contour = []
                stack = [(i,j)]
                visited[i,j] = 1
                while len(stack) > 0:
                    x,y = stack.pop()
                    contour.append((x,y))
                    for dx,dy in [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(1,-1),(-1,1),(1,1)]:
                        nx,ny = x+dx,y+dy
                        if nx >= 0 and nx < thresh.shape[0] and ny >= 0 and ny < thresh.shape[1]:
                            if thresh[nx,ny] == 255 and visited[nx,ny] == 0:
                                stack.append((nx,ny))
                                visited[nx,ny] = 1
                contours.append(np.array(contour))
    return contours
    
# ------------ TEST FUNCTION  ------------ 
img = cv2.imread("./inputs/dice2.png", 0)
contours = find_white_contours(img)
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    img = cv2.rectangle(img, (y, x), (y+h, x+w), 255, 2)
cv2.imwrite("./outputs/cnts.jpg", img)