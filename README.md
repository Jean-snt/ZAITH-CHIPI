# 🦙 PROYECTO LLAMA "CHIPI" - Tutor Interactivo de Español

## 📋 Descripción del Proyecto

**PROYECTO LLAMA "CHIPI"** es una aplicación web completa que funciona como un tutor interactivo de español potenciado por inteligencia artificial. El proyecto combina un backend robusto desarrollado en **Django** con un frontend moderno en **React + Vite**, ofreciendo una experiencia de aprendizaje inmersiva y personalizada.

### ✨ Características Principales

- 🦙 **Mascota Virtual**: Chipi, una llama amigable que guía el aprendizaje
- 🤖 **IA Avanzada**: Corrección automática y enseñanza personalizada
- 💬 **Chat Interactivo**: Conversación en tiempo real con retroalimentación
- 🔐 **Autenticación Segura**: Sistema JWT para usuarios registrados
- 📱 **Interfaz Moderna**: Diseño responsivo con efectos visuales
- 🎯 **Aprendizaje Adaptativo**: Se ajusta al nivel del estudiante

---

## 🏗️ Arquitectura del Sistema

```
ZAITH-CHIPI/
├── 🖥️ BACKEND (Django + DRF + LangChain)
│   ├── config/          # Configuración principal
│   ├── core/            # Autenticación y modelos base
│   ├── chat_tutor/      # Lógica del tutor IA
│   └── tutor/           # Funcionalidades adicionales
│
├── 🎨 FRONTEND (React + Vite)
│   ├── src/
│   │   ├── components/  # Componentes React
│   │   ├── pages/       # Páginas principales
│   │   ├── services/    # Conexión con API
│   │   └── styles/      # Estilos CSS
│   └── public/          # Archivos estáticos
│
└── 📄 DOCUMENTACIÓN
    ├── README.md        # Este archivo
    └── frontend-zaith-chipi/README.md  # Docs del frontend
```

---

## 🚀 Guía de Instalación Completa

### 📋 Prerrequisitos

Antes de comenzar, asegúrate de tener instalado:

- **Python 3.8+** (para el backend)
- **Node.js 18+** (para el frontend)
- **Git** (para clonar el repositorio)

#### Verificar instalaciones:
```bash
python --version    # Debe mostrar 3.8+ 
node --version      # Debe mostrar 18.x.x+
npm --version       # Debe mostrar 8.x.x+
git --version       # Cualquier versión reciente
```

### 1️⃣ Clonar el Repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd ZAITH-CHIPI
```

### 2️⃣ Configurar el Backend (Django)

#### Crear entorno virtual (Recomendado):
```bash
# Crear entorno virtual
python -m venv venv

# Activar en Windows
venv\Scripts\activate

# Activar en macOS/Linux
source venv/bin/activate
```

#### Instalar dependencias:
```bash
pip install -r requirements.txt
```

#### Configurar base de datos:
```bash
python manage.py migrate
```

#### Crear superusuario (Opcional):
```bash
python manage.py createsuperuser
```

### 3️⃣ Configurar el Frontend (React)

#### Navegar al directorio del frontend:
```bash
cd frontend-zaith-chipi
```

#### Instalar dependencias:
```bash
npm install
```

---

## 🎮 Cómo Iniciar el Programa

### 🔥 Inicio Rápido (Ambos Servidores)

#### Terminal 1 - Backend:
```bash
# Desde la raíz del proyecto ZAITH-CHIPI
python manage.py runserver 8000
```

#### Terminal 2 - Frontend:
```bash
# Desde ZAITH-CHIPI/frontend-zaith-chipi
npm run dev
```

### 🌐 URLs de Acceso

Una vez iniciados ambos servidores:

- **🎨 Aplicación Frontend**: http://localhost:5173
- **🔧 API Backend**: http://localhost:8000/api
- **⚙️ Panel Admin Django**: http://localhost:8000/admin

---

## 🔑 Endpoints de la API

### Autenticación
- **`POST /api/register/`** - Registro de nuevos usuarios
- **`POST /api/login/`** - Inicio de sesión (obtiene tokens JWT)

### Tutor de IA
- **`POST /api/chat/`** - Interacción con el tutor (requiere autenticación)

#### Ejemplo de uso del chat:
```json
// Request
{
  "message": "He ido a la tienda y compre dos manzanas."
}

// Response
{
  "reply": "Corrección: 'Fui a la tienda y compré dos manzanas.'\n\n**Regla:** En español, para acciones pasadas y terminadas, usamos el Pretérito Perfecto Simple..."
}
```

---

## 🛠️ Tecnologías Utilizadas

### Backend
- **Django 5.2.6** - Framework web principal
- **Django REST Framework** - API REST
- **LangChain** - Orquestación de IA
- **JWT** - Autenticación segura
- **SQLite** - Base de datos (por defecto)

### Frontend
- **React 18.3.1** - Biblioteca de UI
- **Vite 7.1.7** - Herramienta de desarrollo
- **Three.js** - Efectos visuales 3D
- **Axios** - Cliente HTTP
- **React Router** - Navegación

---

## 📱 Guía de Uso

### 1. **Registro de Usuario**
1. Accede a http://localhost:5173
2. Haz clic en "Registrarse"
3. Completa el formulario con tus datos
4. Confirma tu registro

### 2. **Inicio de Sesión**
1. Ingresa tus credenciales en la página de login
2. El sistema te redirigirá al chat principal
3. ¡Ya puedes empezar a chatear con Chipi!

### 3. **Interacción con el Tutor**
1. Escribe mensajes en español en el chat
2. Chipi corregirá tus errores y te enseñará
3. Practica con los ejercicios que te proponga
4. ¡Mejora tu español de forma divertida!

---

## 🔧 Configuración Avanzada

### Variables de Entorno (Opcional)

#### Backend (.env en raíz):
```env
DEBUG=True
SECRET_KEY=tu-clave-secreta-aqui
DATABASE_URL=sqlite:///db.sqlite3
```

#### Frontend (.env en frontend-zaith-chipi/):
```env
VITE_API_URL=http://localhost:8000/api
VITE_APP_NAME=ZAITH-CHIPI
```

### Configuración de Base de Datos

Por defecto usa SQLite, pero puedes configurar PostgreSQL o MySQL:

```python
# En config/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'zaith_chipi_db',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## 🐛 Solución de Problemas

### Backend no inicia
```bash
# Verificar dependencias
pip install -r requirements.txt

# Aplicar migraciones
python manage.py migrate

# Verificar puerto
python manage.py runserver 8001  # Usar puerto alternativo
```

### Frontend no inicia
```bash
# Limpiar node_modules
rm -rf node_modules package-lock.json
npm install

# Usar puerto alternativo
npm run dev -- --port 3000
```

### Error de conexión entre frontend y backend
1. Verifica que ambos servidores estén ejecutándose
2. Revisa las URLs en el código del frontend
3. Confirma la configuración de CORS en Django

### Problemas de autenticación
1. Verifica que el token JWT no haya expirado
2. Limpia el localStorage del navegador
3. Revisa la configuración JWT en settings.py

---

## 📁 Estructura Detallada del Proyecto

```
ZAITH-CHIPI/
├── 📁 MASCOTA/
│   └── LLAMA.png                    # Avatar de Chipi
├── 📁 chat_tutor/                   # Aplicación del tutor IA
│   ├── views.py                     # Endpoints del chat
│   ├── services.py                  # Lógica de negocio
│   ├── graph.py                     # Grafo de estados LangChain
│   └── models.py                    # Modelos de conversación
├── 📁 config/                       # Configuración Django
│   ├── settings.py                  # Configuración principal
│   └── urls.py                      # URLs principales
├── 📁 core/                         # Autenticación y modelos base
│   ├── views.py                     # Login/Register
│   ├── models.py                    # Modelo de Usuario
│   └── serializers.py               # Serializadores DRF
├── 📁 frontend-zaith-chipi/         # Aplicación React
│   ├── 📁 src/
│   │   ├── 📁 components/           # Componentes React
│   │   ├── 📁 pages/                # Páginas principales
│   │   ├── 📁 services/             # Servicios API
│   │   └── 📁 styles/               # Estilos CSS
│   ├── package.json                 # Dependencias Node.js
│   └── README.md                    # Documentación frontend
├── 📄 manage.py                     # Comando Django
├── 📄 requirements.txt              # Dependencias Python
├── 📄 db.sqlite3                    # Base de datos SQLite
└── 📄 README.md                     # Este archivo
```

---

## 🚀 Scripts de Desarrollo

### Backend
```bash
# Servidor de desarrollo
python manage.py runserver

# Migraciones
python manage.py makemigrations
python manage.py migrate

# Shell interactivo
python manage.py shell

# Crear superusuario
python manage.py createsuperuser

# Ejecutar tests
python manage.py test
```

### Frontend
```bash
# Servidor de desarrollo
npm run dev

# Build para producción
npm run build

# Preview de producción
npm run preview

# Linter
npm run lint
```

---

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

## 🆘 Soporte y Contacto

Si encuentras algún problema:

1. 📖 Revisa esta documentación
2. 🔍 Busca en los Issues del repositorio
3. 🆕 Crea un nuevo Issue con detalles del problema
4. 📧 Contacta al equipo de desarrollo

---

## 🎯 Roadmap y Próximas Funcionalidades

- [ ] 🌙 Modo oscuro/claro
- [ ] 🗣️ Reconocimiento de voz
- [ ] 📊 Sistema de progreso del usuario
- [ ] 🎮 Ejercicios interactivos gamificados
- [ ] 🌍 Soporte para más idiomas
- [ ] 📱 Aplicación móvil nativa
- [ ] 🤖 Integración con más modelos de IA
- [ ] 📈 Analytics y métricas de aprendizaje

---

**¡Disfruta aprendiendo español con Chipi! 🦙✨**

*Desarrollado con ❤️ para la comunidad de aprendizaje de idiomas*
