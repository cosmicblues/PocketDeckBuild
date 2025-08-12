from dataclasses import dataclass, asdict
from typing import Union
from dataclasses import dataclass, asdict
from fastapi import APIRouter, HTTPException, Path, Depends
from sqlalchemy.orm import Session
from schema.schemas import Pokemon
from api.poke_json import list_pokemons
from api.util.utils import get_db
from api.pokemons_routes.getAllPokemons import router
from api.schema.schemas import PokemonInDB, PokemonCreate
from api.model.crud.crud import Crud

#===========================POST============================
@router.post("/pokemons", response_model=PokemonInDB)
def create_pokemon(pokemon: PokemonCreate, dbb: Session = Depends(get_db)):
    return Crud.create_pokemon(dbb, pokemon)