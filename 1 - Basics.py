import cv2

# Carga
img = cv2.imread('img/image_1.jpg', cv2.IMREAD_COLOR)

# Tamaño
# img = cv2.resize(img, (900, 700))  # Resizing con resolución fija
img = cv2.resize(img, (0, 0), fx=0.4, fy=0.4)  # Resizing con %

# Rotación
img2 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) 

# Guardado
cv2.imwrite('export/image1.jpg', img)

# Visualización
cv2.imshow('Image1', img)
cv2.imshow('Image2', img2)
cv2.waitKey(0)  # Espera hasta que se presione una tecla para cerrar
cv2.destroyAllWindows()