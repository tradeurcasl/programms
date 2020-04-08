import cv2, time, pandas
from datetime import datetime

first_frame = None

video=cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    status = 0
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0) #removing "noise" in pic

    if first_frame is None:
        first_frame=gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray) #compairing static back with real-time image
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    cv2.imshow("Gray frame", gray)
    cv2.imshow("Delta", delta_frame)