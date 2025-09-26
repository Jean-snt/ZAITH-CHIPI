# -*- coding: utf-8 -*-
"""
Módulo de URLs para la aplicación 'chat_tutor'.

Este archivo define las rutas de la API para la funcionalidad del tutor de chat.
Cada ruta se asigna a una vista específica que maneja la lógica de la solicitud.

Rutas:
- /chat/: Endpoint para la interacción principal del chat. Dirige a ChatView.
"""
from django.urls import path
from .views import ChatView

urlpatterns = [
    # Define la ruta para el endpoint del chat.
    # Se utiliza ChatView.as_view() porque es una vista basada en clase.
    # El nombre 'chat' permite referenciar esta URL de forma única en el proyecto.
    path("chat/", ChatView.as_view(), name="chat"),
]