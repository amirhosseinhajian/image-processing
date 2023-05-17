import cv2
from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel
from my_image_proccecing_functions import assign_body_part_landmarks, crop_body_part

def fruit_filter(landmarks, coordinates):
    result = crop_body_part(landmarks, img)
    smal_result = cv2.resize(result, (0, 0), fx=0.5, fy=0.5)
    w, h, z = smal_result.shape
    gray = cv2.cvtColor(smal_result, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
    not_mask = cv2.bitwise_not(mask)
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    not_mask = cv2.cvtColor(not_mask, cv2.COLOR_GRAY2BGR)
    mask = mask // 255
    not_mask = not_mask // 255
    start_x = coordinates[0]
    end_x = start_x+w
    start_y = coordinates[1]
    end_y = start_y+h
    peach_img[start_x:end_x, start_y:end_y] = mask*smal_result + not_mask*peach_img[start_x:end_x, start_y:end_y]

fd = UltraLightFaceDetecion("weights/RFB-320.tflite", conf_threshold=0.88)
fa = CoordinateAlignmentModel("weights/coor_2d106.tflite")
img = cv2.imread("./input/woman.jpg")
peach_img = cv2.imread("./input/peach.jpg")
color = (0, 0, 255)
boxes, scores = fd.inference(img)
for pred in fa.get_landmarks(img, boxes):
    # for i, p in enumerate(np.round(pred).astype(np.int)):
    #     cv2.circle(img, tuple(p), 1, color, 1, cv2.LINE_AA)
    #     cv2.putText(img, str(i), tuple(p), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0))
    lips_landmarks = []
    left_eye_landmarks = []
    right_eye_landmarks = []
    lips_landmarks = assign_body_part_landmarks(lips_landmarks, [52, 64, 63, 71, 67, 68, 69, 58, 59, 53, 56, 55], pred) 
    left_eye_landmarks = assign_body_part_landmarks(left_eye_landmarks, [35, 41, 40, 42, 39, 37, 33, 36], pred)
    right_eye_landmarks = assign_body_part_landmarks(right_eye_landmarks, [89, 95, 94, 96, 93, 91, 87, 90], pred)
    fruit_filter(lips_landmarks, [520, 265])
    fruit_filter(left_eye_landmarks, [370, 240])
    fruit_filter(right_eye_landmarks, [370, 370])
cv2.imwrite("./output/fruit_filter.jpg", peach_img)