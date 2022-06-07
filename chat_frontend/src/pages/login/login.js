import React, { useState }  from 'react'
import { Container } from '@mui/material'
import Form from './components/form'
import './login.css'
function Login() {
  return(
    <Container maxWidth='xs' 
    sx={{ 
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      marginTop: '20vh'
     }}
    >
      <h1 id="login-header">Sign in to your account</h1>
      <Form/>
    </Container>
  )
}

export default Login
