import React, { useState, useEffect } from 'react';
import '../css/MainPage.css'
import LogoutButton from './LogoutButton.jsx'
import ReportList from './ReportList.jsx';
import { generateReport } from '../client.js';

export default function MainPage({user, onLogout}) {
    const [suspectName, setSuspectName] = useState('');
    const [website, setWebsite] = useState('lichess');
    const [updateList, setUpdateList] = useState(Date());

    return (
      <div className="fake-body">
        <div className="header-style">
          <h1 className="title-text">sharked</h1>
          <p className="username-display">{user.username}</p>
          <LogoutButton onLogout={onLogout}
          ></LogoutButton>
        </div>
        <div className="main-container">
          <button className="choose-btn" onClick={() => {setWebsite(website === "lichess" ? "chesscom" : "lichess")}}>
            {website === "lichess" ? "switch to chesscom" : "switch to lichess"}
          </button>
          <div className="search-bar">
            <input
              type="search"
              className="search-input"
              placeholder="enter suspect's username"
              autoComplete="off"
              onChange={(e) => setSuspectName(e.target.value)}
              value={suspectName}
            ></input>
            <button className="report-btn" onClick={() => {generateReport(suspectName, website); setSuspectName(''); setUpdateList(Date()) }}>generate report</button>
          </div>
          <ReportList key={updateList}></ReportList>
        </div>
      </div>
    )
}