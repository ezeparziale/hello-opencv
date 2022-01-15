import cv2

def hconcat_resize(img_list, interpolation=cv2.INTER_CUBIC):
    h_min = min(img.shape[0] for img in img_list)  # Minimo hights de todas las imagenes

    im_list_resize = [
        cv2.resize(
            img,
            (int(img.shape[1] * h_min / img.shape[0]), h_min),
            interpolation=interpolation,
        )
        for img in img_list
    ]  # Resizing a la minima hight

    return cv2.hconcat(im_list_resize)  # imagenes concatenadas


def vconcat_resize(img_list, interpolation=cv2.INTER_CUBIC):
    w_min = min(img.shape[1] for img in img_list)  # Minimo width de todas las imagenes

    im_list_resize = [
        cv2.resize(
            img,
            (w_min, int(img.shape[0] * w_min / img.shape[1])),
            interpolation=interpolation,
        )
        for img in img_list
    ]   # Resizing a la minima width

    return cv2.vconcat(im_list_resize)  # imagenes concatenadas


def concat_tile_resize(list_2d, interpolation=cv2.INTER_CUBIC):

    img_list_v = [
        hconcat_resize(list_h, interpolation=cv2.INTER_CUBIC) for list_h in list_2d
    ]  # concatena todas las imagenes horizontalmente

    return vconcat_resize(img_list_v, interpolation=cv2.INTER_CUBIC)  # concatena todas las imagenes verticalmente


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
