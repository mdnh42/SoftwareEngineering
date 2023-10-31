import cv2 
cam = cv2.VideoCapture(2)

while True:
    _, frame = cam.read()
    cv2.imshow('my Cam', frame)
    cv2.waitkey(1)