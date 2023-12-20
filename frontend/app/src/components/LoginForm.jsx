import React, { useState } from 'react';
import '../css/LoginForm.css'



export default function LoginForm({ onLogin }) {

  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');


  return (
    <div className="login-form">
      <h1>login</h1>

      <form className="form-inline" onSubmit={(e) => onLogin(e, username, password)}>
        <div className="form-field">
          <label className="form-field-label">email</label>
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
          <label className="form-field-label">password</label>
          <input
            type="password"
            className="form-control"
            placeholder="Enter your password"
            onChange={e => {
              setPassword(e.target.value);
            }}
          />
        </div>

        <button type="submit" className="btn">login</button>
      </form>
    </div>
  );
}
