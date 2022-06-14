import React from "react";

import { Box } from "@mui/system";
import { AppBar, Toolbar } from "@mui/material"

import { drawerWidth } from "../../dashboard";
import { cardHeight } from "../card/card";
import { Card } from "../card/card";
export function ChatContainer() {
    return (
        <Box sx={{
            minWidth: `calc(100% - ${drawerWidth})`, ml: `${drawerWidth}`,
            display: 'flex'
        }}>
            <AppBar
            sx={{ backgroundColor: 'white', color:'black', height: cardHeight, "& .MuiToolbar-root": {
                ml: drawerWidth,
                padding: 0
                }  }}>
                <Toolbar sx={{ height: '100%' }}>
                    <Card title="teste" subtitle="Online" />
                </Toolbar>
            </AppBar>

        </Box>
    )
}