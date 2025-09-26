# 📚 Backend de ZAITH-CHIPI

Este repositorio contiene el **backend** del proyecto ZAITH-CHIPI, un tutor de español impulsado por IA. Está desarrollado con **Django** y **Django REST Framework (DRF)**, y utiliza **LangChain** para orquestar la lógica de la IA.

---

## 🚀 Arquitectura y Componentes

El backend está estructurado en varias aplicaciones de Django, cada una con una responsabilidad clara:

-   `config/`: Contiene la configuración global del proyecto Django, incluyendo `settings.py` y `urls.py` principales.
-   `core/`: Gestiona la autenticación de usuarios (registro y login con JWT) y los modelos de datos principales.
-   `chat_tutor/`: **(Nuevo)** Encapsula toda la lógica del tutor de IA.
    -   `views.py`: Expone el endpoint `/api/chat/` para la interacción con el tutor.
    -   `services.py`: Orquesta la lógica de negocio, gestionando el estado de la conversación.
    -   `graph.py`: Define el grafo de estados de LangGraph que controla el flujo de la conversación y la toma de decisiones de la IA.
    -   `models.py`: Almacena el estado de la conversación de cada usuario en la base de datos.

---

## 📦 Instalación y Configuración

Para ejecutar el backend, sigue estos pasos:

1.  **Clona el repositorio** y navega a la carpeta del backend:
    ```sh
    git clone <URL_DEL_REPOSITORIO>
    cd ZAITH-CHIPI/BACKEND
    ```

2.  **(Recomendado)** Crea y activa un **entorno virtual**:
    ```sh
    # Crear el entorno
    python -m venv venv

    # Activar en Windows
    venv\Scripts\activate

    # Activar en macOS/Linux
    # source venv/bin/activate
    ```

3.  **Instala las dependencias**:
    El archivo `requirements.txt` ha sido limpiado y las versiones han sido fijadas para garantizar la estabilidad.
    ```sh
    pip install -r requirements.txt
    ```

4.  **Aplica las migraciones** para configurar la base de datos (SQLite por defecto):
    ```sh
    python manage.py migrate
    ```

5.  **Inicia el servidor**:
    ```sh
    python manage.py runserver
    ```
    El servidor estará disponible en `http://127.0.0.1:8000`.

---

## 🔑 Endpoints de la API

### Autenticación

-   **`POST /api/register/`**: Para crear un nuevo usuario.
-   **`POST /api/login/`**: Para autenticar un usuario y obtener tokens `access` y `refresh`.

### Tutor de IA

-   **`POST /api/chat/`** (Protegido con JWT)
    -   Este es el endpoint principal para interactuar con el tutor de IA.
    -   **Headers**: `Authorization: Bearer <ACCESS_TOKEN>`
    -   **Body (JSON)**:
        ```json
        {
          "message": "He ido a la tienda y compre dos manzanas."
        }
        ```
    -   **Respuesta (Ejemplo de corrección)**:
        ```json
        {
          "reply": "Corrección: 'Fui a la tienda y compré dos manzanas.'\n\n**Regla:** En español, para acciones pasadas y terminadas, usamos el Pretérito Perfecto Simple (como 'fui' y 'compré') en lugar del Pretérito Perfecto Compuesto ('he ido').\n\n**Práctica:** Completa la frase: Ayer, yo ___ al cine. (ir)"
        }
        ```

---

## 🧠 Mejoras en Prompt Engineering

Se ha realizado una reingeniería completa de los prompts en `chat_tutor/graph.py` para mejorar drásticamente la calidad de las interacciones:

-   **Persona Definida**: La IA ahora adopta la personalidad de "Chipi", un tutor amigable y experto.
-   **Contexto Mejorado**: Los prompts ahora son más específicos y utilizan el historial de la conversación para tomar mejores decisiones.
-   **Instrucciones Claras**: Se utiliza un enfoque de "cadena de pensamiento" (Chain of Thought) para guiar a la IA en tareas complejas como el análisis de errores.
-   **Enfoque en Español**: Todos los prompts han sido corregidos para centrarse en la enseñanza del español.
