import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import NavBar from './NavBar.js'; 
import Home from './Homepage.js';

const App = () => {
  return (
   <>
    <Router>
      <NavBar/>
      <Switch>
        <Route exact path="/" component={Home} />
        {/* Add more routes for other pages */}
      </Switch>
    </Router>

    <div>
      <h1>Welcome to My React App</h1>
    </div>
    </> 
  );
}

