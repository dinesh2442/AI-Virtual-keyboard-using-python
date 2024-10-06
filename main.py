import cv2 as cv
import mediapipe as mp
import pyautogui as pg
from keys import *
import numpy as np
import pygame


def BeepOn():
    pygame.mixer.init()
    pygame.mixer.music.load('kc.wav')
    pygame.mixer.music.play(loops=0)
    pygame.mixer.music.set_volume(0.50)


cam = cv.VideoCapture(0)
cam.set(3, 1280)
cam.set(4, 720)

mphands = mp.solutions.hands
hands = mphands.Hands()
clk = 1

while True:
    succes, img = cam.read()
    img = cv.flip(img, 1)

    h, w, c = img.shape

    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    result = hands.process(imgRGB)
    img = drawKey(img, buttonList)
    if (result.multi_hand_landmarks):
        lmlist = []
        for handsLms in result.multi_hand_landmarks:
            for id, landmarks in enumerate(handsLms.landmark):
                x, y = int(landmarks.x * w), int(landmarks.y * h)
                lmlist.append([id, x, y])

        X = lmlist[8][1]
        Y = lmlist[8][2]
        cv.circle(img, (X, Y), 15, (0, 255, 255), cv.FILLED)

        # X = lmlist[8][1]
        # Y = lmlist[8][2]
        # for x, y, h, w, keys in buttonList:
        # if x < X < h and y < Y < w:
        # cv.rectangle(img, (x-5, y-5), (h+5, w+5), (0, 0, 0), cv.FILLED)

        """Klik"""
        if (lmlist[11][2] > lmlist[12][2]) and ((clk > 0)):

            cv.circle(img, (X, Y), 20, (0, 255, 0), cv.FILLED)

            for x, y, h, w, keys in buttonList:
                if x < X < h and y < Y < w:
                    cv.rectangle(img, (x, y), (h, w), (0, 0, 255), cv.FILLED)

                    BeepOn()
                    pg.press(keys)

            clk = -1

        elif (lmlist[11][2] < lmlist[12][2]):

            clk = 1

    # drawKey(img, buttonList)

    cv.imshow("webcam", img)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

cv.destroyAllWindows()