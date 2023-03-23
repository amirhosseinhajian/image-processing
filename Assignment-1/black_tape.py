import cv2

img = cv2.imread("./source images/Escape to the moon2432_rectangle.jpg")
for i in range(450):
    img[i, 500-i-50:500-i+50] = 0
for i in range(100):
    img[450+i, 0:100-i] = 0
cv2.imwrite("./processed images/black_tape.jpg", img)