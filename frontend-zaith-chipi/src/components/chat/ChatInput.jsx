import React, { useState } from 'react';
import './ChatInput.css';

function ChatInput({ onSendMessage, isLoading }) {
  const [inputText, setInputText] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (inputText.trim() && !isLoading) {
      onSendMessage(inputText);
      setInputText('');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="chat-input-form">
      <input
        type="text"
        className="chat-input"
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        placeholder="Escribe tu mensaje aquí..."
        disabled={isLoading}
      />
      <button type="submit" className="send-button" disabled={isLoading}>
        Enviar
      </button>
    </form>
  );
}

export default ChatInput;