import React from 'react';
import Navbar from './Navbar';

function Layout({ children }) {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', minHeight: '100vh' }}>
      <Navbar />
      <main style={{ flex: 1, width: '100%', maxWidth: '900px', margin: '0 auto', padding: '2rem', height: '100%' }}>
        {children}
      </main>
    </div>
  );
}

export default Layout;