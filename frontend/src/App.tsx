import React, { useState } from 'react';
import './App.css';
import { BASE_API_URL } from './constants';  // Adjust the import path if necessary

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
        setMessages(prevMessages => [...prevMessages, { text: question, sender: 'user' }]);
        setLoading(true);
        setError('');

        try {
            // Fetch the response from the backend
            const response = await fetch(`${BASE_API_URL}/query`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ question }),
            });
            const data = await response.json();

            // Create new messages array including the user's question and bot's response
            const newMessages: Message[] = [
                { text: data.result, sender: 'bot' }
            ];

            // If the response is "I don't know.", add an extra prompt for rephrasing
            if (data.result.toLowerCase() === "i don't know.") {
                newMessages.push({
                    text: "Try rephrasing your question or using prompt engineering to improve clarity.",
                    sender: 'bot'
                });
            }

            // Update messages with the new responses
            setMessages(prevMessages => [...prevMessages, ...newMessages]);
        } catch (err) {
            setError('Failed to fetch response. Please try again later.');
        } finally {
            setLoading(false);
            setQuestion('');
        }
    };

    return (
        <div className="app-container">
            <h1 className="chat-heading">
                RAG Chatbot: Data from Christmas Research Results and Sustainability Research Results
            </h1>
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
