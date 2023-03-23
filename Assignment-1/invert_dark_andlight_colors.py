import cv2

def invert(img, export_name):
    for i, x in enumerate(img):
        for j, y in enumerate(x):
            for k, z in enumerate(y):
                img[i, j, k] = 255 - img[i, j, k]
    cv2.imwrite(f"./processed images/{export_name}.jpg", img)

invert(cv2.imread("./source images/1.jpg"), "1")
invert(cv2.imread("./source images/2.jpg"), "2")