from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from PocketDeckBuild.database.database import get_db
from PocketDeckBuild.loader import list_pokemons
from PocketDeckBuild.model.crud.pokemons_crud import SqlPokemonCRUD as Crud
from PocketDeckBuild.schema.schemas_pokemons import Pokemon, PokemonInDB

router = APIRouter()
# ===========================GET============================

# @router.get("/total_pokemons")
# def get_total_pokemons(db: Session = Depends(get_db)) -> dict:
#    pokemons_test = db.query(models.Pokemon_table).all()
#    print(pokemons_test)
#    return {"total":len(list_pokemons)}


@router.get("/pokemon/{pid}", response_model=PokemonInDB)
def read_pokemons_id(pid: int, dbb: Session = Depends(get_db)) -> Pokemon:
    if pid not in list_pokemons:
        raise HTTPException(status_code=404, detail="Ce pokemon n'existe pas")

    return Crud.get_pokemon_by_id_if_exists(pid, dbb)
    # return Pokemon(**list_pokemons[id])


@router.get("/pokemons", response_model=List[PokemonInDB])
def read_pokemons(dbb: Session = Depends(get_db)):
    # print(Crud.get_pokemons(dbb=dbb))
    return Crud.get_pokemons(dbb=dbb)
