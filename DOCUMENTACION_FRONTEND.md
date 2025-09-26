# 📋 DOCUMENTACIÓN COMPLETA DEL FRONTEND - ZAITH-CHIPI

## 🎯 DESCRIPCIÓN DEL PROYECTO

**ZAITH-CHIPI** es una aplicación web moderna de corrección de textos que utiliza inteligencia artificial para ayudar a los usuarios a mejorar su escritura. El frontend está desarrollado con **React 18** y **TypeScript**, proporcionando una interfaz de usuario intuitiva y responsive.

### Características Principales
- ✅ **Autenticación JWT** con renovación automática de tokens
- ✅ **Interfaz responsive** con Chakra UI
- ✅ **Corrección de textos en tiempo real** con IA
- ✅ **Historial y progreso** del usuario
- ✅ **Feedback personalizado** del tutor virtual
- ✅ **Arquitectura modular** con TypeScript

---

## 🏗️ ARQUITECTURA DEL FRONTEND

### Stack Tecnológico

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| **React** | 18.2.0 | Framework principal de UI |
| **TypeScript** | 5.0.0 | Tipado estático y mejor DX |
| **Chakra UI** | 2.10.9 | Sistema de componentes y diseño |
| **React Router** | 6.30.1 | Navegación y rutas |
| **Axios** | 1.6.2 | Cliente HTTP para API |
| **Framer Motion** | 10.16.16 | Animaciones y transiciones |
| **React Icons** | 4.12.0 | Iconografía |
| **Recharts** | 2.8.0 | Gráficos y visualización de datos |

### Estructura del Proyecto

```
src/
├── components/           # Componentes reutilizables
│   ├── auth/            # Componentes de autenticación
│   │   ├── LoginForm.tsx
│   │   └── RegisterForm.tsx
│   ├── chat/            # Componentes del chat/corrección
│   │   ├── ChatInterface.tsx
│   │   ├── MessageBubble.tsx
│   │   └── TextInput.tsx
│   ├── layout/          # Componentes de layout
│   │   ├── Header.tsx
│   │   ├── Sidebar.tsx
│   │   └── Layout.tsx
│   ├── progress/        # Componentes de progreso
│   │   ├── ProgressChart.tsx
│   │   ├── StatCard.tsx
│   │   └── MessageHistory.tsx
│   └── ui/              # Componentes UI básicos
│       ├── LoadingSpinner.tsx
│       └── ErrorBoundary.tsx
├── contexts/            # Contextos de React
│   └── AuthContext.tsx  # Contexto de autenticación
├── hooks/               # Custom hooks
│   └── useAuth.ts       # Hook de autenticación
├── pages/               # Páginas principales
│   ├── DashboardPage.tsx
│   ├── LoginPage.tsx
│   ├── ProgressPage.tsx
│   └── RegisterPage.tsx
├── services/            # Servicios y API
│   ├── api.ts           # Configuración de Axios
│   ├── authService.ts   # Servicio de autenticación
│   └── messageService.ts # Servicio de mensajes
├── types/               # Definiciones de tipos
│   └── global.d.ts      # Tipos globales
├── App.tsx              # Componente principal
└── index.tsx            # Punto de entrada
```

---

## 🔐 SISTEMA DE AUTENTICACIÓN

### AuthContext (`src/contexts/AuthContext.tsx`)

El contexto de autenticación maneja el estado global del usuario y proporciona métodos para login, registro y logout.

**Interfaz del Usuario:**
```typescript
interface User {
  id: number;
  username: string;
  email: string;
}
```

**Métodos disponibles:**
- `login(credentials)` - Iniciar sesión
- `register(userData)` - Registrar nuevo usuario
- `logout()` - Cerrar sesión
- `isAuthenticated` - Estado de autenticación
- `isLoading` - Estado de carga

### AuthService (`src/services/authService.ts`)

Servicio que maneja las peticiones HTTP relacionadas con autenticación:

```typescript
interface RegisterData {
  username: string;
  password: string;
  email?: string;
}

interface LoginCredentials {
  username: string;
  password: string;
}
```

**Funcionalidades:**
- ✅ Registro de usuarios con validación
- ✅ Login con JWT tokens
- ✅ Renovación automática de tokens
- ✅ Manejo de errores de Django
- ✅ Almacenamiento seguro en localStorage

---

## 🌐 CONFIGURACIÓN DE API

### API Service (`src/services/api.ts`)

Cliente HTTP configurado con Axios que incluye:

**Configuración Base:**
```typescript
const API_BASE_URL = 'http://localhost:8000/api/';
```

**Interceptores:**
- **Request Interceptor**: Inyecta automáticamente el token JWT
- **Response Interceptor**: Maneja renovación de tokens y errores 401

**Características:**
- ✅ Renovación automática de tokens expirados
- ✅ Cola de peticiones durante renovación
- ✅ Manejo centralizado de errores
- ✅ Headers automáticos de autorización

### Message Service (`src/services/messageService.ts`)

Servicio para el manejo de mensajes y correcciones:

```typescript
interface Message {
  id: number;
  user: string;
  original_text: string;
  corrected_text: string | null;
  feedback: string | null;
  created_at: string;
}
```

**Métodos:**
- `sendMessage(text)` - Enviar texto para corrección
- `getMessages()` - Obtener historial de mensajes
- `pollForUpdates()` - Polling para actualizaciones en tiempo real

---

## 📱 PÁGINAS Y COMPONENTES

### 1. Página de Registro (`src/pages/RegisterPage.tsx`)

**Componente:** `RegisterForm`
- Formulario con validación en tiempo real
- Campos: username, email, password
- Manejo de errores específicos de Django
- Redirección automática después del registro

### 2. Página de Login (`src/pages/LoginPage.tsx`)

**Componente:** `LoginForm`
- Autenticación con credenciales
- Recordar sesión
- Manejo de errores de autenticación
- Redirección al dashboard

### 3. Dashboard Principal (`src/pages/DashboardPage.tsx`)

**Componentes principales:**
- `ChatInterface` - Interfaz de corrección de textos
- `MessageHistory` - Historial reciente
- `StatCard` - Estadísticas del usuario

**Funcionalidades:**
- ✅ Envío de textos para corrección
- ✅ Polling automático para actualizaciones
- ✅ Visualización de correcciones en tiempo real
- ✅ Feedback del tutor virtual

### 4. Página de Progreso (`src/pages/ProgressPage.tsx`)

**Componentes:**
- `ProgressChart` - Gráficos de progreso con Recharts
- `MessageHistory` - Historial completo
- `StatCard` - Métricas y estadísticas

**Métricas mostradas:**
- Total de mensajes enviados
- Mensajes corregidos
- Tasa de mejora
- Progreso temporal

---

## 🎨 SISTEMA DE DISEÑO

### Chakra UI Configuration

**Tema personalizado:**
- **Colores primarios:** Azul profundo (#1A202C)
- **Colores secundarios:** Verde tutor (#48BB78)
- **Colores de acento:** Naranja energético (#ED8936)

**Componentes estilizados:**
- Formularios con validación visual
- Botones con estados de carga
- Cards con sombras y bordes redondeados
- Layout responsive con breakpoints

### Responsive Design

**Breakpoints:**
- **Mobile:** < 768px
- **Tablet:** 768px - 1024px
- **Desktop:** > 1024px

**Características responsive:**
- Navigation adaptativa (hamburger menu en mobile)
- Grid layouts que se adaptan al tamaño de pantalla
- Tipografía escalable
- Espaciado proporcional

---

## 🔄 GESTIÓN DE ESTADO

### Context API

**AuthContext:**
- Estado global de autenticación
- Información del usuario
- Estados de carga

**Patrón de estado:**
```typescript
interface AuthState {
  user: User | null;
  isAuthenticated: boolean;
  isLoading: boolean;
}
```

### Local State Management

**useState para:**
- Estados de formularios
- Estados de carga locales
- Datos temporales de componentes

**useEffect para:**
- Efectos de montaje
- Polling de datos
- Cleanup de recursos

---

## 🚀 OPTIMIZACIONES DE RENDIMIENTO

### Code Splitting

- Lazy loading de páginas con `React.lazy()`
- Suspense boundaries para carga progresiva
- Chunks optimizados por ruta

### Memoización

- `useCallback` para funciones estables
- `useMemo` para cálculos costosos
- `React.memo` para componentes puros

### Polling Inteligente

- Polling condicional basado en actividad del usuario
- Cleanup automático al desmontar componentes
- Manejo de errores en polling

---

## 🧪 TESTING

### Configuración de Testing

**Herramientas:**
- Jest para unit tests
- React Testing Library para integration tests
- @testing-library/user-event para interacciones

**Cobertura de tests:**
- Componentes de autenticación
- Servicios de API
- Hooks personalizados
- Flujos de usuario críticos

---

## 🔧 SCRIPTS DISPONIBLES

```bash
# Desarrollo
npm start          # Inicia servidor de desarrollo en http://localhost:3000

# Construcción
npm run build      # Construye la aplicación para producción

# Testing
npm test           # Ejecuta tests en modo watch
npm run test:coverage  # Ejecuta tests con reporte de cobertura

# Linting y formato
npm run lint       # Ejecuta ESLint
npm run format     # Formatea código con Prettier
```

---

## 🌍 VARIABLES DE ENTORNO

### Configuración (.env)

```bash
# API Configuration
REACT_APP_API_BASE_URL=http://localhost:8000/api/

# Environment
REACT_APP_ENVIRONMENT=development

# Features flags
REACT_APP_ENABLE_POLLING=true
REACT_APP_POLLING_INTERVAL=5000
```

---

## 🔒 SEGURIDAD

### Medidas de Seguridad Implementadas

1. **JWT Token Management:**
   - Tokens almacenados en localStorage
   - Renovación automática antes de expiración
   - Logout automático en tokens inválidos

2. **Validación de Datos:**
   - Validación en frontend y backend
   - Sanitización de inputs
   - Manejo seguro de errores

3. **CORS Configuration:**
   - Configuración específica para dominios permitidos
   - Headers de seguridad apropiados

4. **Route Protection:**
   - Rutas protegidas con autenticación
   - Redirección automática para usuarios no autenticados

---

## 🐛 MANEJO DE ERRORES

### Error Boundaries

- Captura de errores de React
- Fallback UI para errores críticos
- Logging de errores para debugging

### API Error Handling

- Manejo centralizado en interceptores de Axios
- Mensajes de error user-friendly
- Retry automático para errores de red

### Validation Errors

- Validación en tiempo real en formularios
- Mensajes de error específicos de Django
- Estados de error visuales con Chakra UI

---

## 📊 MÉTRICAS Y ANALYTICS

### Performance Monitoring

- Web Vitals integrados
- Métricas de carga de componentes
- Monitoreo de errores de JavaScript

### User Analytics

- Tracking de interacciones del usuario
- Métricas de uso de funcionalidades
- Análisis de flujos de conversión

---

## 🚀 DEPLOYMENT

### Build Process

1. **Optimización automática:**
   - Minificación de JavaScript y CSS
   - Optimización de imágenes
   - Tree shaking para eliminar código no usado

2. **Assets:**
   - Hashing de archivos para cache busting
   - Compresión gzip
   - Service worker para caching

### Production Considerations

- Variables de entorno para producción
- HTTPS obligatorio
- CSP headers configurados
- Monitoring y logging

---

## 🔄 INTEGRACIÓN CON BACKEND

### API Endpoints Utilizados

| Endpoint | Método | Propósito |
|----------|--------|-----------|
| `/register/` | POST | Registro de usuarios |
| `/login/` | POST | Autenticación |
| `/token/refresh/` | POST | Renovación de tokens |
| `/send-message/` | POST | Envío de textos |
| `/progress/` | GET | Historial de mensajes |

### Data Flow

1. **Autenticación:** Frontend → Django → JWT Response
2. **Envío de mensaje:** Frontend → Django → IA Processing → Response
3. **Polling:** Frontend → Django → Updated Message Status
4. **Progreso:** Frontend → Django → User Statistics

---

## 📚 RECURSOS Y DOCUMENTACIÓN

### Enlaces Útiles

- [React Documentation](https://react.dev/)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [Chakra UI Components](https://chakra-ui.com/docs/components)
- [React Router Guide](https://reactrouter.com/en/main)
- [Axios Documentation](https://axios-http.com/docs/intro)

### Convenciones de Código

- **Naming:** PascalCase para componentes, camelCase para variables
- **File Structure:** Un componente por archivo
- **Imports:** Absolute imports configurados
- **TypeScript:** Strict mode habilitado

---

## 🤝 CONTRIBUCIÓN

### Guía para Desarrolladores

1. **Setup inicial:**
   ```bash
   npm install
   npm start
   ```

2. **Antes de hacer commit:**
   ```bash
   npm run lint
   npm test
   npm run build
   ```

3. **Estructura de commits:**
   - feat: nueva funcionalidad
   - fix: corrección de bugs
   - docs: documentación
   - style: formato de código
   - refactor: refactoring
   - test: tests

### Code Review Checklist

- [ ] TypeScript sin errores
- [ ] Tests pasando
- [ ] Componentes responsive
- [ ] Accesibilidad considerada
- [ ] Performance optimizado
- [ ] Documentación actualizada

---

**Última actualización:** Septiembre 2025  
**Versión del frontend:** 1.0.0  
**Compatibilidad:** React 18+, TypeScript 5+