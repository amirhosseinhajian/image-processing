import cv2

def put_sticker(frame, sticker, body_part):
    x, y, w, h = body_part
    overlay = cv2.resize(sticker, (w, h))
    h, w = overlay.shape[:2]
    alpha_s = overlay[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha_s
    for c in range(0, 3):
        frame[y:h+y, x:w+x, c] = (alpha_s * overlay[:, :, c] + alpha_l * frame[y:h+y, x:w+x, c])
    return frame

def put_glasses(frame, glasses_img, eyes):
    if eyes[0][0] > eyes[1][0]:
        [eyes[0], eyes[1]] = [eyes[1], eyes[0]]
    x1, y1, w1, h1 = eyes[0]
    x2, y2, w2, h2 = eyes[1]
    w, h = max(y1+h1, y2+h2)//2, (x2+w2-x1)//2
    overlay = cv2.resize(glasses_img, (w, h))
    alpha_s = overlay[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha_s
    for c in range(0, 3):
        frame[y1:h+y1, x1:w+x1, c] = (alpha_s * overlay[:, :, c] + alpha_l * frame[y1:h+y1, x1:w+x1, c])
    return frame

def detect_on_face(face, frame_gray, cascade):
    x, y, w, h = face
    detected = cascade.detectMultiScale(frame_gray[y:y+h, x:x+w], 1.3)
    result = []
    for sx,sy,sw,sh in detected:
        result.append((sx+x, sy+y, sw, sh))
    return result

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
smile_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")
joker = cv2.imread("./source_images/jokerpng.parspng.com-12-300x300.png", cv2.IMREAD_UNCHANGED)
glasses = cv2.imread("./source_images/glasses.png", cv2.IMREAD_UNCHANGED)
lip_img = cv2.imread("./source_images/lip.png", cv2.IMREAD_UNCHANGED)
vid = cv2.VideoCapture(0)
while(True):
    ret, frame = vid.read()
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if key == ord("1"):
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        for face in faces:
            put_sticker(frame, joker, face)
    elif key == ord("2"):
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        for face in faces:
            lips = detect_on_face(face, gray, smile_detector)
            eyes = detect_on_face(face, gray, eye_detector)
            for lip in lips:
                put_sticker(frame, lip_img, lip)
            if len(eyes)%2==0:
                for i in range(0, len(eyes), 2):
                    put_glasses(frame, glasses, [eyes[i], eyes[i+1]])
    elif key == ord("3"):
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        for face in faces:
            x, y, w, h = face
            face_image = frame[y:y+h, x:x+w]
            face_image_small = cv2.resize(face_image, [10, 10])
            face_image_big = cv2.resize(face_image_small, [w, h], interpolation=cv2.INTER_NEAREST)
            frame[y:y+h, x:x+w] = face_image_big
    elif key == ord("4"):
        x, y, z = frame.shape
        frame[:, y//2:, :] = frame[:, y//2:0:-1, :]
    cv2.imshow("Face Filter", frame)
vid.release()
cv2.destroyAllWindows()