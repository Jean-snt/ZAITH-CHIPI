# 🦙 ZAITH-CHIPI Frontend

## 📋 Descripción

Frontend de la aplicación **ZAITH-CHIPI**, un tutor interactivo de español potenciado por inteligencia artificial. Esta aplicación web moderna está construida con **React + Vite** y ofrece una experiencia de usuario inmersiva con efectos visuales avanzados y una interfaz de chat intuitiva.

## ✨ Características

- 🎨 **Interfaz moderna** con efectos visuales y animaciones
- 🦙 **Avatar interactivo** de la mascota Chipi
- 💬 **Chat en tiempo real** con IA para aprendizaje de español
- 🔐 **Sistema de autenticación** JWT
- 📱 **Diseño responsivo** para todos los dispositivos
- 🌟 **Efectos visuales avanzados** con Three.js

## 🛠️ Tecnologías Utilizadas

- **React 18.3.1** - Biblioteca de interfaz de usuario
- **Vite 7.1.7** - Herramienta de construcción y desarrollo
- **React Router DOM 6.25.1** - Enrutamiento
- **Axios 1.7.2** - Cliente HTTP
- **Three.js 0.166.1** - Gráficos 3D y efectos visuales
- **JWT Decode 4.0.0** - Decodificación de tokens JWT
- **React Awesome Reveal 4.2.11** - Animaciones

## 📋 Prerrequisitos

Antes de comenzar, asegúrate de tener instalado:

- **Node.js** (versión 18 o superior)
- **npm** (viene incluido con Node.js)
- **Git** (para clonar el repositorio)

### Verificar instalaciones:

```bash
node --version    # Debe mostrar v18.x.x o superior
npm --version     # Debe mostrar 8.x.x o superior
```

## 🚀 Instalación y Configuración

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd ZAITH-CHIPI/frontend-zaith-chipi
```

### 2. Instalar dependencias

```bash
npm install
```

### 3. Configurar variables de entorno (Opcional)

Crea un archivo `.env` en la raíz del frontend si necesitas configurar variables específicas:

```env
VITE_API_URL=http://localhost:8000/api
VITE_APP_NAME=ZAITH-CHIPI
```

### 4. Iniciar el servidor de desarrollo

```bash
npm run dev
```

La aplicación estará disponible en: **http://localhost:5173**

## 📁 Estructura del Proyecto

```
frontend-zaith-chipi/
├── public/                 # Archivos estáticos
├── src/
│   ├── components/        # Componentes React
│   │   ├── auth/         # Componentes de autenticación
│   │   ├── chat/         # Componentes del chat
│   │   ├── common/       # Componentes comunes
│   │   └── ui/           # Componentes de interfaz
│   ├── pages/            # Páginas principales
│   ├── services/         # Servicios y API calls
│   ├── styles/           # Archivos CSS
│   ├── utils/            # Utilidades y helpers
│   ├── App.jsx           # Componente principal
│   └── main.jsx          # Punto de entrada
├── package.json          # Dependencias y scripts
├── vite.config.js        # Configuración de Vite
└── README.md            # Este archivo
```

## 🎮 Scripts Disponibles

### Desarrollo
```bash
npm run dev          # Inicia el servidor de desarrollo
```

### Producción
```bash
npm run build        # Construye la aplicación para producción
npm run preview      # Previsualiza la build de producción
```

### Calidad de código
```bash
npm run lint         # Ejecuta ESLint para revisar el código
```

## 🔧 Configuración del Backend

Para que el frontend funcione completamente, necesitas tener el backend de Django ejecutándose:

### 1. Navegar al directorio del backend
```bash
cd ../  # Desde frontend-zaith-chipi, ir al directorio raíz
```

### 2. Instalar dependencias de Python
```bash
pip install -r requirements.txt
```

### 3. Ejecutar migraciones
```bash
python manage.py migrate
```

### 4. Crear superusuario (opcional)
```bash
python manage.py createsuperuser
```

### 5. Iniciar el servidor Django
```bash
python manage.py runserver 8000
```

## 🌐 URLs de la Aplicación

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000/api
- **Admin Django**: http://localhost:8000/admin

## 🔐 Funcionalidades de Autenticación

### Registro de Usuario
1. Accede a la página de registro
2. Completa el formulario con tus datos
3. Confirma tu cuenta (si está habilitado)

### Inicio de Sesión
1. Usa tus credenciales en la página de login
2. El sistema generará un token JWT
3. Serás redirigido al chat principal

### Chat con IA
1. Una vez autenticado, accede al chat
2. Escribe mensajes en español
3. Chipi te ayudará a mejorar tu español

## 🎨 Personalización

### Cambiar colores del tema
Edita los archivos CSS en `src/styles/` para personalizar:
- Colores principales
- Efectos de neón
- Animaciones
- Tipografía

### Modificar el avatar
Reemplaza las imágenes en `public/` o `src/assets/` para cambiar:
- Avatar de Chipi
- Iconos de la aplicación
- Imágenes de fondo

## 🐛 Solución de Problemas

### Error: "Cannot connect to backend"
- Verifica que el backend esté ejecutándose en el puerto 8000
- Revisa la configuración de CORS en Django
- Confirma que las URLs de la API sean correctas

### Error: "Module not found"
```bash
rm -rf node_modules package-lock.json
npm install
```

### Error: "Port 5173 is already in use"
```bash
npm run dev -- --port 3000  # Usar puerto alternativo
```

### Problemas de autenticación
- Verifica que el token JWT no haya expirado
- Revisa la configuración de JWT en el backend
- Limpia el localStorage del navegador

## 📱 Compatibilidad

### Navegadores soportados:
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

### Dispositivos:
- Desktop (1920x1080 recomendado)
- Tablet (768px+)
- Mobile (375px+)

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🆘 Soporte

Si encuentras algún problema o tienes preguntas:

1. Revisa la sección de **Solución de Problemas**
2. Busca en los **Issues** del repositorio
3. Crea un nuevo **Issue** con detalles del problema

## 🚀 Próximas Funcionalidades

- [ ] Modo oscuro/claro
- [ ] Más idiomas de interfaz
- [ ] Integración con más modelos de IA
- [ ] Sistema de progreso del usuario
- [ ] Ejercicios interactivos
- [ ] Reconocimiento de voz

---

**¡Disfruta aprendiendo español con Chipi! 🦙✨**
