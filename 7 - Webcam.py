import cv2

# Carga de webcam
cap = cv2.VideoCapture(0)  # Webcam ID = 0

while True:
    _, frame = cap.read()  # Lectura de los frames
    cv2.imshow('frame', frame)  # Visualización de cada frame
    if cv2.waitKey(1) == ord('q'):  # Presionar "Q" para salir
        break

cap.release()  # Libera la camara
cv2.destroyAllWindows()