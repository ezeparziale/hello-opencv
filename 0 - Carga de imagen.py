import cv2

# Carga
img = cv2.imread('img/image_0.jpg')

# Visualización
cv2.imshow('Imagen', img)
cv2.waitKey(0)  # Espera hasta que se presione una tecla para cerrar
cv2.destroyAllWindows()