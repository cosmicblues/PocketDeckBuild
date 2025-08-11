from dataclasses import dataclass, asdict
from typing import Union
from dataclasses import dataclass, asdict
from fastapi import APIRouter, HTTPException, Path, Depends
from sqlalchemy.orm import Session
from schema.schemas import Pokemon
from api.poke_json import list_pokemons
from api.model.models import Pokemon_table
from api.schema import schemas

api = APIRouter()

#===========================GET============================
@api.get("/pokemons")
def getPokemons() -> list[Pokemon]:
    res = []
    for id in list_pokemons :
        res.append(Pokemon(**list_pokemons[id]))
    return res

#@router.get("/total_pokemons")
#def get_total_pokemons(db: Session = Depends(get_db)) -> dict:
#    pokemons_test = db.query(models.Pokemon_table).all()
#    print(pokemons_test)
#    return {"total":len(list_pokemons)} 

@api.get("/pokemon/{id}")
def get_pokemon_by_id(id: int = Path(ge=1)) -> Pokemon :

    if id not in list_pokemons :
        raise HTTPException(status_code=404, detail="Ce pokemon n'existe pas")
    
    return Pokemon(**list_pokemons[id])
