// components/NavBar.js
import React from 'react';
import { Navbar, Nav, Button } from 'react-bootstrap';

const NavbarComponent = () => (
  <Navbar bg="dark" variant="dark">
    <Navbar.Brand href="/">Authenticity Insurance</Navbar.Brand>
    <Nav className="mr-auto">
      <Nav.Link href="/">Home</Nav.Link>
      {/* Add more Nav.Links for other routes */}
    </Nav>
    <Button variant="outline-info">Sign Up / Log In</Button>
  </Navbar>
);

export default NavbarComponent;
