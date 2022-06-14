import React from "react"
import { Drawer } from '@mui/material'
import { drawerWidth } from "../../dashboard"
import { CardList } from "../card_list/card_list"
import { Card } from "../card/card"


export function ContactContainer(props) {
    const handleClick = function(name) {
        props.clickUser(name)
    }
    const cards = ["Romero", "Victória", "Carol", "Alegria"].map((name, i) => <Card title={name} onClick={() => handleClick(name)}
                                                                                subtitle="last message" key={i}/>)
    const drawerContent = (
        <CardList>
            {cards}
        </CardList>
    )

    return (
        <Drawer
        sx={{
            width: drawerWidth,
            flexShrink: 0,
            '& .MuiDrawer-paper': {
              width: drawerWidth,
              boxSizing: 'border-box',
            },
          }}
          variant="permanent"
          anchor="left" 
        >
            {drawerContent}
        </Drawer>
    )
}    
