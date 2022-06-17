import React from "react";
import './message.css'

export function Message(props) {
    return (
        <div className="message">
            <p className="from-me">{props.text}</p>
        </div>
    )
}