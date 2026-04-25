import cv2
import numpy as np


class ImageAnalyzer:
    """Clase que encapsula la lógica de análisis de imágenes."""

    def calcular_histograma(self, imagen: np.ndarray) -> np.ndarray:
        histograma = cv2.calcHist([imagen], [0], None, [256], [0, 256])
        return histograma.flatten()

    def clasificar_imagen(self, histograma: np.ndarray) -> str:
        intensidad_baja = histograma[:128].sum()
        intensidad_alta = histograma[128:].sum()

        if intensidad_baja > intensidad_alta:
            return "oscura"
        return "clara"


# 🔥 FUNCIÓN QUE KEDRO VA A USAR
def analizar_imagen(image_paths):
    analyzer = ImageAnalyzer()
    resultados = []

    for path in image_paths:
        # 1. leer imagen
        img = cv2.imread(path)

        # 2. pasar a escala de grises
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 3. histograma
        hist = analyzer.calcular_histograma(gray)

        # 4. clasificación
        clase = analyzer.clasificar_imagen(hist)

        # 5. guardar resultado
        resultados.append({
            "ruta_imagen": path,
            "clasificacion": clase,
            "histograma": hist.tolist()
        })

    return resultados