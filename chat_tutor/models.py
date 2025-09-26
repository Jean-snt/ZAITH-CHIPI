# -*- coding: utf-8 -*-
"""
Módulo de Modelos para la aplicación 'chat_tutor'.

Este archivo define la estructura de la base de datos para la funcionalidad del
tutor de chat. Los modelos de Django son la fuente única y definitiva de
información sobre los datos de la aplicación.

Clases:
- ConversationState: Almacena el estado de la conversación de un usuario con la IA.
"""
from django.db import models
from django.contrib.auth.models import User

class ConversationState(models.Model):
    """
    Representa el estado de una conversación entre un usuario y el tutor de IA.

    Este modelo almacena el estado completo del grafo de LangChain en formato JSON,
    permitiendo que las conversaciones sean persistentes y puedan reanudarse.

    Atributos:
        user (OneToOneField): Relación uno a uno con el modelo de usuario de Django.
                              Cada usuario tiene un único estado de conversación.
        state_json (JSONField): Un campo JSON para almacenar el diccionario de estado
                                del grafo de LangChain (GraphState).
        last_updated (DateTimeField): Marca de tiempo que se actualiza automáticamente
                                      cada vez que se guarda el estado.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        help_text="Usuario al que pertenece este estado de conversación."
    )
    state_json = models.JSONField(
        help_text="Almacena el estado del grafo de LangChain en formato JSON."
    )
    last_updated = models.DateTimeField(
        auto_now=True,
        help_text="Fecha y hora de la última actualización del estado."
    )

    def __str__(self):
        """
        Devuelve una representación en cadena del modelo.
        """
        return f"Estado de la conversación de {self.user.username}"

    class Meta:
        """
        Metadatos para el modelo ConversationState.
        """
        verbose_name = "Estado de Conversación"
        verbose_name_plural = "Estados de Conversación"
