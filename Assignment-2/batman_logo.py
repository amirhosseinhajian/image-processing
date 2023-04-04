import cv2

img = cv2.imread("./source images/batman.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, img = cv2.threshold(img, 135, 255, cv2.THRESH_BINARY_INV)
cv2.putText(img, "BATMAN", (350, 515), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, 255, 2)
cv2.imwrite("./processed_images/batman.jpg", img)