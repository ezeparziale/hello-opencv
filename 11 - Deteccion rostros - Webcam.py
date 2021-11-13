import numpy as np
import cv2

# Carga de webcam
cap = cv2.VideoCapture(0)  # Webcam ID = 0

# Modelos
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    _, frame = cap.read()

    # Conversión a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detección de cara
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)  # Dibujo rectangulo en cara

    # Visualización
    cv2.imshow('Webcam (Presione Q para salir)', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()