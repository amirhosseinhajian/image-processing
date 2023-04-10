import cv2

img_1 = 255 - cv2.imread("./source_images/a.png")
img_2 = 255 - cv2.imread("./source_images/b.png")
result = 255 - cv2.subtract(img_1, img_2)
cv2.imwrite("./outputs/secret_text.jpg", result)