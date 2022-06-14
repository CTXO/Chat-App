import React from 'react'
import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';
import ListItemAvatar from '@mui/material/ListItemAvatar';
import ListItemButton from '@mui/material/ListItemButton';
import Avatar from '@mui/material/Avatar';
export const cardHeight = '5rem'
export function Card (props) {
    return (
        <ListItem divider={true} className="list-item" sx={{ height: cardHeight, padding: 0 }}>
            <ListItemButton onClick={props.onClick} sx={{ height: "100%" }}>
                 <ListItemAvatar>
                    <Avatar src={`pictures/user_mock.jpeg`}/>
                </ListItemAvatar>
                <ListItemText primary={props.title} secondary={props.subtitle}/>
            </ListItemButton>
        </ListItem>
    )
}