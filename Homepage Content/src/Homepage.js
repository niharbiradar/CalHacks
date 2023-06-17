// components/Homepage.js
import React from 'react';
import { Container, Row, Col, Jumbotron, Button } from 'react-bootstrap';

const Home = () => (
  <Container>
    <Jumbotron>
      <h1>Shielding You from Digital Deception</h1>
      <p>
        Authenticity Insurance is your reliable safeguard against deepfakes, misinformation, 
        and disinformation.
      </p>
      <p>
        <Button variant="primary" href="/signup">Sign Up Now</Button>
      </p>
    </Jumbotron>
    <Row>
      <Col>
        <h2>Our Solution</h2>
        <p>Explanation of your application...</p>
      </Col>
      <Col>
        <h2>The Threat of DeepFakes</h2>
        <p>What would happen if you were attacked with DeepFakes...</p>
      </Col>
    </Row>
    <Row>
      <Col>
        <h2>The Real Cost</h2>
        <p>
          A study by the University of Baltimore in 2019 revealed that disinformation and 
          misinformation have caused over $78 billion in damage to businesses. With the 
          advancement of AI, this number is expected to multiply by ten over the next five years.
        </p>
      </Col>
    </Row>
  </Container>
);

export default Home;
