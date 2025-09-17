import React from 'react';
import { useState } from 'react'
import { useEffect } from 'react';
// import AddPokemonForm from './addPokemonForm';
import api from '../api';

export default function PokemonList() {
  const [pokemon, setPokemon] = React.useState([]);
  useEffect(() => {
    const pokemonList = async () => {  
      try {
        const response = await api.get('/pokemons');
        setPokemon(response.data);
        console.log(JSON.stringify(response.data[0]));
        return (
          <div>
              {response.data.map((pokemon) => pokemon.name).forEach((pokemon) => {
            (<h1>{pokemon}</h1>);
              })}
          </div>
        )
      } catch (error) {
        console.error("Error fetching pokemons", error);
      }
    };

    pokemonList();
    }, []);
  }


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
