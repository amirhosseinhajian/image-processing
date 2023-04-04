import cv2
import imageio

def set_frame(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.rectangle(frame, (100, 200), (200, 300), 0, 4)
    blured_frame = cv2.GaussianBlur(frame, (41, 41), 0)    
    blured_frame[200:300, 100:200] = frame[200:300, 100:200]
    return blured_frame

def countInRange(arr, first, end):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if (arr[i][j] >= first and arr[i][j] <= end):
                count += 1
    return count

def detect_color(frame):
    obj = {"black": countInRange(frame, 0, 45),
           "gray": countInRange(frame, 86, 120),
           "white": countInRange(frame, 130, 255)}
    max_key = max(obj, key=obj.get)
    return max_key

gif_frames = []
vid = cv2.VideoCapture(0)
while(True):
    ret, frame = vid.read()
    preset_frame = set_frame(frame)
    color = detect_color(preset_frame[200:300, 100:200])
    cv2.putText(preset_frame, color, (20, 55), cv2.FONT_HERSHEY_PLAIN, 3, 0, 2)
    cv2.imshow('frame', preset_frame)
    gif_frames.append(preset_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()
imageio.mimsave('./processed_images/color detector.gif', gif_frames, duration=0.1)