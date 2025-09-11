import React, { useState } from 'react';

const AddPokemonForm = ({ addPokemon }) => {
  const [pokemonName, setPokemonName] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    if (pokemonName) {
      addPokemon(pokemonName);
      setPokemonName('');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={pokemonName}
        onChange={(e) => setPokemonName(e.target.value)}
        placeholder="Enter pokemon name"
      />
      <button type="submit">Add Pokemon</button>
    </form>
  );
};

export default AddPokemonForm;