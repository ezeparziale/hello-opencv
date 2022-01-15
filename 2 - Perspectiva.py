import cv2
import numpy as np

# Carga
img = cv2.imread("img/cartel_0.jpg")

# Parametros imagen
width, height = 800, 600

# Puntos de la imagen a transformar
input_points = np.float32([[375, 205], [638, 231], [375, 367], [627, 381]])
output_points = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

# Aplicar transformación de perspectiva
matrix = cv2.getPerspectiveTransform(input_points, output_points)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

# Visualización
cv2.imshow("Image orignal", img)
cv2.imshow("Cartel", imgOutput)

cv2.waitKey(0)  # Espera hasta que se presione una tecla para cerrar
cv2.destroyAllWindows()
