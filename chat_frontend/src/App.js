import './App.css';
import React  from 'react'
import { Button } from "@mui/material";
import Login  from "./pages/login/login"
import { HashRouter as Router, Route, Routes, Navigate } from "react-router-dom"

function App() {
  return (
    <Router>
      <Routes>
        <Route path='/' element={<Navigate replace to='/login'/>}/>
        <Route path='/login' element={<Login id="login-page"/>}/>
        <Route path="/dashboard" element={<h1>Dashboard page</h1>}>
          Dashboard page
        </Route>
      </Routes>
    </Router>
  );
}

export default App;
