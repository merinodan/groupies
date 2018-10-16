import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <img src={logo} className="App-logo" alt="logo" />
        <h1 className="App-title">Groupies</h1>
        <p className="App-intro">
          Enter something to groupie
        </p>
        <button>
          >
        </button>
      </div>
    );
  }
}

export default App;
