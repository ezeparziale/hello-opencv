import cv2
import numpy as np


def on_trackbar(value):
    pass


# Show trackbar
title_window = "Trackbar"

cv2.namedWindow(title_window)
cv2.resizeWindow(title_window, 640, 240)

cv2.createTrackbar("Hue Min", title_window, 80, 255, on_trackbar)
cv2.createTrackbar("Hue Max", title_window, 118, 255, on_trackbar)
cv2.createTrackbar("Sat Min", title_window, 31, 255, on_trackbar)
cv2.createTrackbar("Sat Max", title_window, 255, 255, on_trackbar)
cv2.createTrackbar("Val Min", title_window, 84, 255, on_trackbar)
cv2.createTrackbar("Val Max", title_window, 255, 255, on_trackbar)

# Carga de imagen
imagen_path = "img/car_0.jpg"

img = cv2.imread(imagen_path)
img = cv2.resize(img, (0, 0), fx=0.4, fy=0.4)  # Resizing con %

while True:
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue Min", title_window)
    h_max = cv2.getTrackbarPos("Hue Max", title_window)
    s_min = cv2.getTrackbarPos("Sat Min", title_window)
    s_max = cv2.getTrackbarPos("Sat Max", title_window)
    v_min = cv2.getTrackbarPos("Val Min", title_window)
    v_max = cv2.getTrackbarPos("Val Max", title_window)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(img_hsv, lower, upper)
    img_result = cv2.bitwise_and(img, img, mask=mask)

    mask = cv2.cvtColor(
        mask, cv2.COLOR_GRAY2RGB
    )  # Para realizar un reshape y poder concatenar

    img_all = np.vstack((np.hstack((img, img_hsv)), np.hstack((mask, img_result))))

    cv2.imshow("Mascara de color", img_all)

    if cv2.waitKey(1) & cv2.waitKey(1) == ord("q"):  # Presionar "Q" para salir
        break
