import cvzone
import cv2 as cv
import numpy as np
keys = [['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
        ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ':'],
        ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '?']]

"""Fungsi ngambil koordinat besar kotak untuk gambar"""
size = 80/ 100
buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        x = int((j * 120 * size) + 60)
        y = int((i * 120 * size) + 120)
        h = int(x + 110 * size)
        w = int(y + 110 * size)
        buttonList.append([x, y, h, w, key])


def S_keys():
    xs = lambda i: int((i * 120 * size) + 60)
    ys = lambda y: int((y * 120 * size) + 120)
    hws = lambda hw: int(hw + 110 * size)
    buttonList.append([xs(0), ys(len(keys)), hws(xs(3)), hws(ys(len(keys))), 'backspace'])
    buttonList.append([xs(4), ys(len(keys)), hws(xs(6.5)), hws(ys(len(keys))), 'capslock'])
    buttonList.append([xs(7.5), ys(len(keys)), hws(xs(9)), hws(ys(len(keys))), 'enter'])
    buttonList.append([xs(1), ys(len(keys) + 1), hws(xs(8)), hws(ys(len(keys) + 1)), ' '])


S_keys()

"""Gambar Keyboardnya"""


def drawKey(img, buttonList):

    imgNew = np.zeros_like(img, np.uint8)

    for x, y, h, w, key in buttonList:
        cv.rectangle(imgNew, (x-9, y-9), (h+9, w+9), (255, 255, 0), cv.FILLED)
        cv.rectangle(imgNew, (x, y), (h, w), (255, 255, 255), cv.FILLED)
        cv.putText(imgNew, key, (x + 16, y + 60), cv.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)

    out = img.copy()
    alpha = 0.4
    mask = imgNew.astype(bool)
    print(img.shape)
    out = cv.addWeighted(imgNew, alpha, img, 1 - alpha, 0)
    return out
