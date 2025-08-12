from dataclasses import dataclass, asdict
from typing import Union, List
from dataclasses import dataclass, asdict
from fastapi import APIRouter, HTTPException, Path, Depends
from sqlalchemy.orm import Session
from schema.schemas import Pokemon
from api.poke_json import list_pokemons
from api.model.models import Pokemon_table
from api.schema.schemas import PokemonInDB, PokemonCreate, PokemonUpdate
from api.model.crud.crud import Crud
from api.util.utils import get_db, get_pokemon_by_id_if_exists

router = APIRouter()

#===========================GET============================

#@router.get("/total_pokemons")
#def get_total_pokemons(db: Session = Depends(get_db)) -> dict:
#    pokemons_test = db.query(models.Pokemon_table).all()
#    print(pokemons_test)
#    return {"total":len(list_pokemons)} 

@router.get("/pokemon/{pid}", response_model=PokemonInDB)
def read_pokemons_id(pid: int, dbb: Session = Depends(get_db)) -> Pokemon :

    if pid not in list_pokemons :
        raise HTTPException(status_code=404, detail="Ce pokemon n'existe pas")
   
    return get_pokemon_by_id_if_exists(pid, dbb)
    #return Pokemon(**list_pokemons[id])

@router.get("/pokemons", response_model=List[PokemonInDB])
def read_pokemons(dbb: Session = Depends(get_db)):
    #print(Crud.get_pokemons(dbb=dbb))
    return Crud.get_pokemons(dbb=dbb)

@router.post("/pokemons", response_model=PokemonInDB)
def create_pokemon(pokemon: PokemonCreate, dbb: Session = Depends(get_db)):
    return Crud.create_pokemon(dbb, pokemon)

@router.put("/pokemons/{pid}", response_model=PokemonInDB)
def update_pokemon(
    pid: int,
    pokemon: PokemonUpdate,
    dbb: Session = Depends(get_db),
):
    prev_pokemon = get_pokemon_by_id_if_exists(pid, dbb)
    
    pokemon_update = PokemonUpdate(
        pokemon_id=pid,
        name=pokemon.name if pokemon.name else prev_pokemon.name,
        types=pokemon.types if pokemon.types else prev_pokemon.types,
        hp=pokemon.hp if pokemon.hp else prev_pokemon.hp,
        attack=pokemon.attack if pokemon.attack else prev_pokemon.attack,
        weakness=pokemon.weakness if pokemon.weakness else prev_pokemon.weakness,
        evolution_id=pokemon.evolution_id if pokemon.evolution_id else prev_pokemon.evolution_id,
    )
    return Crud.update_pokemon(dbb, pokemon_update)

@router.delete("/pokemons/{pid}", response_model=PokemonInDB)
def delete_pokemon(pid: int, dbb: Session = Depends(get_db)):
    get_pokemon_by_id_if_exists(pid, dbb)
    return Crud.delete_pokemon(dbb, pid)