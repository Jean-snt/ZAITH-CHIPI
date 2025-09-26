# ZAITH-CHIPI - Tutor Virtual de Español

## 📋 Descripción

ZAITH-CHIPI es una aplicación web que combina un backend Django con un frontend React TypeScript para proporcionar un tutor virtual de español que corrige textos y ofrece feedback personalizado.

## 🏗️ Estructura del Proyecto

```
TRADUCTOR_MCP/
├── ZAITH-CHIPI/          # Backend Django
│   ├── config/           # Configuración Django
│   ├── core/            # Aplicación principal
│   ├── manage.py        # Script de gestión Django
│   └── requirements.txt # Dependencias Python
├── src/                 # Frontend React TypeScript
│   ├── components/      # Componentes React
│   ├── pages/          # Páginas de la aplicación
│   ├── services/       # Servicios API
│   ├── contexts/       # Contextos React
│   └── hooks/          # Hooks personalizados
├── package.json        # Dependencias Node.js
└── tsconfig.json       # Configuración TypeScript
```

## 🚀 Instalación y Configuración

### Prerrequisitos

1. **Node.js** (versión 18 o superior)
   - Descargar desde: https://nodejs.org/
   - Verificar instalación: `node --version` y `npm --version`

2. **Python** (versión 3.8 o superior)
   - Descargar desde: https://python.org/

### Configuración del Frontend

1. **Instalar Node.js** si no está instalado
2. **Instalar dependencias del frontend**:
   ```bash
   cd c:\TRADUCTOR_MCP
   npm install
   ```

3. **Iniciar el servidor de desarrollo**:
   ```bash
   npm start
   ```

### Configuración del Backend

1. **Navegar al directorio del backend**:
   ```bash
   cd ZAITH-CHIPI
   ```

2. **Crear entorno virtual**:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # En Windows
   ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar migraciones**:
   ```bash
   python manage.py migrate
   ```

5. **Iniciar servidor Django**:
   ```bash
   python manage.py runserver
   ```

## 🔧 Solución de Problemas

### Error: "npm no se reconoce como comando"

**Causa**: Node.js no está instalado o no está en el PATH del sistema.

**Solución**:
1. Descargar e instalar Node.js desde https://nodejs.org/
2. Reiniciar la terminal/PowerShell
3. Verificar con: `node --version`

### Errores de TypeScript sobre módulos faltantes

**Causa**: Las dependencias no están instaladas.

**Solución**:
```bash
npm install
```

### Errores de tipos en AuthContext

**Causa**: Ya corregidos en la versión actual.

**Estado**: ✅ Resuelto

## 📦 Dependencias Principales

### Frontend
- React 18
- TypeScript 5
- Chakra UI
- React Router DOM
- Axios
- React Icons

### Backend
- Django
- Django REST Framework
- Django CORS Headers

## 🎯 Funcionalidades

- ✅ Sistema de autenticación JWT
- ✅ Registro y login de usuarios
- ✅ Dashboard interactivo
- ✅ Corrección de textos en tiempo real
- ✅ Historial de progreso
- ✅ Feedback personalizado del tutor virtual
- ✅ Interfaz responsive con Chakra UI

## 🔐 Seguridad

- Tokens JWT con renovación automática
- Interceptores Axios para manejo de autenticación
- Rutas protegidas en el frontend
- Validación de datos en backend y frontend

## 📱 Uso

1. **Registro**: Crear cuenta nueva en `/register`
2. **Login**: Iniciar sesión en `/login`
3. **Dashboard**: Enviar textos para corrección
4. **Progreso**: Ver historial y estadísticas en `/progress`

## 🛠️ Desarrollo

Para contribuir al proyecto:

1. Instalar todas las dependencias
2. Seguir las convenciones de código TypeScript
3. Usar Chakra UI para componentes de interfaz
4. Mantener la separación entre frontend y backend

## 📞 Soporte

Si encuentras problemas:

1. Verificar que Node.js esté instalado
2. Ejecutar `npm install` para instalar dependencias
3. Revisar los logs de la consola para errores específicos
4. Asegurarse de que el backend Django esté ejecutándose

---

**Nota**: Este proyecto requiere tanto el frontend React como el backend Django ejecutándose simultáneamente para funcionar completamente.