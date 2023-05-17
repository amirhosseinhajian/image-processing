import cv2
from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel
from my_image_proccecing_functions import assign_body_part_landmarks, crop_body_part

def rotate(landmarks, coordinates, offset_divide, resize_value):
    result = crop_body_part(landmarks, img)
    result_cw_180 = cv2.rotate(result, cv2.ROTATE_180)
    result_cw_180 = cv2.resize(result_cw_180, (0, 0), fx=resize_value, fy=resize_value)
    w, h, z = result_cw_180.shape
    gray = cv2.cvtColor(result_cw_180, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
    not_mask = cv2.bitwise_not(mask)
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    not_mask = cv2.cvtColor(not_mask, cv2.COLOR_GRAY2BGR)
    mask = mask // 255
    not_mask = not_mask // 255
    start_x = int(coordinates[1])-w//2
    if offset_divide != 0:
        start_x -= w//offset_divide
    end_x = start_x + w
    start_y = int(coordinates[0])
    end_y = start_y + h
    img[start_x:end_x, start_y:end_y] = mask * result_cw_180 + not_mask * img[start_x:end_x, start_y:end_y]

fd = UltraLightFaceDetecion("weights/RFB-320.tflite", conf_threshold=0.88)
fa = CoordinateAlignmentModel("weights/coor_2d106.tflite")
img = cv2.imread("./input/wensday.jpg")
color = (0, 0, 255)
boxes, scores = fd.inference(img)
for pred in fa.get_landmarks(img, boxes):
    # for i, p in enumerate(np.round(pred).astype(np.int)):
    #     cv2.circle(img, tuple(p), 1, color, 1, cv2.LINE_AA)
    #     cv2.putText(img, str(i), tuple(p), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0))
    lips_landmarks = []
    left_eye_landmarks = []
    right_eye_landmarks = []
    lips_landmarks = assign_body_part_landmarks(
    lips_landmarks, [52, 64, 63, 71, 67, 68, 69, 58, 59, 53, 56, 55], pred)
    left_eye_landmarks = assign_body_part_landmarks(left_eye_landmarks, [35, 41, 40, 42, 39, 37, 33, 36], pred)
    right_eye_landmarks = assign_body_part_landmarks(right_eye_landmarks, [89, 95, 94, 96, 93, 91, 87, 90], pred)
    rotate(lips_landmarks, pred[52], 0, 1.19)
    rotate(left_eye_landmarks, pred[35], 0, 1.08)
    rotate(right_eye_landmarks, pred[89], 6, 1.09)

cv2.imwrite("./output/magic_filter.jpg", img = cv2.rotate(img, cv2.ROTATE_180))