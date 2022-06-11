import React from 'react'
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';
import ListItemAvatar from '@mui/material/ListItemAvatar';
import Avatar from '@mui/material/Avatar';

import './card_list.scss'
export function CardList (props) {
    return (
        <List className='contact-list'>
            {props.children}
        </List>
    )
}