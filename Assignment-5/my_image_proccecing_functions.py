import numpy as np
import cv2

def assign_body_part_landmarks(body_part_list, landmarks, pred):
    for i in landmarks:
        body_part_list.append(pred[i])
    return np.array(body_part_list, dtype=int)

def crop_body_part(landmarks, img):
    mask = np.zeros(img.shape, dtype=np.uint8)
    cv2.drawContours(mask, [landmarks], -1, (255, 255, 255), -1)
    mask = mask//255
    result = img*mask
    x, y, w, h = cv2.boundingRect(landmarks)
    return result[y:y+h, x:x+w]