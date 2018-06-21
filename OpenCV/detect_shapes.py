from collections import deque
import numpy as np
import argparse
import imutils
import cv2
from pyimagesearch.shapedetector import ShapeDetector
from time import time

xrange = range

ap = argparse.ArgumentParser()
ap.add_argument("-b", "--buffer", type=int, default=64,
                help="max buffer size")
args = vars(ap.parse_args())

#Границы определяемого цвета
greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)

#Buffer для trace (линия перемещения центра)
pts = deque(maxlen=args["buffer"])

#Включение видеозахвата
camera = cv2.VideoCapture(0)

while True:

    #Захват кадра
    (grabbed, frame) = camera.read()
    #Resize кадра
    frame = imutils.resize(frame, width=600)

    #The function transforms a grayscale image to a binary image
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Checks if array elements lie between the elements of two other arrays.
    mask = cv2.inRange(hsv, greenLower, greenUpper)
    #Erodes an image by using a specific structuring element.
    mask = cv2.erode(mask, None, iterations=2)
    #Dilates an image by using a specific structuring element.
    mask = cv2.dilate(mask, None, iterations=2)

    #Находим контуры
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None
    sd = ShapeDetector()
    b = time()
    if len(cnts) > 0:
        #Находим наибольший контур
        c = max(cnts, key=cv2.contourArea)
        #Узнаем тип фигуры
        shape = sd.detect(c)
        #Находим минимальный круг, описывающий наш контур
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        if shape is 'circle' and radius >20:
            #Находим моменты изображения
            M = cv2.moments(c)
            #Находим центр контура
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

            if radius > 10:
                cv2.circle(frame, center, 5, (0, 0, 255), -1)

            #Записываем положение центра в Buffer
            pts.appendleft(center)

            #Рисуем trace
            for i in xrange(1, len(pts)):

                if pts[i - 1] is None or pts[i] is None:
                    continue

                thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
                cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)
                cv2.putText(frame, '{}: R = {}'.format(shape,int(radius)), (center[0], center[1]), cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, (255, 255, 255), 2)

            #Рисуем контур
            cv2.drawContours(frame, c, -1, (0, 255, 0), 3)


    print(time() - b)
    #Показываем изображение
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break
camera.release()
cv2.destroyAllWindows()
