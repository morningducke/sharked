import React from 'react';
import '../css/LogoutButton.css'

export default function LogoutButton({ onLogout }) {
    return (
        <button className="logout-btn" onClick={onLogout}>logout</button>
    )
}