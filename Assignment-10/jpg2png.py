import cv2

img = cv2.imread("./inputs/microsoft.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
filter_arr = img % 2 == 0
for i, row in enumerate(img):
    for j, pixle in enumerate(row):
        b, g, r, a = img[i][j]
        if 70<b<100 and 70<g<100 and 70<r<100:
            img[i][j][3] = 0
cv2.imwrite("./outputs/microsof_logo.png", img)