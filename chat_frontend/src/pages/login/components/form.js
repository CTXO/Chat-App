import React, { useState }  from 'react'
import { TextField, Button, Stack } from '@mui/material'
import { useNavigate } from 'react-router-dom';
export default function Form() {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('');

  const navigate = useNavigate()

  const handleUsernameChange = event => setUsername(event.target.value)
  const handlePasswordChange = event => setPassword(event.target.value)

  const handleSubmit = event => {
    event.preventDefault();
    console.log(username, password);
    navigate('/dashboard')

  }

  return (
    <form onSubmit={handleSubmit}>
      <Stack spacing={2}>
        <TextField variant="filled" label="username" type="text" value={username} onChange={handleUsernameChange}/>
        <TextField variant="filled" label="password" type="password" value={password} onChange={handlePasswordChange}/>
        <Button variant="contained" type="submit">Log In</Button>
      </Stack>
    </form>
  )


}