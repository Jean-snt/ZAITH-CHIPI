# -*- coding: utf-8 -*-
"""
Módulo del Grafo de Lógica del Tutor de IA.

Este archivo define la arquitectura y el flujo de la conversación del tutor de IA
utilizando LangGraph. El grafo es una máquina de estados que orquesta las llamadas
a los modelos de lenguaje (LLMs) para analizar, corregir, explicar y practicar
conceptos de inglés con el usuario.

Componentes Clave:
- Configuración del Modelo: Inicializa los modelos de Vertex AI.
- Definiciones de Estado y Estructuras:
    - `AnalisisEntrada`: Estructura Pydantic para el análisis de errores.
    - `GraphState`: Diccionario TypedDict que representa el estado de la conversación.
- Nodos del Grafo: Funciones que representan los pasos lógicos (ej. analizar, corregir).
- Bordes Condicionales: Funciones que deciden el siguiente paso en el grafo.
- Ensamblaje del Grafo: Construcción y compilación del grafo de estados.
"""
from langchain_google_vertexai import ChatVertexAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from typing import TypedDict, List, Optional
from langgraph.graph import StateGraph, END

# --- 1. Configuración del Modelo de IA ---

# Inicializa el modelo de lenguaje principal de Vertex AI.
# Se utiliza para tareas de generación de texto libre como explicaciones y conversaciones.
# El parámetro 'temperature' controla la creatividad de las respuestas.
llm = ChatVertexAI(model_name="gemini-1.5-flash-001", temperature=0.7)

class AnalisisEntrada(BaseModel):
    """
    Define una estructura de datos para el análisis de la entrada del usuario.
    
    Esta clase Pydantic asegura que el LLM devuelva la información sobre errores
    gramaticales en un formato predecible y estructurado.
    """
    contiene_error: bool = Field(description="Indica si se encontró un error gramatical en el mensaje del usuario.")
    correccion_sugerida: Optional[str] = Field(description="La corrección sugerida para el error encontrado.")
    tipo_error: Optional[str] = Field(description="El tipo de error gramatical (ej. 'Concordancia Sujeto-Verbo').")

# Vincula la estructura Pydantic al LLM para obtener respuestas estructuradas.
# Esto fuerza al modelo a responder en el formato de `AnalisisEntrada`.
structured_llm = llm.with_structured_output(AnalisisEntrada)


# --- 2. Definición del Estado del Grafo ---

class GraphState(TypedDict):
    """
    Representa el estado de la conversación en cualquier punto del grafo.

    Este estado es persistente a lo largo de la conversación y se pasa entre nodos.
    Contiene toda la información necesaria para que el tutor tome decisiones.

    Atributos:
        conversation_history (List[str]): Historial completo de la conversación.
        user_level (Optional[str]): Nivel de inglés estimado del usuario (ej. "A1", "B2").
        error_patterns (List[str]): Lista de errores gramaticales comunes del usuario.
        current_topic (Optional[str]): Tema actual de la conversación.
        last_interaction_type (Optional[str]): Tipo de la última interacción (ej. "corrección", "ejercicio").
        user_message (str): El último mensaje enviado por el usuario.
        bot_response (Optional[str]): La última respuesta generada por el bot.
    """
    conversation_history: List[str]
    user_level: Optional[str]
    error_patterns: List[str]
    current_topic: Optional[str]
    last_interaction_type: Optional[str]
    user_message: str
    bot_response: Optional[str]


# --- 3. Nodos del Grafo (Lógica de la IA) ---

def analizar_entrada(state: GraphState) -> GraphState:
    """
    Nodo 1: Analiza la entrada del usuario para detectar errores gramaticales.

    Utiliza un LLM estructurado para identificar si hay un error, sugerir una
    corrección y clasificar el tipo de error. Actualiza el estado con esta
    información para dirigir el flujo del grafo.
    """
    print("--- Ejecutando Nodo: Analizar Entrada (IA) ---")
    user_message = state["user_message"]
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", """Eres Chipi, un tutor de español experto y amigable. Tu objetivo es identificar el error más significativo en la frase de un estudiante.
Sigue estos pasos:
1.  Analiza la frase del usuario: `{user_message}`.
2.  Busca errores gramaticales, de vocabulario o de estructura. Ignora errores de tipeo menores que no afecten el significado.
3.  Si encuentras un error, identifica la corrección y clasifica el tipo de error (ej: 'Concordancia de Género', 'Uso de Ser/Estar', 'Preposiciones', 'Tiempo Verbal').
4.  Si no hay un error claro, pero la frase suena poco natural, sugiere una forma más común de expresarla.
5.  Responde únicamente con la estructura de datos JSON solicitada."""),
        ("human", f"Por favor, analiza la siguiente frase: '{user_message}'")
    ])
    
    chain = prompt | structured_llm
    analisis_result = chain.invoke({})
    
    if analisis_result.contiene_error:
        print(f"Error detectado: {analisis_result.tipo_error}")
        state["last_interaction_type"] = "correction_detected"
        state["bot_response"] = f"Corrección: '{analisis_result.correccion_sugerida}'"
        if analisis_result.tipo_error and analisis_result.tipo_error not in state["error_patterns"]:
            state["error_patterns"].append(analisis_result.tipo_error)
    else:
        print("No se detectaron errores.")
        state["last_interaction_type"] = "chat"
        state["bot_response"] = None

    return state

def generar_correccion_y_explicacion(state: GraphState) -> GraphState:
    """
    Nodo 2: Genera una explicación simple para la corrección gramatical.

    Si se detectó un error, este nodo usa el LLM para crear una explicación
    clara y concisa de la regla gramatical, adaptada a un nivel de principiante.
    """
    print("--- Ejecutando Nodo: Generar Corrección y Explicación (IA) ---")
    user_message = state["user_message"]
    correccion = state["bot_response"]
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Eres Chipi, un tutor de español muy paciente. Explica la siguiente corrección gramatical de forma sencilla y clara, como para un principiante. Enfócate en la regla principal sin usar términos complejos. Proporciona la regla y un ejemplo adicional."),
        ("human", f"Frase original del estudiante: '{user_message}'.\nMi corrección fue: {correccion}.\n\nExplica por qué la corrección es necesaria de forma simple.")
    ])
    
    chain = prompt | llm
    explanation = chain.invoke({})
    
    state["bot_response"] = f"{correccion}\n\n**Regla:** {explanation.content}"
    state["last_interaction_type"] = "explanation_given"
    return state

def generar_ejercicio(state: GraphState) -> GraphState:
    """
    Nodo 3: Genera un ejercicio de práctica basado en el error corregido.

    Crea un ejercicio de "completar el espacio en blanco" para que el usuario
    pueda practicar la regla gramatical que acaba de aprender.
    """
    print("--- Ejecutando Nodo: Generar Ejercicio (IA) ---")
    user_message = state["user_message"]
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Eres Chipi, un tutor de español. Crea un ejercicio práctico de 'completar el espacio en blanco' que ayude al estudiante a practicar la regla que acaba de aprender. El ejercicio debe ser simple y directo. Proporciona únicamente la frase del ejercicio."),
        ("human", f"La corrección se aplicó a la frase: '{user_message}'. Crea un ejercicio relevante para esa regla gramatical.")
    ])
    
    chain = prompt | llm
    ejercicio = chain.invoke({})
    
    state["bot_response"] += f"\n\n**Práctica:** {ejercicio.content}"
    state["last_interaction_type"] = "exercise_given"
    return state

def evaluar_respuesta_ejercicio(state: GraphState) -> GraphState:
    """
    Nodo 4: Evalúa la respuesta del usuario al ejercicio.

    Determina si la respuesta del usuario es correcta o incorrecta, utilizando
    el contexto de la conversación para entender la pregunta del ejercicio.
    """
    print("--- Ejecutando Nodo: Evaluar Respuesta del Ejercicio (IA) ---")
    conversation_history = "\n".join(state["conversation_history"])
    user_answer = state["user_message"]

    prompt = ChatPromptTemplate.from_messages([
        ("system", "Eres un evaluador preciso. Tu única tarea es determinar si la respuesta del usuario al ejercicio es correcta. Considera el contexto de la conversación para entender la pregunta. Responde únicamente con 'True' si es correcta o 'False' si es incorrecta."),
        ("human", f"Historial de la conversación:\n{conversation_history}\n\nLa última respuesta del usuario fue: '{user_answer}'.\n\n¿Es esta la respuesta correcta para el ejercicio propuesto? Responde solo 'True' o 'False'.")
    ])
    
    chain = prompt | llm
    result = chain.invoke({})
    
    if "true" in result.content.lower():
        print("Respuesta evaluada como CORRECTA.")
        state["last_interaction_type"] = "exercise_correct"
    else:
        print("Respuesta evaluada como INCORRECTA.")
        state["last_interaction_type"] = "exercise_incorrect"
    return state

def refuerzo_positivo(state: GraphState) -> GraphState:
    """
    Nodo 5a: Proporciona refuerzo positivo y continúa la conversación.

    Si el usuario acierta el ejercicio, lo felicita y hace una pregunta abierta
    para volver a un flujo de conversación natural.
    """
    print("--- Ejecutando Nodo: Refuerzo Positivo (IA) ---")
    prompt = ChatPromptTemplate.from_template(
        "Eres Chipi, un tutor que anima a sus estudiantes. El estudiante acertó el ejercicio. Felicítalo de forma breve y natural (ej. '¡Muy bien!' o '¡Exacto!') y luego haz una pregunta abierta para volver a una conversación normal."
    )
    chain = prompt | llm
    response = chain.invoke({})
    state["bot_response"] = response.content
    state["last_interaction_type"] = "chat"
    return state

def re_explicar(state: GraphState) -> GraphState:
    """
    Nodo 5b: Re-explica el concepto si el usuario se equivoca.

    Si el usuario falla el ejercicio, explica la regla de nuevo de una forma
    diferente y luego cambia de tema para no frustrarlo.
    """
    print("--- Ejecutando Nodo: Re-explicar (IA) ---")
    conversation_history = "\n".join(state["conversation_history"])

    prompt = ChatPromptTemplate.from_messages([
        ("system", "Eres Chipi, un tutor comprensivo. El estudiante no acertó el ejercicio. No te preocupes. Re-explica la regla de una manera aún más simple o con una analogía diferente. Luego, para no frustrarlo, haz una pregunta sencilla sobre un tema nuevo."),
        ("human", f"Contexto de la conversación:\n{conversation_history}\n\nEl estudiante se equivocó en el ejercicio. Vuelve a explicarle la regla de otra forma y luego cambia de tema.")
    ])
    
    chain = prompt | llm
    response = chain.invoke({})
    state["bot_response"] = response.content
    state["last_interaction_type"] = "chat"
    return state

def continuar_conversacion_natural(state: GraphState) -> GraphState:
    """
    Nodo 6: Mantiene una conversación natural con el usuario.

    Si no se detectan errores, este nodo simplemente genera una respuesta
    apropiada para continuar la charla de forma fluida.
    """
    print("--- Ejecutando Nodo: Continuar Conversación Natural (IA) ---")
    conversation_history = state["conversation_history"]
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Eres Chipi, un compañero de chat en español amigable y curioso. Tu objetivo es mantener una conversación natural. No corrijas, solo conversa. Haz preguntas abiertas y muestra interés."),
        ("human", f"Este es el historial de nuestra conversación:\n{conversation_history}\n\nAhora, continúa la charla de forma interesante.")
    ])
    
    chain = prompt | llm
    response = chain.invoke({})
    state["bot_response"] = response.content
    state["last_interaction_type"] = "chat"
    return state


# --- 4. Bordes Condicionales (Lógica de Enrutamiento) ---

def decidir_camino_despues_de_analisis(state: GraphState) -> str:
    """
    Decide el siguiente paso después de analizar la entrada del usuario.
    - Si se detectó un error, inicia el ciclo de corrección.
    - Si no, continúa con una conversación normal.
    """
    print(f"--- Decidiendo Camino (Análisis): Tipo = {state['last_interaction_type']} ---")
    if state["last_interaction_type"] == "correction_detected":
        return "ciclo_de_correccion"
    return "conversacion_natural"

def decidir_camino_despues_de_evaluacion(state: GraphState) -> str:
    """
    Decide el siguiente paso después de evaluar la respuesta a un ejercicio.
    - Si la respuesta es correcta, da refuerzo positivo.
    - Si es incorrecta, vuelve a explicar.
    """
    print(f"--- Decidiendo Camino (Evaluación): Tipo = {state['last_interaction_type']} ---")
    if state["last_interaction_type"] == "exercise_correct":
        return "refuerzo_positivo"
    return "re_explicar"


# --- 5. Ensamblaje del Grafo ---

def create_tutor_graph():
    """
    Crea, configura y compila el grafo de estados del tutor de IA.

    Esta función ensambla todos los nodos y bordes para definir el flujo completo
    de la lógica conversacional.

    Returns:
        CompiledGraph: El grafo de LangGraph compilado y listo para ser invocado.
    """
    workflow = StateGraph(GraphState)

    # Añadir todos los nodos al grafo
    workflow.add_node("analizar_entrada", analizar_entrada)
    workflow.add_node("generar_correccion_y_explicacion", generar_correccion_y_explicacion)
    workflow.add_node("generar_ejercicio", generar_ejercicio)
    workflow.add_node("evaluar_respuesta_ejercicio", evaluar_respuesta_ejercicio)
    workflow.add_node("refuerzo_positivo", refuerzo_positivo)
    workflow.add_node("re_explicar", re_explicar)
    workflow.add_node("continuar_conversacion_natural", continuar_conversacion_natural)

    # Definir el punto de entrada del grafo
    workflow.set_entry_point("analizar_entrada")

    # Añadir bordes condicionales para la toma de decisiones
    workflow.add_conditional_edges(
        "analizar_entrada",
        decidir_camino_despues_de_analisis,
        {
            "ciclo_de_correccion": "generar_correccion_y_explicacion",
            "conversacion_natural": "continuar_conversacion_natural",
        },
    )
    workflow.add_conditional_edges(
        "evaluar_respuesta_ejercicio",
        decidir_camino_despues_de_evaluacion,
        {
            "refuerzo_positivo": "refuerzo_positivo",
            "re_explicar": "re_explicar",
        },
    )

    # Añadir bordes normales que definen flujos lineales
    workflow.add_edge("generar_correccion_y_explicacion", "generar_ejercicio")
    # En una implementación real, este borde esperaría la entrada del usuario.
    # Aquí, para simplicidad, fluye directamente a la evaluación.
    workflow.add_edge("generar_ejercicio", "evaluar_respuesta_ejercicio")
    
    # Definir los puntos finales del grafo
    workflow.add_edge("refuerzo_positivo", END)
    workflow.add_edge("re_explicar", END)
    workflow.add_edge("continuar_conversacion_natural", END)

    # Compilar el grafo en una aplicación ejecutable
    app = workflow.compile()
    return app

# Opcional: Visualizar el grafo (requiere matplotlib y pygraphviz)
# if __name__ == '__main__':
#     app = create_tutor_graph()
#     try:
#         # Genera una imagen PNG del grafo para visualización.
#         app.get_graph().draw_mermaid_png(output_file_path="graph_visualization.png")
#         print("Grafo visualizado y guardado en 'graph_visualization.png'")
#     except Exception as e:
#         print(f"No se pudo visualizar el grafo. Asegúrate de tener 'matplotlib' y 'pygraphviz' instalados. Error: {e}")