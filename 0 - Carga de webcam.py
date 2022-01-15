import cv2

# Parametros de Width y Height para el video
frame_width = 1280
frame_height = 720

# Carga de webcam
cap = cv2.VideoCapture(0)  # Webcam ID = 0

cap.set(3, frame_width)  # Setting Width
cap.set(4, frame_height)  # Setting Height

while True:
    _, frame = cap.read()  # Lectura de los frames
    cv2.imshow('Webcam', frame)  # Visualización de cada frame
    if cv2.waitKey(1) == ord('q'):  # Presionar "Q" para salir
        break

cap.release()  # Libera la camara
cv2.destroyAllWindows()