import { useQuery } from '@tanstack/react-query';
import api from '../services/api';

export const useProjects = () => {
  const { data: projects } = useQuery(['projects'], () => api.get('/projects').then(res => res.data));
  return { projects };
};
