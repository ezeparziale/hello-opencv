import cv2
import numpy as np

# Carga
img = cv2.imread("img/image_0.jpg")
print(img.shape)

# Corte de imagen
img_cropped = img[248:500, 250:420]  # Punto Origen y punto destino
print(img_cropped.shape)

# Visualización
cv2.imshow("Imagen original", img)
cv2.imshow("Corte de imagen", img_cropped)

cv2.waitKey(0)  # Espera hasta que se presione una tecla para cerrar
cv2.destroyAllWindows()
