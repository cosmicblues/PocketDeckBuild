from fastapi import Depends
from sqlalchemy.orm import Session

from PocketDeckBuild.model.crud.pokemons_crud import SqlPokemonCRUD as Crud
from PocketDeckBuild.pokemons_routes.getAllPokemons import router
from PocketDeckBuild.schema.schemas_pokemons import PokemonCreate, PokemonInDB
from PocketDeckBuild.util.utils import get_db


# ===========================POST============================
@router.post("/pokemons", response_model=PokemonInDB)
def create_pokemon(pokemon: PokemonCreate, dbb: Session = Depends(get_db)):
    return Crud.create_pokemon(dbb, pokemon)
