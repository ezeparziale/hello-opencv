import cv2
from utils.concatenar_imagen import concat_tile_resize


# Carga
img_1 = cv2.imread("img/image_0.jpg")
img_2 = cv2.imread("img/image_1.jpg")

# Lista de imagenes a concatenar
img_concat = concat_tile_resize(
    [
        [img_1],
        [img_1, img_2, img_1],
        [img_1, img_2],
    ]
)

# Visualización
cv2.imshow("Imagenes concatenadas", img_concat)

cv2.waitKey(0)  # Espera hasta que se presione una tecla para cerrar
cv2.destroyAllWindows()
