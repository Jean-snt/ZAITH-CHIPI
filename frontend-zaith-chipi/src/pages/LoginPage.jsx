import React, { useState } from 'react';
import useAuth from '../hooks/useAuth';
import { Link } from 'react-router-dom';
import { Slide, JackInTheBox } from "react-awesome-reveal";
import Mascot from '../components/mascot/Mascot';
import './AuthPage.css';

function LoginPage() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const { login } = useAuth();

  const handleSubmit = (e) => {
    e.preventDefault();
    if (username && password) {
      login(username, password);
    }
  };

  return (
    <div className="auth-page-container">
      <Slide direction="left" triggerOnce>
        <div className="auth-mascot-column">
          <Mascot />
        </div>
      </Slide>
      <Slide direction="right" triggerOnce>
        <div className="auth-form-column">
          <div className="auth-form">
            <JackInTheBox triggerOnce>
              <h2>¡Qué bueno verte!</h2>
            </JackInTheBox>
            <form onSubmit={handleSubmit}>
              <div className="form-group">
                <input type="text" id="username" value={username} onChange={(e) => setUsername(e.target.value)} required placeholder="Usuario" />
              </div>
              <div className="form-group">
                <input type="password" id="password" value={password} onChange={(e) => setPassword(e.target.value)} required placeholder="Contraseña" />
              </div>
              <button type="submit" className="auth-button">Ingresar</button>
              <p className="auth-switch">
                ¿No tienes una cuenta? <Link to="/register">Regístrate aquí</Link>
              </p>
            </form>
          </div>
        </div>
      </Slide>
    </div>
  );
}

export default LoginPage;