  // import MyButton from "./components/MyButton"
import React, { useState, useEffect } from 'react';
import LoginForm from './components/LoginForm';
import MainPage from './components/MainPage';
import { login } from './client'

export default function App() {
  const [user, setUser] = useState(null);
  // stay logged in after refreshing
  useEffect(() => {
    const loggedInUser = localStorage.getItem("user");
    if (loggedInUser) {
      const foundUser = JSON.parse(loggedInUser);
      setUser(foundUser);
    }
  }, []);


  async function handleLogin(e, username, password) {
    e.preventDefault();
    const isLoginOk = await login(username, password);
    setUser({username: username});
    localStorage["user"] = JSON.stringify({username}); // TODO: change to getCurrentUser
    // alert(`${isLoginOk}, ${JSON.stringify(localStorage['token'])}`);
  }

  async function handleLogout() {
    setUser(null);
    localStorage.removeItem("user");
  }

  return (
    <>
    {user === null && <LoginForm onLogin={handleLogin}></LoginForm>}
    {user !== null && <MainPage user={user}
                                onLogout={handleLogout}
                                >
                                {user.username}</MainPage>}
    </>
    
  );
}

