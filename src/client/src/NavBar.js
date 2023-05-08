import React from 'react';
import { Link } from 'react-router-dom';

function NavBar({ isAuthenticated, onLogout }) {
  const handleLogout = () => {
    onLogout();
  };

  return (
    <nav className="navbar navbar-expand-lg bg-body-tertiary">
      <div className="container-fluid">
        <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
          <div className="navbar-nav">
            {isAuthenticated ? (
              <>
                <a className="nav-link active" aria-current="page">
                  <Link to="/dashboard">Dashboard</Link>
                </a>
                <a className="nav-link">
                  <Link to="/about">About</Link>
                </a>
                <a className="nav-link">
                  <Link to="/generator">Generator</Link>
                </a>
                <a className="nav-link" onClick={handleLogout}>
                  Logout
                </a>
              </>
            ) : (
              <>
                <a className="nav-link active" aria-current="page">
                  <Link to="/">Home</Link>
                </a>
                <a className="nav-link">
                  <Link to="/about">About</Link>
                </a>
              </>
            )}
          </div>
        </div>
      </div>
    </nav>
  );
}

export default NavBar;
