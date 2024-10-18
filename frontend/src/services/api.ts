// src/services/api.ts
import axios from 'axios';

const apiClient = axios.create({
    baseURL: 'http://127.0.0.1:8000/api', // Backend API base URL
    headers: {
        'Content-Type': 'application/json',
    },
});

export const submitQuery = async (question: string) => {
    try {
        const response = await apiClient.post('/query', { question });
        return response.data;
    } catch (error) {
        throw new Error('Failed to fetch the response. Please try again later.');
    }
};
