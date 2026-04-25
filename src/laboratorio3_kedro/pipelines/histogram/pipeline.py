from kedro.pipeline import Pipeline, node
from laboratorio3_kedro.pipelines.histogram.nodes import analizar_imagen


def create_pipeline(**kwargs) -> Pipeline:
    """Crea el pipeline de análisis de histogramas."""
    return Pipeline(
        [
            node(
                func=analizar_imagen,
                inputs="params:image_paths",
                outputs="resultados_analisis",
                name="analizar_imagen_node",
            )
        ]
    )