import cv2
from laboratorio3_kedro.pipelines.histogram.analyzer import ImageAnalyzer


def analizar_imagen(image_paths: list) -> list:
    """Carga múltiples imágenes, calcula histograma y clasifica cada una."""

    analyzer = ImageAnalyzer()
    resultados = []

    for filepath in image_paths:
        imagen = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)

        if imagen is None:
            raise ValueError(f"No se pudo cargar la imagen: {filepath}")

        histograma = analyzer.calcular_histograma(imagen)
        clasificacion = analyzer.clasificar_imagen(histograma)

        resultados.append({
            "ruta_imagen": filepath,
            "clasificacion": clasificacion,
            "histograma": histograma.tolist(),
        })

    return resultados