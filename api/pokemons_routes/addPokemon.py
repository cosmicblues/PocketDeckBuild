from dataclasses import dataclass, asdict
from typing import Union
from dataclasses import dataclass, asdict
from fastapi import APIRouter, HTTPException, Path, Depends
from sqlalchemy.orm import Session
from schema.schemas import Pokemon
from api.poke_json import list_pokemons
from getAllPokemons import api
from api.util.utils import get_db, get_pizza_by_id_if_exists

#===========================POST============================
@api.post("/pokemon/")
def create_pokemon(pokemon: Pokemon) -> Pokemon:
    if pokemon.id in list_pokemons :
        raise HTTPException(status_code=404, detail=f"Le pokemon {pokemon.id} existe déjà !")
    
    list_pokemons[pokemon.id] = asdict(pokemon)
    return pokemon