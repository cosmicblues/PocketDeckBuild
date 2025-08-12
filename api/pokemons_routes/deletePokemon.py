#from dataclasses import dataclass, asdict
#from typing import Union
from dataclasses import dataclass, asdict
from fastapi import APIRouter, HTTPException, Path, Depends
from sqlalchemy.orm import Session
from schema.schemas import Pokemon
from api.poke_json import list_pokemons
#import models.Pokemon_table
from api.pokemons_routes.getAllPokemons import router
from api.model.crud.crud import Crud
from api.schema.schemas import PokemonInDB
from api.util.utils import get_db, get_pokemon_by_id_if_exists

#===========================DELETE============================
@router.delete("/pokemons/{pid}", response_model=PokemonInDB)
def delete_pokemon(pid: int, dbb: Session = Depends(get_db)):
    get_pokemon_by_id_if_exists(pid, dbb)
    return Crud.delete_pokemon(dbb, pid)