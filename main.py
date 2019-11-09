import cv2
import numpy as np


def line(file, value, t):
    img = cv2.imread(file, 1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (0, 0, value - t), (0, 0, value + t))
    res = cv2.bitwise_and(img, img, mask=mask)
    take = cv2.multiply(res, res)
    for n in range(1,3):
        take = cv2.multiply(take, take)
    return take

threshold = 0.01
path = 'golan_data Height Map (Merged).png'
layers = 30

blank = np.zeros((1081, 1081, 3), np.uint8)
cv2.imwrite('origin.png', blank)

for n in range(0, 255, int(255/layers)):
    blank = cv2.bitwise_or(blank, line(path, n, threshold))

blur = cv2.blur(blank, (2, 2))
final = cv2.bitwise_not(blur)
cv2.imwrite('output.png', final)
