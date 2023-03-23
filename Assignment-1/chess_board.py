from math import floor
import cv2
import numpy as np

colors = [0, 255]
colors_swaped = [255, 0]
chess_board = [[np.uint8(colors[floor(j/90)%2]) if floor(i/90)%2==0 else np.uint8(colors_swaped[floor(j/90)%2]) for i in range(720)] for j in range(720)]
chess_board = np.array(chess_board)
cv2.imshow("", chess_board)
cv2.imwrite('./processed images/chess_board.png', chess_board)
cv2.waitKey()