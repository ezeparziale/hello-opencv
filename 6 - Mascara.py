import cv2
import numpy as np

# Carga de webcam
cap = cv2.VideoCapture(0)  # Webcam ID = 0

while True:
    _, frame = cap.read()

    width = int(cap.get(3))  # 3 = widht
    height = int(cap.get(4))  # 4 = height

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([110, 50, 50])  # Rango minimo
    upper_blue = np.array([130, 255, 255])  # Rango maximo

    mask = cv2.inRange(hsv, lower_blue, upper_blue)  # Mascara con rango de colores

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', result)  # Visualización de cada frame
    cv2.imshow('mask', mask)  # Visualización mascara

    if cv2.waitKey(1) == ord('q'):  # Presionar "Q" para salir
        break

cap.release()  # Libera la camara
cv2.destroyAllWindows()