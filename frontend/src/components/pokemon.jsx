import React, { useEffect, useState } from 'react';
// import AddPokemonForm from './addPokemonForm';
import api from '../api';

const PokemonList = () => {
  const [pokemon, setPokemon] = useState([]);

  useEffect(() => {
    api.get('/pokemons').then(response => {console.log(response.data)})
  .catch(error => {console.log(error)})
  }, [])
//   console.log(api.get('/pokemons'))

}


//   fetchPokemons();
// }, []);

//   const addPokemon = async (pokemonName, pokemonType, pokemonHp, pokemonAttack, pokemonWeakness, pokemonEvo) => {
//     try {
//       await api.post('/pokemons', { name: pokemonName, type: pokemonType, hp: pokemonHp, attack: pokemonAttack, weakness: pokemonWeakness, evolution_id: pokemonEvo, });
//       fetchPokemons();  // Refresh the list after adding a pokemon
//     } catch (error) {
//       console.error("Error adding pokemon", error);
//     }
//     console.log(pokemons);
//   };

//   return (
//     <div>
//       <h2>Pokemon List</h2>
//       <table></table>
//       <ul>
//         {pokemons?.map((pokemon, index) => (
//           <li key={index}>{pokemon.name}</li>,
//           <li key={index}>{pokemon.type}</li>,
//           <li key={index}>{pokemon.hp}</li>,
//           <li key={index}>{pokemon.attack}</li>,
//           <li key={index}>{pokemon.weakness}</li>,
//           <li key={index}>{pokemon.evolution_id}</li>
//         ))}
//       </ul>
//       <AddPokemonForm addPokemon={addPokemon} />
//     </div>

export default PokemonList;