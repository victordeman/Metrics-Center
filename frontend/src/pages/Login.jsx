import React from 'react';
import AuthForm from '../components/AuthForm';
import { useAuth } from '../hooks/useAuth';

const Login = () => {
  const { login } = useAuth();

  return (
    <div className="flex justify-center items-center h-screen">
      <AuthForm onSubmit={login} buttonText="Login" />
    </div>
  );
};

export default Login;
