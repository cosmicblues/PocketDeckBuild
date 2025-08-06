from dataclasses import dataclass, asdict
from typing import Union
from fastapi import FastAPI, HTTPException, Path, Depends, APIRouter
from sqlalchemy.orm import Session
from database import SessionLocal, engine
#from mainApp import list_pokemons
from schema.schemas import Pokemon
import models
import json

with open("pokemons.json", "r") as f:
    pokemons_list = json.load(f)
    print('ça marche')

list_pokemons = {k+1:v for k, v in enumerate(pokemons_list)}

router = APIRouter()

#===========================GET============================
@router.get("/pokemons")
def get_all_pokemons1() -> list[Pokemon]:
    res = []
    for id in list_pokemons :
        res.append(Pokemon(**list_pokemons[id]))
    return res

""" @router.get("/total_pokemons")
def get_total_pokemons(db: Session = Depends(get_db)) -> dict:
    pokemons_test = db.query(models.Pokemon_table).all()
    print(pokemons_test)
    return {"total":len(list_pokemons)} """

""" @app.get("/pokemon/{id}")
def get_pokemon_by_id(id: int = Path(ge=1)) -> Pokemon :

    if id not in list_pokemons :
        raise HTTPException(status_code=404, detail="Ce pokemon n'existe pas")
    
    return Pokemon(**list_pokemons[id]) """