import React, { useState } from "react";
import "./styles.css";


export default function CreateAccount() {

    const [user, setUser] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    
    function handleSubmit(event) {
        event.preventDefault();
        console.log("Email: " + email)
        console.log("user: " + user)
        console.log("password: " +password)
    }



    return (
        <div className="container">
            <form onSubmit={handleSubmit}>
                <label htmlFor="user">
                    Username *
                </label>
                <input type="text" id="user" value={user} onChange={event => setUser(event.target.value)}/>
        
                <label htmlFor="email">
                    E-mail *
                </label>
                <input type="email" id="email" value={email} onChange={event => setEmail(event.target.value)}/>
        
                <label htmlFor="password">
                    Password *
                </label>
                <input type="password" id="password" value={password} onChange={event => setPassword(event.target.value)}/>

                <input type="submit" id="submit" />
            </form>
        </div>
    )
}


