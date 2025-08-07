#from dataclasses import dataclass, asdict
#from typing import Union
from fastapi import APIRouter
#from sqlalchemy.orm import Session
from schema.schemas import Pokemon
from api.poke_json import list_pokemons
#import models.Pokemon_table

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

#@router.get("/pokemon/{id}")
#def get_pokemon_by_id(id: int = Path(ge=1)) -> Pokemon :

#    if id not in list_pokemons :
#        raise HTTPException(status_code=404, detail="Ce pokemon n'existe pas")
    
#    return Pokemon(**list_pokemons[id])