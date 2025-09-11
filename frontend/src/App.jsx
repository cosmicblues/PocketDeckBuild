import React from 'react';
import './App.css';
import PokemonList from './components/pokemon';

const App = () => {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Pokemons Management App</h1>
      </header>
      <main>
        <PokemonList />
      </main>
    </div>
  );
};

export default App;