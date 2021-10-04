import React, { useState } from "react";
import "./styles.css";


export default function CreateAccount() {

    const [user, setUser] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");


    handleSubmit(e) {
        e.preventDefault();
        console.log("Submitted")
    }



    return (
        <div className="container">
            <form onSubmit={handleSubmit}>
                <label htmlFor="user">
                    Username *
                </label>
                <input type="text" id="user" value={user} />
        
                <label htmlFor="email">
                    E-mail *
                </label>
                <input type="email" id="email" value={email} />
        
                <label htmlFor="password">
                    Password *
                </label>
                <input type="password" id="password" value={password} />
            </form>
        </div>
    )
}


