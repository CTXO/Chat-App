import './App.scss';
import React  from 'react'
import { Button } from "@mui/material";
import Login  from "./pages/login/login"
import Dashboard from './pages/dashboard/dashboard'
import { HashRouter as Router, Route, Routes, Navigate } from "react-router-dom"

function App() {
  return (
    <Router>
      <Routes>
        <Route path='/' element={<Navigate replace to='/login'/>}/>
        <Route path='/login' element={<Login/>}/>
        <Route path="/dashboard" element={<Dashboard/>}>
          Dashboard page
        </Route>
      </Routes>
    </Router>
  );
}

export default App;
