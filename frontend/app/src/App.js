// import MyButton from "./components/MyButton"
import './App.css';
import axios from 'axios';
import React, { useEffect, useState } from 'react';
import config from './config'
import LoginForm from './components/LoginForm';
import MainPage from './components/MainPage';

export default function App() {

  return (
    <>
      {/* <h1>Users</h1>
      {users.map(user => (
        <div key={user.username}>
          <p> Username: {user.username}</p>
        </div>
      ))} */}
    {/* <LoginForm></LoginForm> */}
    <MainPage></MainPage>
    </>
    
  );
}

