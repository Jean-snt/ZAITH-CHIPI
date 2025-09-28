import React, { useState } from 'react';
import MessageList from '../components/chat/MessageList';
import ChatInput from '../components/chat/ChatInput';
import { sendMessageToTutor } from '../services/apiService';
import Mascot from '../components/mascot/Mascot';
import './ChatPage.css';

function ChatPage() {
  const [messages, setMessages] = useState([
    { id: 1, sender: 'ai', text: '¡Hola! Soy Chipi, tu tutor de español. Escribe una frase y la corregiré para ti.' }
  ]);
  const [isLoading, setIsLoading] = useState(false);

  const handleSendMessage = async (messageText) => {
    // Añadir mensaje del usuario a la lista
    const userMessage = { id: Date.now(), sender: 'user', text: messageText };
    setMessages(prevMessages => [...prevMessages, userMessage]);
    setIsLoading(true);

    try {
      // Enviar mensaje a la API
      const response = await sendMessageToTutor(messageText);
      const aiResponse = { id: Date.now() + 1, sender: 'ai', text: response.data.reply };
      setMessages(prevMessages => [...prevMessages, aiResponse]);
    } catch (error) {
      console.error("Error al contactar al tutor:", error);
      const errorResponse = { id: Date.now() + 1, sender: 'ai', text: "Lo siento, tuve un problema para conectarme. Inténtalo de nuevo." };
      setMessages(prevMessages => [...prevMessages, errorResponse]);
    } finally {
      setIsLoading(false);
    }
  };
  
  return (
    <div className="chat-window">
      {messages.length <= 1 && <Mascot />}
      <MessageList messages={messages} isLoading={isLoading} />
      <ChatInput onSendMessage={handleSendMessage} isLoading={isLoading} />
    </div>
  );
}

export default ChatPage;