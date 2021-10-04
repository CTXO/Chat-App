
import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';


import Login from './pages/Login';
import CreateAccount from './pages/CreateAccount';
import Main from './pages/Main';

export default function Routes() {
    return(
        <BrowserRouter>
            <Switch>
                <Route path="/" exact component={Login} />
                <Route path="/create" component={CreateAccount} />
                <Route path="/main" component={Main} />
            </Switch>
        </BrowserRouter>
    );
}