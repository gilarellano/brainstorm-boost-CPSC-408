import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate, Link } from 'react-router-dom';

function Home({ onLogin }) {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [name, setName] = useState('');
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
       
        <body>
            <div class="text-center">
                <main class="container">
                    <h1 class="display-1">Welcome to BrainstormBoost!</h1>
                    <p class="display-6 lead"> BrainstormBoost is a program that uses OpenAI to generate project ideas for a group of people. All you need to do is enter the members in your group, what their skills and interests are, and describe what kind of project you want. Then it will generate a list of ideas for your group to vote on.</p>
                    <h2 class="display-5"><Link to="/generator">Get Started</Link></h2>
                </main>
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
            </div>
        </body>
        
    );
}
export default Home;