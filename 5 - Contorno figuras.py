import cv2
import numpy as np
from utils.concatenar_imagen import concat_tile_resize


def get_contorno(img_original, img_canny):
    img_aux = img_original.copy()
    contours, _ = cv2.findContours(img_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        cv2.drawContours(img_aux, cnt, -1, (5, 226, 247), 3)
        # perimetro = cv2.arcLength(cnt, True)
        # approx = cv2.approxPolyDP(cnt, 0.02 * perimetro, True)
        # x, y, w, h = cv2.boundingRect(approx)
        # cv2.rectangle(img_aux, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return img_aux

# Carga
path = "img/figuras_0.png"
img = cv2.imread(path)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7, 7), 1)
img_canny = cv2.Canny(img_blur, 50, 50)
img_contour = get_contorno(img, img_canny)

# Reshape
img_gray = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2RGB)
img_blur = cv2.cvtColor(img_blur, cv2.COLOR_GRAY2RGB)
img_canny = cv2.cvtColor(img_canny, cv2.COLOR_GRAY2RGB)

# Visualización
cv2.imshow(
    "Figuras",
    concat_tile_resize([[img], [img_gray], [img_blur], [img_canny], [img_contour]]),
)
cv2.waitKey(0)  # Espera hasta que se presione una tecla para cerrar
cv2.destroyAllWindows()
