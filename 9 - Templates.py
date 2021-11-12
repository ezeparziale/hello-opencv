import cv2

# Carga de imagen
img = cv2.resize(cv2.imread('img/pokemons.jpg', 0), (0, 0), fx=0.8, fy=0.8)

# Carga de template a buscar
template = cv2.resize(cv2.imread('img/pokemon_test1.jpg', 0), (0, 0), fx=0.8, fy=0.8)
# template = cv2.resize(cv2.imread('img/pokemon_test2.jpg', 0), (0, 0), fx=0.8, fy=0.8)

h, w = template.shape

# Metodos de busqueda template
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()

    # Matching template
    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Identificación puntos para recuadro
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)    

    # Visualización
    cv2.rectangle(img2, location, bottom_right, 0, 3) # Recudro de la busqueda
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()