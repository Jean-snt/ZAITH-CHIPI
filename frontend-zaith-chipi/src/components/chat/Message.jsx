import React from 'react';
import LlamaAvatar from '../../assets/images/LLAMA.png'; // <-- IMPORTAMOS LA IMAGEN
import './Message.css';

function Message({ message }) {
  const { sender, text } = message;
  const isUser = sender === 'user';

  return (
    <div className={`message-row ${isUser ? 'user-message-row' : 'ai-message-row'}`}>
      {/* Renderizamos el avatar solo si el mensaje NO es del usuario */}
      {!isUser && (
        <img src={LlamaAvatar} alt="Avatar de Chipi" className="avatar-img" />
      )}
      <div className={`message-bubble ${isUser ? 'user-message' : 'ai-message'}`}>
        <p>{text}</p>
      </div>
    </div>
  );
}

export default Message;