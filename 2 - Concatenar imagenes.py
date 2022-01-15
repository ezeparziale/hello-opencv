import cv2
import numpy as np

# Carga
img_1 = cv2.imread("img/image_0.jpg")
img_2 = cv2.imread("img/image_1.jpg")

# Concatenar imagenes horizontalmente y verticamente
# Las imagenes tienen que tener la misma resolución
# Las matrices deben tener las mismas dimensiones
img_horizontal = np.hstack((img_1, img_1))
img_vertical = np.vstack((img_1, img_1))

# img_horizontal = np.hstack((img_1, img_2))  # Imagenes con distintas resoluciones
# img_vertical = np.vstack((img_1, img_2))  # Imagenes con distintas resoluciones

# Visualización
cv2.imshow("Imagen horizontal", img_horizontal)
cv2.imshow("Imagen vertical", img_vertical)

cv2.waitKey(0)  # Espera hasta que se presione una tecla para cerrar
cv2.destroyAllWindows()
