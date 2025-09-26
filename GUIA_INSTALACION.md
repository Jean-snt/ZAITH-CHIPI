# 🚀 GUÍA DE INSTALACIÓN Y CONFIGURACIÓN - ZAITH-CHIPI

## 📋 DESCRIPCIÓN DEL PROYECTO

**ZAITH-CHIPI** es una aplicación web completa de corrección de textos con IA que consta de:
- **Backend:** Django REST Framework con autenticación JWT
- **Frontend:** React 18 + TypeScript + Chakra UI
- **Base de datos:** SQLite (desarrollo) / PostgreSQL (producción)
- **IA:** Integración con servicios de procesamiento de lenguaje natural

---

## 🔧 REQUISITOS DEL SISTEMA

### Software Necesario

| Componente | Versión Mínima | Versión Recomendada |
|------------|----------------|---------------------|
| **Python** | 3.8+ | 3.11+ |
| **Node.js** | 16.0+ | 18.0+ |
| **npm** | 8.0+ | 9.0+ |
| **Git** | 2.0+ | Última versión |

### Sistemas Operativos Soportados
- ✅ Windows 10/11
- ✅ macOS 10.15+
- ✅ Ubuntu 20.04+
- ✅ Debian 11+

---

## 📁 ESTRUCTURA DEL PROYECTO

```
TRADUCTOR_MCP/
├── ZAITH-CHIPI/                    # Proyecto principal Django
│   ├── config/                     # Configuración Django
│   │   ├── __init__.py
│   │   ├── settings.py            # Configuración principal
│   │   ├── urls.py                # URLs principales
│   │   └── wsgi.py                # WSGI para producción
│   ├── core/                      # Aplicación principal
│   │   ├── migrations/            # Migraciones de base de datos
│   │   ├── __init__.py
│   │   ├── admin.py               # Panel de administración
│   │   ├── apps.py                # Configuración de la app
│   │   ├── models.py              # Modelos de datos
│   │   ├── serializers.py         # Serializadores DRF
│   │   ├── urls.py                # URLs de la aplicación
│   │   └── views.py               # Vistas y API endpoints
│   ├── frontend/                  # Aplicación React (ÚNICA UBICACIÓN)
│   │   ├── public/                # Archivos públicos
│   │   ├── src/                   # Código fuente React
│   │   │   ├── components/        # Componentes reutilizables
│   │   │   ├── contexts/          # Contextos de React
│   │   │   ├── hooks/             # Hooks personalizados
│   │   │   ├── pages/             # Páginas principales
│   │   │   ├── services/          # Servicios API
│   │   │   ├── types/             # Tipos TypeScript
│   │   │   ├── App.tsx            # Componente principal
│   │   │   └── index.tsx          # Punto de entrada
│   │   ├── node_modules/          # Dependencias instaladas
│   │   ├── package.json           # Dependencias React
│   │   └── tsconfig.json          # Configuración TypeScript
│   ├── manage.py                  # Script de gestión Django
│   └── requirements.txt           # Dependencias Python
├── DOCUMENTACION_FRONTEND.md       # Documentación del frontend
├── API_INTEGRATION.md              # Documentación de integración API
├── GUIA_INSTALACION.md            # Esta guía
└── README.md                      # Información general
```

> **⚠️ Nota Importante**: La estructura ha sido optimizada para eliminar duplicaciones. El frontend React se encuentra únicamente en `ZAITH-CHIPI/frontend/` y no hay carpetas `node_modules` duplicadas.

---

## 🛠️ INSTALACIÓN PASO A PASO

### 1. Clonar el Repositorio

```bash
# Clonar el proyecto
git clone <URL_DEL_REPOSITORIO>
cd TRADUCTOR_MCP
```

### 2. Configuración del Backend (Django)

#### 2.1 Crear Entorno Virtual

```bash
# Navegar al directorio del backend
cd ZAITH-CHIPI

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
```

#### 2.2 Instalar Dependencias

```bash
# Instalar dependencias de Python
pip install -r requirements.txt
```

**Dependencias principales incluidas:**
- Django 4.2.7
- djangorestframework 3.14.0
- djangorestframework-simplejwt 5.3.0
- django-cors-headers 4.3.1
- mysqlclient 2.2.0
- psycopg2-binary 2.9.9

#### 2.3 Configurar Base de Datos

```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario (opcional)
python manage.py createsuperuser
```

#### 2.4 Configurar Variables de Entorno

Crear archivo `.env` en `ZAITH-CHIPI/`:

```bash
# Configuración de Django
SECRET_KEY=tu_clave_secreta_muy_segura_aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Base de datos (SQLite por defecto)
DATABASE_URL=sqlite:///db.sqlite3

# JWT Configuration
JWT_SECRET_KEY=tu_jwt_secret_key_aqui
JWT_ACCESS_TOKEN_LIFETIME=60  # minutos
JWT_REFRESH_TOKEN_LIFETIME=1440  # minutos (24 horas)

# CORS Configuration
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

#### 2.5 Iniciar Servidor Backend

```bash
# Iniciar servidor de desarrollo
python manage.py runserver

# El servidor estará disponible en: http://127.0.0.1:8000/
```

### 3. Configuración del Frontend (React)

#### 3.1 Instalar Dependencias

```bash
# Volver al directorio raíz
cd ..

# Instalar dependencias de Node.js
npm install
```

**Dependencias principales incluidas:**
- React 18.2.0
- TypeScript 5.0.0
- Chakra UI 2.10.9
- React Router 6.30.1
- Axios 1.6.2
- Framer Motion 10.16.16

#### 3.2 Configurar Variables de Entorno

Crear archivo `.env` en la raíz del proyecto:

```bash
# API Configuration
REACT_APP_API_BASE_URL=http://localhost:8000/api/

# Environment
REACT_APP_ENVIRONMENT=development

# Features
REACT_APP_ENABLE_POLLING=true
REACT_APP_POLLING_INTERVAL=5000
```

#### 3.3 Iniciar Servidor Frontend

```bash
# Iniciar servidor de desarrollo
npm start

# La aplicación estará disponible en: http://localhost:3000/
```

---

## 🔧 CONFIGURACIÓN AVANZADA

### Configuración de Base de Datos PostgreSQL (Producción)

#### 1. Instalar PostgreSQL

```bash
# Ubuntu/Debian
sudo apt-get install postgresql postgresql-contrib

# macOS (con Homebrew)
brew install postgresql

# Windows: Descargar desde https://www.postgresql.org/download/windows/
```

#### 2. Configurar Base de Datos

```sql
-- Conectar a PostgreSQL
sudo -u postgres psql

-- Crear base de datos
CREATE DATABASE zaith_chipi;

-- Crear usuario
CREATE USER zaith_user WITH PASSWORD 'tu_password_seguro';

-- Otorgar permisos
GRANT ALL PRIVILEGES ON DATABASE zaith_chipi TO zaith_user;

-- Salir
\q
```

#### 3. Actualizar settings.py

```python
# En ZAITH-CHIPI/config/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'zaith_chipi',
        'USER': 'zaith_user',
        'PASSWORD': 'tu_password_seguro',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Configuración de Redis (Cache y Sesiones)

#### 1. Instalar Redis

```bash
# Ubuntu/Debian
sudo apt-get install redis-server

# macOS
brew install redis

# Windows: Usar Docker o WSL
```

#### 2. Configurar en Django

```python
# Agregar a requirements.txt
redis==4.5.1
django-redis==5.2.0

# En settings.py
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
```

---

## 🚀 SCRIPTS DE AUTOMATIZACIÓN

### Backend Scripts

Crear archivo `scripts/backend.sh`:

```bash
#!/bin/bash
# Script para inicializar backend

echo "🚀 Iniciando configuración del backend..."

# Activar entorno virtual
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Migraciones
python manage.py makemigrations
python manage.py migrate

# Recopilar archivos estáticos
python manage.py collectstatic --noinput

# Iniciar servidor
python manage.py runserver

echo "✅ Backend configurado y ejecutándose en http://127.0.0.1:8000/"
```

### Frontend Scripts

Crear archivo `scripts/frontend.sh`:

```bash
#!/bin/bash
# Script para inicializar frontend

echo "🚀 Iniciando configuración del frontend..."

# Instalar dependencias
npm install

# Verificar configuración
npm run lint

# Ejecutar tests
npm test -- --watchAll=false

# Iniciar servidor de desarrollo
npm start

echo "✅ Frontend configurado y ejecutándose en http://localhost:3000/"
```

### Script de Instalación Completa

Crear archivo `install.sh`:

```bash
#!/bin/bash
# Script de instalación completa

echo "🎯 INSTALACIÓN COMPLETA DE ZAITH-CHIPI"
echo "======================================"

# Verificar requisitos
echo "📋 Verificando requisitos del sistema..."

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 no está instalado"
    exit 1
fi

# Verificar Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js no está instalado"
    exit 1
fi

echo "✅ Requisitos del sistema verificados"

# Configurar backend
echo "🔧 Configurando backend..."
cd ZAITH-CHIPI
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
cd ..

# Configurar frontend
echo "🎨 Configurando frontend..."
npm install

echo "🎉 ¡Instalación completada!"
echo "📖 Consulta GUIA_INSTALACION.md para más detalles"
```

---

## 🧪 TESTING

### Backend Testing

```bash
# Ejecutar tests del backend
cd ZAITH-CHIPI
python manage.py test

# Tests con cobertura
pip install coverage
coverage run --source='.' manage.py test
coverage report
coverage html  # Genera reporte HTML
```

### Frontend Testing

```bash
# Ejecutar tests del frontend
npm test

# Tests con cobertura
npm run test:coverage

# Tests end-to-end (si están configurados)
npm run test:e2e
```

---

## 🔒 CONFIGURACIÓN DE SEGURIDAD

### Configuración para Producción

#### 1. Variables de Entorno de Producción

```bash
# .env para producción
SECRET_KEY=clave_super_secreta_de_produccion
DEBUG=False
ALLOWED_HOSTS=tu-dominio.com,www.tu-dominio.com

# Base de datos de producción
DATABASE_URL=postgresql://user:password@localhost:5432/zaith_chipi_prod

# CORS para producción
CORS_ALLOWED_ORIGINS=https://tu-dominio.com,https://www.tu-dominio.com
```

#### 2. Configuraciones de Seguridad Django

```python
# En settings.py para producción
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

### HTTPS y SSL

```bash
# Usando Let's Encrypt con Certbot
sudo apt-get install certbot python3-certbot-nginx
sudo certbot --nginx -d tu-dominio.com
```

---

## 🐳 DEPLOYMENT CON DOCKER

### Dockerfile para Backend

```dockerfile
# ZAITH-CHIPI/Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

### Dockerfile para Frontend

```dockerfile
# Dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "start"]
```

### Docker Compose

```yaml
# docker-compose.yml
version: '3.8'

services:
  backend:
    build: ./ZAITH-CHIPI
    ports:
      - "8000:8000"
    environment:
      - DEBUG=True
    volumes:
      - ./ZAITH-CHIPI:/app
    depends_on:
      - db

  frontend:
    build: .
    ports:
      - "3000:3000"
    volumes:
      - .:/app
      - /app/node_modules
    depends_on:
      - backend

  db:
    image: postgres:13
    environment:
      POSTGRES_DB: zaith_chipi
      POSTGRES_USER: zaith_user
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

---

## 🔧 TROUBLESHOOTING

### Problemas Comunes

#### 1. Error de CORS

**Síntoma:** Requests bloqueados por CORS policy
**Solución:**
```python
# Verificar en settings.py
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
CORS_ALLOW_CREDENTIALS = True
```

#### 2. Error de JWT Token

**Síntoma:** Token inválido o expirado
**Solución:**
```bash
# Limpiar localStorage en el navegador
# O reiniciar ambos servidores
```

#### 3. Error de Base de Datos

**Síntoma:** Database locked o connection error
**Solución:**
```bash
# Recrear base de datos
rm db.sqlite3
python manage.py migrate
```

#### 4. Error de Dependencias

**Síntoma:** Module not found
**Solución:**
```bash
# Backend
pip install -r requirements.txt

# Frontend
rm -rf node_modules
npm install
```

### Logs y Debugging

#### Backend Logs

```python
# En settings.py para debugging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
```

#### Frontend Debugging

```bash
# Habilitar debugging en React
REACT_APP_DEBUG=true npm start

# Ver logs en consola del navegador
# Usar React Developer Tools
```

---

## 📊 MONITOREO Y MANTENIMIENTO

### Health Checks

#### Backend Health Check

```python
# En core/views.py
from django.http import JsonResponse

def health_check(request):
    return JsonResponse({
        'status': 'healthy',
        'timestamp': timezone.now(),
        'version': '1.0.0'
    })
```

#### Frontend Health Check

```typescript
// En src/services/healthService.ts
export const checkHealth = async () => {
  try {
    const response = await api.get('/health/');
    return response.data;
  } catch (error) {
    throw new Error('Health check failed');
  }
};
```

### Backup y Restauración

```bash
# Backup de base de datos
python manage.py dumpdata > backup.json

# Restaurar base de datos
python manage.py loaddata backup.json

# Backup de archivos estáticos
tar -czf static_backup.tar.gz static/
```

---

## 🚀 PRÓXIMOS PASOS

### Después de la Instalación

1. **✅ Verificar funcionamiento:**
   - Registrar un usuario de prueba
   - Enviar un mensaje para corrección
   - Verificar el historial de progreso

2. **🔧 Personalizar configuración:**
   - Ajustar variables de entorno
   - Configurar base de datos de producción
   - Personalizar tema de Chakra UI

3. **📈 Optimizar rendimiento:**
   - Configurar cache con Redis
   - Implementar CDN para assets
   - Optimizar queries de base de datos

4. **🔒 Reforzar seguridad:**
   - Configurar HTTPS
   - Implementar rate limiting
   - Configurar monitoring

### Recursos Adicionales

- 📖 [Documentación del Frontend](./DOCUMENTACION_FRONTEND.md)
- 🌐 [Django REST Framework Docs](https://www.django-rest-framework.org/)
- ⚛️ [React Documentation](https://react.dev/)
- 🎨 [Chakra UI Components](https://chakra-ui.com/)

---

## 🤝 SOPORTE

### Contacto y Ayuda

- **Documentación:** Consultar archivos .md del proyecto
- **Issues:** Reportar problemas en el repositorio
- **Contribuciones:** Fork y pull requests bienvenidos

### Checklist de Verificación

- [ ] Python 3.8+ instalado
- [ ] Node.js 16+ instalado
- [ ] Backend ejecutándose en puerto 8000
- [ ] Frontend ejecutándose en puerto 3000
- [ ] Base de datos migrada correctamente
- [ ] CORS configurado
- [ ] Variables de entorno configuradas
- [ ] Tests pasando
- [ ] Registro de usuario funcional
- [ ] Envío de mensajes funcional

---

**Última actualización:** Septiembre 2025  
**Versión:** 1.0.0  
**Compatibilidad:** Python 3.8+, Node.js 16+