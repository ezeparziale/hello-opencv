import cv2
import random

# Carga
img = cv2.imread('img/image_1.jpg', cv2.IMREAD_COLOR)
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# Valores internos
print(img)

# Tipo numpy
print(type(img))

print(img.shape)  # (HEIGHT, WIDTH, CHANNELS)

# Remplazando pixeles
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

# Visualización
cv2.imshow('Image1', img)
cv2.waitKey(0)  # Espera hasta que se presione una tecla para cerrar
cv2.destroyAllWindows()