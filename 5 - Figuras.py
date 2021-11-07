import cv2
import numpy as np

# Carga de webcam
cap = cv2.VideoCapture(0)  # Webcam ID = 0

while True:
    ret, frame = cap.read()

    width = int(cap.get(3))  # 3 = widht
    height = int(cap.get(4))  # 4 = height

    # Lineas
    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
    img = cv2.line(frame, (0, height), (width, 0), (0, 255, 0), 10)

    # Rectangulos
    img = cv2.rectangle(frame, (100, 100), (200, 200), (128, 128, 0), -1)

    # Circulos
    img = cv2.circle(frame, (300, 300), 50, (0, 0, 255), -1)

    # Texto
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(frame, 'Hello opencv', (0, height-50), font, 2, (0, 0, 0), 5, cv2.LINE_AA)

    cv2.imshow('frame', frame)  # Visualización de cada frame

    if cv2.waitKey(1) == ord('q'):  # Presionar "Q" para salir
        break

cap.release()  # Libera la camara
cv2.destroyAllWindows()