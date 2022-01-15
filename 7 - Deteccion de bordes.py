import cv2
import numpy as np


def on_trackbar(value):
    pass

# Show trackbar
title_window = "Trackbar"

cv2.namedWindow(title_window)
cv2.resizeWindow(title_window, 800, 150)
cv2.createTrackbar("Threadhold 1", title_window, 100, 255, on_trackbar)
cv2.createTrackbar("Threadhold 2", title_window, 255, 255, on_trackbar)

while True:
    # Carga
    img = cv2.imread("img/image_2.jpg")
    img = cv2.resize(img, (0, 0), fx=0.3, fy=0.3)  # Resizing con %

    kernel = np.ones((5, 5), np.uint8)  # Kernel size= 3x3, 5x5, 7x7, ...

    threadhold_1 = cv2.getTrackbarPos("Threadhold 1", title_window)
    threadhold_2 = cv2.getTrackbarPos("Threadhold 2", title_window)

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (5, 5), 1.4)
    img_canny = cv2.Canny(img, threadhold_1, threadhold_2)
    img_dialation = cv2.dilate(img_canny, kernel, iterations=1)
    img_eroded = cv2.erode(img_dialation, kernel, iterations=1)

    # Visualización
    cv2.imshow("Imagen orignal", img)
    cv2.imshow("Escala de grises", img_gray)
    cv2.imshow("Blur", img_blur)
    cv2.imshow("Canny", img_canny)
    cv2.imshow("Dialation", img_dialation)
    cv2.imshow("Eroded", img_eroded)

    if cv2.waitKey(1) == ord("q"):  # Presionar "Q" para salir
        break

cv2.destroyAllWindows()
