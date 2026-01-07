import { useState } from 'react';
import { useQueryClient } from '@tanstack/react-query';
import api from '../services/api';

export const useAuth = () => {
  const [token, setToken] = useState(localStorage.getItem('token'));
  const queryClient = useQueryClient();

  const login = async (credentials) => {
    const res = await api.post('/auth/login', credentials);
    localStorage.setItem('token', res.data.access_token);
    setToken(res.data.access_token);
  };

  const register = async (credentials) => {
    const res = await api.post('/auth/register', credentials);
    localStorage.setItem('token', res.data.access_token);
    setToken(res.data.access_token);
  };

  return { token, login, register };
};
