import React, { createContext, useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { loginUser as loginApi, registerUser as registerApi } from '../services/apiService';
import { jwtDecode } from 'jwt-decode'; // Necesitaremos esta librería

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [authTokens, setAuthTokens] = useState(() => 
    localStorage.getItem('authTokens')
      ? JSON.parse(localStorage.getItem('authTokens'))
      : null
  );
  const navigate = useNavigate();

  const login = async (username, password) => {
    try {
      const response = await loginApi({ username, password });
      if (response.status === 200) {
        setAuthTokens(response.data);
        setUser(jwtDecode(response.data.access));
        localStorage.setItem('authTokens', JSON.stringify(response.data));
        navigate('/');
      }
    } catch (error) {
      console.error("Error en el login:", error);
      alert("Usuario o contraseña incorrectos.");
    }
  };
  
  const register = async (username, email, password) => {
    try {
      const response = await registerApi({ username, email, password });
      if (response.status === 201) {
        alert("Usuario registrado con éxito. Por favor, inicia sesión.");
        navigate('/login');
      }
    } catch (error) {
        console.error("Error en el registro:", error);
        alert("Error en el registro. Es posible que el usuario ya exista.");
    }
  };

  const logout = () => {
    setAuthTokens(null);
    setUser(null);
    localStorage.removeItem('authTokens');
    navigate('/login');
  };

  useEffect(() => {
    if (authTokens) {
      setUser(jwtDecode(authTokens.access));
    }
  }, [authTokens]);
  
  const contextData = {
    user,
    login,
    register,
    logout,
  };

  return (
    <AuthContext.Provider value={contextData}>
      {children}
    </AuthContext.Provider>
  );
};

export default AuthContext;