import cv2

img = cv2.imread("./inputs/female.jpg", 0)
vid = cv2.VideoCapture(0)
while(True):
    ret, frame = vid.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img [300:530, 300:500] = frame[40:270, 220:420]
    cv2.imshow('frame', img)
    print(frame.shape)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print(img.shape)
vid.release()
cv2.destroyAllWindows()