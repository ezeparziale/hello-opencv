import cv2

# Carga
img = cv2.imread('img/image1.jpg', cv2.IMREAD_COLOR)
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# Copiando pixeles
tag = img[0:300, 0:300]  # Puntos de la zona a copiar
img[300:600, 300:600] = tag  # Puntos a reeemplazar

# Visualización
cv2.imshow('Image1', img)
cv2.waitKey(0)  # Espera hasta que se presione una tecla para cerrar
cv2.destroyAllWindows()