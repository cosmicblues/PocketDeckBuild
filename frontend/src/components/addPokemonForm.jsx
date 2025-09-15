import React, { useState } from 'react';

// const AddPokemonForm = ({ addPokemon }) => {
//   const [pokemonName, setPokemonName] = useState('');
//   const [pokemonType, setPokemonType] = useState('');
//   const [pokemonHp, setPokemonHp] = useState();
//   const [pokemonAttack, setPokemonAttack] = useState();
//   const [pokemonWeakness, setPokemonWeakness] = useState('');
//   const [pokemonEvo, setPokemonEvo] = useState();

//   const handleSubmit = (event) => {
//     event.preventDefault();
//     if (pokemonName) {
//       addPokemon(pokemonName);
//       setPokemonName('');
//     }
//     if (pokemonType) {
//       addPokemon(pokemonType);
//       setPokemonType('');
//     }
//     if (pokemonHp) {
//       addPokemon(pokemonHp);
//       setPokemonHp();
//     }
//     if (pokemonAttack) {
//       addPokemon(pokemonAttack);
//       setPokemonAttack();
//     }
//     if (pokemonWeakness) {
//       addPokemon(pokemonWeakness);
//       setPokemonWeakness('');
//     }
//     if (pokemonEvo) {
//       addPokemon(pokemonEvo);
//       setPokemonEvo();
//     }
//   };

//   return (
//     <form onSubmit={handleSubmit}>
//       <input
//         type="text"
//         value={pokemonName}
//         onChange={(e) => setPokemonName(e.target.value)}
//         placeholder="Enter pokemon name"
//       />
//       <input
//         type="text"
//         value={pokemonType}
//         onChange={(e) => setPokemonType(e.target.value)}
//         placeholder="Enter pokemon type"
//       />
//       <input
//         type="number"
//         value={pokemonHp}
//         onChange={(e) => setPokemonHp(e.target.value)}
//         placeholder="Enter pokemon hp"
//       />
//       <input
//         type="number"
//         value={pokemonAttack}
//         onChange={(e) => setPokemonAttack(e.target.value)}
//         placeholder="Enter pokemon attack"
//       />
//       <input
//         type="text"
//         value={pokemonWeakness}
//         onChange={(e) => setPokemonWeakness(e.target.value)}
//         placeholder="Enter pokemon weakness"
//       />
//       <input
//         type="number"
//         value={pokemonEvo}
//         onChange={(e) => setPokemonEvo(e.target.value)}
//         placeholder="Enter pokemon evolution_id"
//       />
//       <button type="submit">Add Pokemon</button>
//     </form>
//   );
// };

// export default AddPokemonForm;