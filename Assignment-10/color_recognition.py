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
    black_b = countInRange(frame[:,:,0], 0, 10)
    black_g = countInRange(frame[:,:,1], 0, 10)
    black_r = countInRange(frame[:,:,2], 0, 10)
    white_b = countInRange(frame[:,:,0], 127, 255)
    white_g = countInRange(frame[:,:,1], 127, 255)
    white_r = countInRange(frame[:,:,2], 127, 255)
    obj = {
        'red': black_b + black_g + white_r,
        'green': black_b + white_g + black_r,
        'blue': white_b + black_g + black_r,
        'yellow': black_b + countInRange(frame[:,:,1], 150, 255) + white_r,
        'orange': black_b + countInRange(frame[:,:,1], 85, 180) + white_r,
        'purple': countInRange(frame[:,:,0], 85, 140) + black_g + countInRange(frame[:,:,2], 85, 140),
        'white': white_b + white_g + white_r,
        'black': black_b + black_g + black_r,
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