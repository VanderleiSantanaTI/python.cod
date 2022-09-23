import cv2

webCamera = cv2.VideoCapture(2)
classificadorVideoFace = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    camera, frame = webCamera.read()
    cv2.imshow('video', frame)


    if cv2.waitKey(1) == ord('f'):
        break