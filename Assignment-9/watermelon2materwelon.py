import cv2

watermelon = cv2.imread('./inputs/watermelon.jpg')
materwelon = watermelon.copy()
materwelon[:, :, 1] = watermelon[:, :, 2]
materwelon[:, :, 2] = watermelon[:, :, 1]
cv2.imwrite("./outputs/materwelon.jpg", materwelon)