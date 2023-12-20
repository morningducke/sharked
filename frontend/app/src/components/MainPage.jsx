import React, { useState } from 'react';
import '../css/MainPage.css'

export default function MainPage() {
    return (
      <div className="main-container">
        <div className="search-bar">
          <input
            type="search"
            className="search-input"
            placeholder="Enter suspect's username"
            autoComplete="off"
          ></input>
          <button className="report-btn">Generate Report</button>
          
        </div>
        <div className="report-list">
          <div className="report-item">Report 1</div>
          <div className="report-item">Report 2</div>
          <div className="report-item">Report 3</div>
        </div>
      </div>
    )
}