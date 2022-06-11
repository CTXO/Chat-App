import React, {useState, useNavigate} from 'react'
import { Container } from "@mui/system";
import { Drawer, Stack } from "@mui/material"

import { Card } from './components/card/card';
import { CardList } from './components/card_list/card_list';

import  './dashboard.scss'

export default function Dashboard () {
    const cards = [1,2,3,4,5].map((i) => <Card key={i}></Card>)
    return (
        <Container maxWidth={false}>
            <Drawer variant="permanent" className='drawer'>
                <CardList>
                    {cards}
                </CardList>
            </Drawer>
        </Container>
    )
}