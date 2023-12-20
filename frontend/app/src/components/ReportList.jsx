
import React, { useState, useEffect } from 'react';
import { getUsersReports } from '../client';
import ReportItem from './ReportItem';
import '../css/Report.css'

export default function ReportList() {
    const [userReports, setUserReports] = useState([]);
    useEffect(() => {
        const fetchReports = async () => {
          setUserReports(await getUsersReports());
        }
        if (localStorage.getItem("user"))
          fetchReports(); 
      }, []);

      return (
        <div className="report-list">
            {userReports.map(report => <ReportItem report={report}></ReportItem>)}
        </div>
      )

}