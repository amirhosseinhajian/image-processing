import cv2
import imageio

def set_frame(frame):
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
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(frame_hsv)
    obj = {
        'red': countInRange(h, 0, 10),
        'green': countInRange(h, 50, 75),
        'blue': countInRange(h, 105, 150),
        'yellow': countInRange(h, 25, 55),
        'orange': countInRange(h, 10, 30),
        'purple': countInRange(h, 145, 160),
        'white': countInRange(s, 0, 30),
        'black': countInRange(v, 0, 30),
           }
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
    preset_frame = cv2.cvtColor(preset_frame, cv2.COLOR_BGR2RGB)
    gif_frames.append(preset_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()
imageio.mimsave('./outputs/color detector.gif', gif_frames, duration=0.1)