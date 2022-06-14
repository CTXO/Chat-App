import React from "react";

import { Box } from "@mui/system";
import { AppBar, Toolbar } from "@mui/material"

import { drawerWidth } from "../../dashboard";
import { cardHeight } from "../card/card";
import { Card } from "../card/card";
export function ChatContainer(props) {
    const renderBarIfClicked = function() {
        if (props.userClicked){
            return (
                <AppBar onClick={console.log(props.clickedUser)}
                sx={{ backgroundColor: 'white', color:'black', height: cardHeight, "& .MuiToolbar-root": {
                    ml: drawerWidth,
                    padding: 0
                    }  }}>
                    <Toolbar sx={{ height: '100%' }}>
                        <Card title={props.userClicked} subtitle="Online" />
                    </Toolbar>
                </AppBar>
            )
        }
    }
    return (
        <Box sx={{
            minWidth: `calc(100% - ${drawerWidth})`, ml: `${drawerWidth}`,
            display: 'flex'
        }}>
            {renderBarIfClicked()}
        </Box>
    )
}