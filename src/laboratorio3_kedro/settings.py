"""Configuración mínima de Kedro para el proyecto."""

from kedro.framework.project import settings


# En esta guía no se personaliza la configuración.
# El archivo se mantiene para mostrar al estudiante dónde
# pueden declararse opciones avanzadas del proyecto.
HOOKS = settings.HOOKS
DISABLE_HOOKS_FOR_PLUGINS = settings.DISABLE_HOOKS_FOR_PLUGINS
SESSION_STORE_CLASS = settings.SESSION_STORE_CLASS
SESSION_STORE_ARGS = settings.SESSION_STORE_ARGS
