import cv2
import numpy as np

# Carga de webcam
cap = cv2.VideoCapture(0)  # Webcam ID = 0

while True:
    _, frame = cap.read()

    width = int(cap.get(3))  # 3 = widht
    height = int(cap.get(4))  # 4 = height

    image = np.zeros(frame.shape, np.uint8)  # Nueva imagen
    mini_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)  # Mini frame
    image[:height//2, :width//2] = cv2.rotate(mini_frame, cv2.ROTATE_180)  # top left
    image[height//2:, :width//2] = mini_frame  # bottom left
    image[:height//2, width//2:] = cv2.rotate(mini_frame, cv2.ROTATE_180)  # top right
    image[height//2:, width//2:] = mini_frame  # bottom right

    cv2.imshow('frame', image)  # Visualización de cada frame

    if cv2.waitKey(1) == ord('q'):  # Presionar "Q" para salir
        break

cap.release()  # Libera la camara
cv2.destroyAllWindows()