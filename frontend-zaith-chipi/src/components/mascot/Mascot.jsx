import React, { useState } from 'react';
import LlamaImage from '../../assets/images/LLAMA.png';
import './Mascot.css';

function Mascot() {
  const [isShaking, setIsShaking] = useState(false);

  const handleLlamaClick = () => {
    setIsShaking(true);
    // Quita la clase después de que termine la animación (500ms)
    setTimeout(() => {
      setIsShaking(false);
    }, 500);
  };

  return (
    <div className="mascot-container">
      <img
        src={LlamaImage}
        alt="Mascota Chipi, la Llama"
        className={`mascot-image ${isShaking ? 'shake' : ''}`}
        onClick={handleLlamaClick}
      />
      <div className="mascot-platform"></div>
    </div>
  );
}

export default Mascot;