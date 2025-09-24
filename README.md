# 📚 Proyecto Backend - Equipo 1

Este repositorio contiene el **backend** del proyecto, desarrollado con **Django** y **Django REST Framework (DRF)**, autenticación con **JWT** y base de datos **MySQL** o **PostgreSQL**.

---

## 🚀 Avance actual

- Proyecto base creado en Django.
- App principal `core/` creada.
- Configuración de **Django REST Framework**.
- Configuración de conexión con **MySQL** (opcional: PostgreSQL) *(pendiente de implementación)*.
- Integración de **JWT Authentication** (`djangorestframework_simplejwt`).
- **Hoy**: Se implementaron los endpoints principales para registro, login, envío de mensajes y consulta de progreso.

---

## 📦 Instalación

Clona el repositorio e instala las dependencias:

```sh
pip install -r requirements.txt
```

---

## 🔑 Endpoints principales

### Registro de usuario

**POST** `/api/register/`

**Body (JSON):**
```json
{
  "username": "usuario",
  "email": "correo@test.com",
  "password": "123456"
}
```

**Response:**
```json
{
  "message": "Usuario creado correctamente"
}
```

---

### Login (obtener tokens JWT)

**POST** `/api/login/`

**Body (JSON):**
```json
{
  "username": "usuario",
  "password": "123456"
}
```

**Response:**
```json
{
  "refresh": "token_refresh",
  "access": "token_access"
}
```

---

### Enviar mensaje (protegido)

**POST** `/api/messages/`

**Headers:**
```
Authorization: Bearer <ACCESS_TOKEN>
```

**Body (JSON):**
```json
{
  "original_text": "Hola como estas?"
}
```

**Response (ejemplo):**
```json
{
  "id": 1,
  "original_text": "Hola como estas?",
  "corrected_text": null,
  "feedback": null,
  "created_at": "2025-09-24T12:34:56Z"
}
```

---

### Consultar progreso (protegido)

**GET** `/api/progress/`

**Headers:**
```
Authorization: Bearer <ACCESS_TOKEN>
```

**Response (ejemplo):**
```json
[
  {
    "id": 1,
    "original_text": "Hola como estas?",
    "corrected_text": "Hola, ¿cómo estás?",
    "feedback": "Recuerda usar tildes.",
    "created_at": "2025-09-24T12:34:56Z"
  }
]
```

---

## 🧪 Pruebas con Postman

Para probar los endpoints protegidos en Postman, añade en la sección **Headers** lo siguiente:

- **Key:** `Authorization`
- **Value:** `Bearer TU_TOKEN_AQUI`

Reemplaza `TU_TOKEN_AQUI` por el token de acceso obtenido en el login.

---

## 📅 Cambios realizados hoy

- Se crearon los endpoints `/api/register/`, `/api/login/`, `/api/messages/` y `/api/progress/` en la app `core/`.
- Se configuró la autenticación JWT para proteger los endpoints de mensajes y progreso.
- Se probaron los endpoints usando herramientas como Postman o el navegador de DRF.

---

## 📖 Notas

- El endpoint `/api/messages/` permite enviar frases para que la IA (equipo 2) procese y devuelva correcciones/feedback.
- El endpoint `/api/progress/` permite ver el historial de mensajes de cada usuario autenticado.
- La autenticación está basada en JWT: el frontend o IA debe enviar el access token en cada request protegida.

---
