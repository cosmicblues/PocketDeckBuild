import './App.css';
import PokemonList from './components/pokemon';
import NavbarSection from './components/test';

const App = () => {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Pokemons Management App</h1>
      </header>
      <main>
        <PokemonList />
        <NavbarSection />
      </main>
    </div>
  );
};

export default App;