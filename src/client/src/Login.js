import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

function Login({ onLogin }) {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [name, setName] = useState(''); // Add this line
    const [register, setRegister] = useState(false);
    const navigate = useNavigate();
  
    const handleLogin = async () => {
      try {
        const response = await axios.post('/api/login', { username, password });
        if (response.data.success) {
          // Call the onLogin prop to update the parent state
          onLogin(response.data.user);
          // Navigate to the next page with the user's information
          navigate('/groups');
        } else {
          alert('Incorrect username or password');
        }
      } catch (error) {
        console.error('Error logging in:', error);
      }
    };
    
  
    const handleRegister = async () => {
        try {
          const response = await axios.post('/api/register', { username, password, name }); // Include 'name' here
          if (response.data.success) {
            alert('User registered successfully');
            setRegister(false);
          } else {
            alert('Error registering user');
          }
        } catch (error) {
          console.error('Error registering user:', error);
        }
    };
  
    return (
      <div className="login">
        <h2>{register ? 'Register' : 'Login'}</h2>
        <input
          type="text"
          placeholder="Name" // Add this input field
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        {register ? (
          <>
            <button onClick={handleRegister}>Register</button>
            <button onClick={() => setRegister(false)}>Back to Login</button>
          </>
        ) : (
          <>
            <button onClick={handleLogin}>Login</button>
            <button onClick={() => setRegister(true)}>Create Account</button>
          </>
        )}
      </div>
    );
  }
  
  export default Login;
