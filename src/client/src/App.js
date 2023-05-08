import './App.css';
import React, { useState, useEffect } from 'react';
import About from './About';
import Home from './Home';
import Generator from './Generator';
import NavBar from './NavBar';
import Login from './Login';
import Dashboard from './Dashboard';
import { Routes, Route, Link, BrowserRouter } from 'react-router-dom';
import axios from 'axios';

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [user, setUser] = useState(null);

  const onLogin = (user) => {
    setUser(user);
  };

  useEffect(() => {
    const checkAuth = async () => {
      try {
        const response = await axios.get('/api/check-auth', { withCredentials: true });
        if (response.data.success) {
          setIsAuthenticated(true);
        }
      } catch (error) {
        console.error('Error checking authentication:', error);
      }
    };

    checkAuth();
  }, []);

  const handleLogout = () => {
    setIsAuthenticated(false);
  };

  return (
    <div>
      <NavBar isAuthenticated={isAuthenticated} onLogout={handleLogout} />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        {isAuthenticated ? (
          <>
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/generator" element={<Generator />} />
            <Route path="/groups" element={<Generator />} />
          </>
        ) : (
          <Route path="/login" element={<Login onLogin={onLogin} />} />
        )}
      </Routes>
    </div>
  );
}

export default App;
