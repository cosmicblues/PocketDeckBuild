import React, { useEffect, useState } from 'react';
import AddPokemonForm from './addPokemonForm';
import api from '../api';

const PokemonList = () => {
  const [pokemons, setPokemons] = useState([]);

  const fetchPokemons = async () => {
    try {
      const response = await api.get('/pokemons');
      setPokemons(response.data.pokemons);
    } catch (error) {
      console.error("Error fetching pokemons", error);
    }
  };

  const addPokemon = async (pokemonName) => {
    try {
      await api.post('/pokemons', { name: pokemonName });
      fetchPokemons();  // Refresh the list after adding a fruit
    } catch (error) {
      console.error("Error adding pokemon", error);
    }
  };

  useEffect(() => {
    fetchPokemons();
  }, []);

  return (
    <div>
      <h2>Pokemon List</h2>
      <ul>
        {pokemons.map((pokemon, index) => (
          <li key={index}>{pokemon.name}</li>
        ))}
      </ul>
      <AddPokemonForm addPokemon={addPokemon} />
    </div>
  );
};

export default PokemonList;