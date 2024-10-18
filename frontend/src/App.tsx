// src/App.tsx
import React, { useState } from 'react';
import './App.css';

interface Message {
    text: string;
    sender: 'user' | 'bot';
}

const App: React.FC = () => {
    const [question, setQuestion] = useState('');
    const [messages, setMessages] = useState<Message[]>([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const handleQuerySubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        if (!question.trim()) return;

        // Add user's question to the chat
        setMessages([...messages, { text: question, sender: 'user' }]);
        setLoading(true);
        setError('');

        try {
            // Fetch the response from the backend
            const response = await fetch('http://127.0.0.1:8000/api/query', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ question }),
            });
            const data = await response.json();

            // Add the bot's response to the chat
            setMessages([...messages, { text: question, sender: 'user' }, { text: data.result, sender: 'bot' }]);
        } catch (err) {
            setError('Failed to fetch response. Please try again later.');
        } finally {
            setLoading(false);
            setQuestion('');
        }
    };

    return (
        <div className="app-container">
            <div className="chat-box">
                {messages.map((message, index) => (
                    <div key={index} className={`chat-bubble ${message.sender}`}>
                        <p>{message.text}</p>
                    </div>
                ))}
                {loading && <div className="loading">Thinking...</div>}
            </div>
            <form onSubmit={handleQuerySubmit} className="input-area">
                <input
                    type="text"
                    value={question}
                    onChange={(e) => setQuestion(e.target.value)}
                    placeholder="Type your question..."
                />
                <button type="submit" disabled={loading}>Send</button>
            </form>
            {error && <p className="error-message">{error}</p>}
        </div>
    );
};

export default App;
