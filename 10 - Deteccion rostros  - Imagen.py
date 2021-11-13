import cv2

# Carga de webcam
img = cv2.imread('img/argentina.jpeg', cv2.IMREAD_COLOR)

# Modelos
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Conversión a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detección de cara
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)  # Dibujo rectangulo en cara

print(f'Se encontraron {len(faces)} rostros!')

# Visualización
cv2.imshow('Imagen', img)
cv2.waitKey(0)  # Espera hasta que se presione una tecla para cerrar
cv2.destroyAllWindows()