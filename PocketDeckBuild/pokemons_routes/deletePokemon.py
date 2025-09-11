# from dataclasses import dataclass, asdict
# from typing import Union
from fastapi import Depends
from sqlalchemy.orm import Session

from PocketDeckBuild.database.database import get_db
from PocketDeckBuild.model.crud.pokemons_crud import SqlPokemonCRUD as Crud

# import models.Pokemon_table
from PocketDeckBuild.pokemons_routes.getAllPokemons import router
from PocketDeckBuild.schema.schemas_pokemons import PokemonInDB


# ===========================DELETE============================
@router.delete("/pokemons/{pid}", response_model=PokemonInDB)
def delete_pokemon(pid: int, dbb: Session = Depends(get_db)):
    Crud.get_pokemon_by_id_if_exists(pid, dbb)
    return Crud.delete_pokemon(dbb, pid)
