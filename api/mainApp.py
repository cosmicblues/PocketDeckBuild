from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from api.database.database import SessionLocal, engine
from fastapi import FastAPI
import api.model.models as models
import math
import uvicorn
from api.poke_json import list_pokemons
from api.pokemons_routes.getAllPokemons import api as getPokemons




# Structure de données #
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#===========================TEST============================
@app.get("/")
def hello_world():
    return {"Hello": "World"}

app.include_router(getPokemons)

#==========================Startup=========================
@app.on_event("startup")
def startup_populate_db():
    db = SessionLocal()
    num_pokemons = db.query(models.Pokemon_table)
    if num_pokemons:
        Pokemon_table = list_pokemons
        for pokemon in Pokemon_table:
            print(pokemon)
            db.add(models.Pokemon_table(**list_pokemons))
        db.commit()
        print(num_pokemons)
        db.close()
    else:
        print(f"{num_pokemons} pokemon est déjà dans la DB")
        db.close()

"""
#===========================DELETE============================
@app.delete("/pokemon/{id}")
def delete_pokemon(id: int = Path(ge=1)) -> Pokemon:
    if id in list_pokemons :
        pokemon = Pokemon(**list_pokemons[id])
        del list_pokemons[id]
        return pokemon
    
    raise HTTPException(status_code=404, detail=f"Le pokemon {id} n'existe pas.")

#===========================GET============================
@app.get("/types")
def get_all_types()->list[str]:

    types = []
    for pokemon in pokemons_list :
        for type in pokemon["types"] :
            if type not in types :
                types.append(type)
    types.sort()
    return types


@app.get("/pokemons/search/")
def search_pokemons(
    types: Union[str, None] = None,
    evo : Union[str, None] = None,
    totalgt : Union[int, None] = None,
    totallt : Union[int, None] = None,
    sortby : Union[str, None] = None,
    order : Union[str, None] = None,
)->Union[list[Pokemon], None] :
    
    filtered_list = []
    res = []

    #On filtre les types
    if types is not None :
        for pokemon in pokemons_list :
            if set(types.split(",")).issubset(pokemon["types"]) :
                filtered_list.append(pokemon)

    #On filtre les evolutions
    if evo is not None :
        tmp = filtered_list if filtered_list else pokemons_list
        new = []

        for pokemon in tmp :
            if evo == "true" and "evolution_id" in pokemon:
                new.append(pokemon)
            if evo == "false" and "evolution_id" not in pokemon:
                new.append(pokemon)

        filtered_list = new

    #On filtre sur greater than total
    if totalgt is not None :
        tmp = filtered_list if filtered_list else pokemons_list
        new = []

        for pokemon in tmp :
            if pokemon["total"] > totalgt:
                new.append(pokemon)

        filtered_list = new

    #On filtre sur less than total
    if totallt is not None :
        tmp = filtered_list if filtered_list else pokemons_list
        new = []

        for pokemon in tmp :
            if pokemon["total"] < totallt:
        if order == "desc" : sorting_order = True

        filtered_list = sorted(filtered_list, key=lambda d: d[sortby], reverse=sorting_order)

        
    #Réponse           
    if filtered_list :
        for pokemon in filtered_list :
            res.append(Pokemon(**pokemon))
        return res
    
    raise HTTPException(status_code=404, detail="Aucun Pokemon ne répond aux critères de recherche")

#=====Tous les Pokémons avec la pagination=====
@app.get("/pokemons2/")
def get_all_pokemons(page: int=1, items: int=10) -> list[Pokemon]:

    items = min(items, 20)
    max_page = math.ceil(len(list_pokemons) / items)
    current_page = min(page, max_page)
    start = (current_page-1)*items
    stop = start + items if start + items <= len(list_pokemons) else len(list_pokemons)
    sublist = (list(list_pokemons))[start:stop]

    res = []

    for id in sublist :
        res.append(Pokemon(**list_pokemons[id]))
    
    return res            new.append(pokemon)

        filtered_list = new

    #On gére le tri
    if sortby is not None and sortby in ["id","name","total"] :
        filtered_list = filtered_list if filtered_list else pokemons_list
        sorting_order = False
        if order == "asc" : sorting_order = False """
    
