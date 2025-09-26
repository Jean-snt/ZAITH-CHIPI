# -*- coding: utf-8 -*-
"""
Módulo de Vistas para el Tutor de Chat IA.

Este módulo define los puntos de entrada de la API REST para la funcionalidad del chat.
Actúa como la capa de presentación, gestionando las solicitudes HTTP, la autenticación,
la validación de entradas y la delegación de la lógica de negocio al módulo de servicios.

Clases:
- ChatView: Maneja las interacciones de chat a través de solicitudes POST.
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .services import gestionar_chat_ia

class ChatView(APIView):
    """
    Vista de API para gestionar la interacción del chat con el tutor de IA.

    Este endpoint espera una solicitud POST autenticada que contenga un campo 'message'.
    Delega el procesamiento del mensaje al módulo de servicios `gestionar_chat_ia`
    y devuelve la respuesta generada por la IA.

    Métodos:
    - post: Procesa el mensaje entrante del usuario y devuelve la respuesta del bot.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        """
        Maneja las solicitudes POST para el chat.

        Extrae el mensaje del usuario de la solicitud, valida que no esté vacío
        y llama al servicio `gestionar_chat_ia` para procesarlo.

        Args:
            request (Request): El objeto de solicitud de Django REST Framework.
            *args: Argumentos adicionales.
            **kwargs: Argumentos de palabra clave adicionales.

        Returns:
            Response: Un objeto de respuesta JSON que contiene la réplica del bot
                      o un mensaje de error si la entrada es inválida.
        """
        user = request.user
        user_message = request.data.get("message")

        if not user_message:
            return Response(
                {"error": "El campo 'message' es obligatorio."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Delegar la lógica de negocio al servicio
        response_data = gestionar_chat_ia(user, user_message)

        return Response(response_data, status=status.HTTP_200_OK)
