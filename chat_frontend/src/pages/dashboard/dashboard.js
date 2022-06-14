import React, {useState, useNavigate} from 'react'
import { Box } from "@mui/system";

import { Card, cardHeight } from './components/card/card';
import { CardList } from './components/card_list/card_list';

import  './dashboard.scss'
import { ChatContainer } from './components/chat_container/chat_container';
import { ContactContainer } from './components/drawer/contact_container';

export const drawerWidth = "25%"
export default function Dashboard () {
        const [clickedUser, setClickedUser] = useState(null)

        const clickUser = function(userName) {
            console.log(userName)
            setClickedUser(userName)
        }

        return (
        <Box sx={{ display: 'flex' }}>
            <ChatContainer userClicked={clickedUser}/>
            <ContactContainer clickUser={clickUser}/>
        </Box>
    )
}