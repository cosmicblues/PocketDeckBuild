#from dataclasses import dataclass, asdict
#from typing import Union
from dataclasses import dataclass, asdict
from fastapi import APIRouter, HTTPException, Path, Depends
#from sqlalchemy.orm import Session
from schema.schemas import Pokemon
from api.poke_json import list_pokemons
from getAllPokemons import api

#===========================PUT============================
@api.put("/pokemon/{id}")
def update_pokemon(pokemon: Pokemon, id: int = Path(ge=1)) -> Pokemon:
    if id not in list_pokemons :
        raise HTTPException(status_code=404, detail=f"Le pokemon {id} n'existe pas.")
    
    list_pokemons[id] = asdict(pokemon)
    return pokemon