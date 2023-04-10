import cv2

def photo_to_sketch(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inverted = 255 - img
    blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
    inverted_blured = 255 - blurred
    sketch = img/inverted_blured
    return sketch * 255
    
img = cv2.imread("./source_images/david.jpg")
sketch = photo_to_sketch(img)
cv2.imwrite("./outputs/david_sketch.jpg", sketch)