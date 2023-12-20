import React from 'react';
import '../css/Report.css'

export default function ReportItem({report}) {    
    return (
        <>
          <div className="report-item">
            <p>{report.suspect_username}</p>
            <p>verdict: {report.verdict ? "cheater" : "innocent"}</p>
            <p>winrate: {Math.round(report.winrate)}%</p>
            <p>total games: {report.total_games}</p>
          </div>
        </>
    )
}

