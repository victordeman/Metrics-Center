import React from 'react';
import AuthForm from '../components/AuthForm';
import { useAuth } from '../hooks/useAuth';

const Register = () => {
  const { register } = useAuth();

  return (
    <div className="flex justify-center items-center h-screen">
      <AuthForm onSubmit={register} buttonText="Register" />
    </div>
  );
};

export default Register;
