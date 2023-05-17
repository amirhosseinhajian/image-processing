import numpy as np
import cv2
from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel
from my_image_proccecing_functions import assign_body_part_landmarks, crop_body_part

def zoom_effect(landmarks, coordinates):
    result = crop_body_part(landmarks, img)
    big_result = cv2.resize(result, (0, 0), fx=2, fy=2)
    w, h, z = big_result.shape 
    start_x = int(coordinates[1])-w//2 -w//4
    end_x = start_x + w
    start_y = int(coordinates[0])-h//4
    end_y = start_y + h
    _, mask = cv2.threshold(big_result, 1, 255, cv2.THRESH_BINARY)
    not_mask = cv2.bitwise_not(mask)
    mask = mask // 255
    not_mask = not_mask // 255
    img[start_x:end_x, start_y:end_y] = mask * big_result + not_mask*img[start_x:end_x, start_y:end_y]

fd = UltraLightFaceDetecion("weights/RFB-320.tflite", conf_threshold=0.88)
fa = CoordinateAlignmentModel("weights/coor_2d106.tflite")
img = cv2.imread("./input/ja.jpg")
color = (0, 0, 255)
boxes, scores = fd.inference(img)
for pred in fa.get_landmarks(img, boxes):
    # for i, p in enumerate(np.round(pred).astype(np.int)):
    #     cv2.circle(img, tuple(p), 1, color, 1, cv2.LINE_AA)
    #     cv2.putText(img, str(i), tuple(p), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 255))
    lips_landmarks = []
    left_eye_landmarks = []
    right_eye_landmarks = []
    lips_landmarks = assign_body_part_landmarks(lips_landmarks, [52, 55, 56, 53, 59, 58, 61, 68, 67, 71, 63, 64], pred) 
    left_eye_landmarks = assign_body_part_landmarks(left_eye_landmarks, [35, 36, 33, 37, 39, 42, 40, 41], pred)
    right_eye_landmarks = assign_body_part_landmarks(right_eye_landmarks, [89, 90, 87, 91, 93, 96, 94, 95], pred)

zoom_effect(lips_landmarks, np.round(pred[52]).astype(np.int))
zoom_effect(left_eye_landmarks, np.round(pred[35]).astype(np.int))
zoom_effect(right_eye_landmarks, np.round(pred[89]).astype(np.int))
cv2.imwrite("./output/big_lip_eyes.jpg", img)