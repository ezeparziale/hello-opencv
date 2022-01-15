import cv2

# Parametros
frame_width = 960
frame_height = 540

# Carga de video
cap = cv2.VideoCapture('videos/new_york.mp4')

while True:
    _, frame = cap.read()  # Lectura de los frames
    frame = cv2.resize(frame, (frame_width, frame_height))  # Resize del video si es necesario
    cv2.imshow("Video", frame)  # Visualización de cada frame
    if cv2.waitKey(1) & cv2.waitKey(1) == ord('q'):  # Presionar "Q" para salir
        break

cap.release()  # Libera el video
cv2.destroyAllWindows()
 