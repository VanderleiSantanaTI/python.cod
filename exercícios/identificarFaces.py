"""
pip install opencv-python mediapipe cvzone
Mediapipe é uma biblioteca desenvolvida pelo Google que fornece uma estrutura flexível e fácil de usar para a
construção de pipelines de processamento de mídia. É projetado principalmente para tarefas de visão computacional,
 processamento de vídeo e áudio em tempo real.

Algumas das funcionalidades oferecidas pelo Mediapipe incluem:

Detecção de Pose: Mediapipe pode detectar e rastrear as poses humanas em imagens e vídeos.

Detecção de Mãos: Ele pode identificar e rastrear mãos em tempo real, útil para aplicações como controle gestual
ou interações de realidade aumentada.

Detecção Facial: Mediapipe pode ser usado para detecção facial, identificação de pontos faciais, expressões faciais,
 e até mesmo detecção de movimento dos lábios.

Detecção de Objetos: Ele também suporta detecção de objetos em tempo real, permitindo identificar e rastrear objetos
específicos em vídeos.

Seguimento de Mão 3D: Além da detecção de mãos, o Mediapipe pode estimar a pose 3D das mãos em tempo real.

Essas são apenas algumas das funcionalidades do Mediapipe.

"""
import time

import cv2
from cvzone.FaceDetectionModule import FaceDetector

video = cv2.VideoCapture(1)
detector = FaceDetector()
print(video)

cont = 0
while True:
    _, img = video.read()

    img, bboxes = detector.findFaces(img, draw=True)
    cont += 1
    if bboxes and cont > 100:
        print("detectado")
        cont = 1


    cv2.imshow('Resultado', img)
    if cv2.waitKey(1) == 27:
        break

