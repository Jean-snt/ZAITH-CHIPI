# -*- coding: utf-8 -*-
"""
Módulo de Servicios para el Tutor de Chat IA.

Este módulo encapsula toda la lógica de negocio relacionada con la interacción del chat,
la gestión del estado de la conversación y la orquestación del grafo de LangChain.
Su objetivo es mantener los controladores (vistas) delgados y centrados en la gestión de
solicitudes y respuestas HTTP, mientras que la lógica compleja reside aquí.

Funciones:
- gestionar_chat_ia: Orquesta el procesamiento de un mensaje de usuario.
- _obtener_o_crear_estado_conversacion: Recupera o inicializa el estado de la conversación para un usuario.
- _ejecutar_grafo_ia: Invoca el grafo de LangChain con el estado actual.
- _actualizar_estado_conversacion: Guarda el estado final de la conversación en la base de datos.
"""

from .models import ConversationState
from .graph import create_tutor_graph, GraphState
from django.contrib.auth.models import User

def gestionar_chat_ia(user: User, user_message: str) -> dict:
    """
    Orquesta el flujo completo de una interacción de chat con la IA.

    Esta función de alto nivel coordina los siguientes pasos:
    1. Recupera o crea el estado de la conversación del usuario.
    2. Prepara el estado para la ejecución del grafo de IA.
    3. Invoca el grafo de IA para obtener una respuesta.
    4. Actualiza y guarda el nuevo estado de la conversación.
    5. Devuelve la respuesta generada por la IA.

    Args:
        user (User): La instancia del usuario autenticado que envía el mensaje.
        user_message (str): El mensaje de texto enviado por el usuario.

    Returns:
        dict: Un diccionario que contiene la respuesta del bot, listo para ser enviado
              como una respuesta JSON. Ejemplo: {"reply": "Hello there!"}
    """
    # 1. Obtener el estado actual de la conversación
    conversation_state = _obtener_o_crear_estado_conversacion(user)

    # 2. Preparar el estado para el grafo
    current_graph_state: GraphState = conversation_state.state_json
    current_graph_state["user_message"] = user_message
    current_graph_state["conversation_history"].append(f"User: {user_message}")

    # 3. Ejecutar el grafo de IA
    final_state = _ejecutar_grafo_ia(current_graph_state)

    # 4. Actualizar y guardar el estado
    _actualizar_estado_conversacion(conversation_state, final_state)

    # 5. Devolver la respuesta
    return {"reply": final_state.get("bot_response")}

def _obtener_o_crear_estado_conversacion(user: User) -> ConversationState:
    """
    Recupera el estado de la conversación para un usuario o crea uno nuevo si no existe.

    El estado inicial por defecto contiene una estructura vacía para el historial,
    nivel del usuario, patrones de error, etc.

    Args:
        user (User): El usuario para el cual se busca el estado.

    Returns:
        ConversationState: La instancia del modelo ConversationState, ya sea existente o recién creada.
    """

    initial_state: GraphState = {
        "conversation_history": [],
        "user_level": None,
        "error_patterns": [],
        "current_topic": None,
        "last_interaction_type": None,
        "user_message": "",
        "bot_response": None,
    }
    
    state, created = ConversationState.objects.get_or_create(
        user=user,
        defaults={"state_json": initial_state}
    )
    return state

def _ejecutar_grafo_ia(current_state: GraphState) -> GraphState:
    """
    Invoca el grafo de LangChain con el estado actual de la conversación.

    El grafo procesa el mensaje del usuario en el contexto del historial y decide
    la acción apropiada (corregir, explicar, conversar, etc.).

    Args:
        current_state (GraphState): El estado actual de la conversación, incluyendo
                                    el último mensaje del usuario.

    Returns:
        GraphState: El estado final después de que el grafo haya sido ejecutado.
    """
    graph = create_tutor_graph()
    final_state = graph.invoke(current_state)
    return final_state

def _actualizar_estado_conversacion(conversation_state: ConversationState, final_state: GraphState):
    """
    Actualiza el historial de la conversación y guarda el estado final en la base de datos.

    Añade la respuesta del bot al historial antes de persistir los cambios.

    Args:
        conversation_state (ConversationState): La instancia del modelo de estado a actualizar.
        final_state (GraphState): El estado resultante de la ejecución del grafo.
    """
    if final_state.get("bot_response"):
        final_state["conversation_history"].append(f"Bot: {final_state['bot_response']}")

    conversation_state.state_json = final_state
    conversation_state.save()