# -*- coding: utf-8 -*-
"""
Configuración de URLs principal del proyecto.

Este archivo es el enrutador principal de URLs para todo el proyecto Django.
Define las rutas de nivel superior y delega las rutas específicas de las
aplicaciones a sus respectivos archivos `urls.py`.

Rutas Principales:
- /admin/: Interfaz de administración de Django.
- /api/: Rutas para la aplicación 'core' (ej. autenticación, usuarios).
- /api/tutor/: Rutas para la aplicación 'chat_tutor'.
- /: Ruta raíz que muestra un mensaje de bienvenida.
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

urlpatterns = [
    # Ruta para la interfaz de administración de Django.
    path('admin/', admin.site.urls),

    # Incluye las URLs de la aplicación 'core'.
    # Todas las rutas definidas en 'core.urls' estarán prefijadas con 'api/'.
    path('api/', include('core.urls')),

    # Incluye las URLs de la aplicación 'chat_tutor'.
    # Todas las rutas definidas en 'chat_tutor.urls' estarán prefijadas con 'api/tutor/'.
    path('api/tutor/', include('chat_tutor.urls')),

    # Ruta raíz que devuelve una respuesta JSON de bienvenida.
    # Útil para verificar que la API está en funcionamiento.
    path('', lambda request: JsonResponse({"message": "Bienvenido a la API del Equipo 1 🚀"})),
]

