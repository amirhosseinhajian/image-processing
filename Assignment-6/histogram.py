import cv2
import numpy as np
import matplotlib.pyplot as plt

def draw_chart(chart, hist, bins, range):
    if chart == 'hist':
        plt.hist(hist, bins=bins, range=range)
    elif chart == 'bar':
        plt.bar(np.arange(256), hist)
    else:
        plt.plot(hist)
    plt.title("Histogram Cahrt")
    plt.xlabel("Intensity value")
    plt.ylabel("count")
    plt.show()

def calculate_histogram(img):
    histogram = np.zeros((256), dtype=np.uint)
    for row in img:
        for col in row:
            for z in col:
                histogram[z] += 1
    return histogram

img = cv2.imread("./inputs/ship-moon.jpg")
histogram = calculate_histogram(img)
draw_chart('plot', histogram, 0, 0)
draw_chart('hist', img.ravel(), 256, [0, 256])
draw_chart('bar', histogram, 0, 0)