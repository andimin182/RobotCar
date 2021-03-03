import cv2 as cv

import time

cam = cv.VideoCapture(0)

time.sleep(4)

_, img = cam.read()
cv.imwrite("opencv2.png", img)

del(cam)  # so that others can use the camera as soon as possible
