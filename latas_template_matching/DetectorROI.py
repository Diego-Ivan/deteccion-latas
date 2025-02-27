# Diego Iván Martínez Escobar
# Programa de Honores
# Universidad de las Américas Puebla, 2025

import cv2

def obtener_detecciones(imagen):
    """
    Genera las detecciones de latas para una imagen de OpenCV (np.array)
    Las detecciones que genera son
    :param imagen: La imagen de la cuál se obtendrán las detecciones
    :return: Un arreglo de 4-tuplas de la forma [(x1, y1, x2, y2), ...], donde (x1, y1) es la esquina superior de la detección, y (x2, y2) es la esquina inferior derecha
    """

    # Leer la imagen en blanco y negro
    gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Aplicar Gaussian Blur para reducir el ruido
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Aplicar binarización del Umbral de Otsu para separar las latas de la arena
    # FIXME: Verificar que THRESH_BINARY_INV es el threshold correcto, o si es mejor utilizar cv2.THRESH_BINARY
    # por la iluminación que pueda tener la imagen.
    ret, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

    # Encontrar los contornos de la imagen filtrada
    contours, hierarchy = cv2.findContours(opening.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    latas_detectadas = []

    for cnt in contours:
        # Descartar contornos demasiado pequeños
        # FIXME: Es 500 mucho para la resolución de la cámara que se va a utilizar?
        if cv2.contourArea(cnt) < 500 or cv2.contourArea(cnt) > 5000:
            continue

        x, y, w, h = cv2.boundingRect(cnt)
        latas_detectadas.append((x, y, x + w, y + h))

    return latas_detectadas
