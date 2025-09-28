import React from 'react';
import { Link } from 'react-router-dom';
import LlamaLogo from '../../assets/images/LLAMA.png';
import useAuth from '../../hooks/useAuth';
import './Navbar.css';

function Navbar() {
  const { user, logout } = useAuth();

  return (
    <nav className="navbar-container">
      <div className="navbar-logo-container">
        <img src={LlamaLogo} alt="Chipi, la llama" className="navbar-logo-img" />
        <Link to="/" className="navbar-title">Tutor de Lenguaje</Link>
      </div>
      <div className="navbar-links">
        {user ? (
          <>
            <span className="navbar-user">Hola, {user.username}</span>
            <button onClick={logout} className="navbar-logout-btn">Salir</button>
          </>
        ) : (
          <>
            <Link to="/login" className="navbar-link">Login</Link>
            <Link to="/register" className="navbar-link">Registro</Link>
          </>
        )}
      </div>
    </nav>
  );
}

export default Navbar;