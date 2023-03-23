import React, { Component } from 'react'
import { Container ,Row,Col } from 'react-bootstrap'

export default class Home extends Component {
  render() {
    return (
      <div className='text-center'>
        <h1>Home Page</h1>
        <Container fluid>
            <Row>
                <Col className='colname'>
                hi
                </Col>
            </Row>
        </Container>
    </div>
    );
  }
}
