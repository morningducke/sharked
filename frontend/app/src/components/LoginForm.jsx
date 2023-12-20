import React, { useState } from 'react';
import '../css/LoginForm.css'
import { login } from '../client'


export default function LoginForm() {

  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  async function handleLogin(e) {
    e.preventDefault();
    const isLoginOk = await login(username, password);
    alert(`${isLoginOk}, ${JSON.stringify(localStorage['token'])}`);
  }

  return (
    <div className="login-form">
      <h1>Login</h1>

      <form className="form-inline" onSubmit={handleLogin}>
        <div className="form-field">
          <label className="form-field-label">Email</label>
          <input
            type="text"
            className="form-control"
            placeholder="Enter your email"
            onChange={e => {
              setUsername(e.target.value);
            }}
          />
        </div>

        <div className="form-field">
          <label className="form-field-label">Password</label>
          <input
            type="password"
            className="form-control"
            placeholder="Enter your password"
            onChange={e => {
              setPassword(e.target.value);
            }}
          />
        </div>

        <button type="submit" className="btn">Login</button>
      </form>
    </div>
  );
}
