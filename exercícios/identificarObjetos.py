import cv2
import mediapipe as mp

# Carregar o modelo de detecção de objetos do MediaPipe
mp_object_detection = mp.solutions.objectron
mp_drawing = mp.solutions.drawing_utils
objectron = mp_object_detection.Objectron()

# Inicializar a câmera
cap = cv2.VideoCapture(1)

while cap.isOpened():
    # Capturar quadro da câmera
    ret, frame = cap.read()
    if not ret:
        break

    # Converter o quadro para RGB (MediaPipe usa imagens RGB)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Executar a detecção de objetos
    results = objectron.process(frame_rgb)

    # Desenhar os resultados no quadro original
    if results.detected_objects:
        for detected_object in results.detected_objects:
            mp_drawing.draw_landmarks(frame, detected_object.landmarks_2d, mp_object_detection.BOX_CONNECTIONS)
            mp_drawing.draw_axis(frame, detected_object.rotation, detected_object.translation)

    # Exibir o quadro com os resultados
    cv2.imshow("Object Detection", frame)

    # Checar se a tecla 'q' foi pressionada para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar a captura e fechar as janelas
cap.release()
cv2.destroyAllWindows()
