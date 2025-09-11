from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from PocketDeckBuild.database.database import engine, session_local
from PocketDeckBuild.loader import pokemons_list, trainers_list
from PocketDeckBuild.model import models
from PocketDeckBuild.pokemons_routes.addPokemon import router as addPokemon

# from api.pokemons_routes.deleteAllPokemons import router as deleteAllPokemons
from PocketDeckBuild.pokemons_routes.deletePokemon import router as deletePokemon
from PocketDeckBuild.pokemons_routes.getAllPokemons import router as getPokemons
from PocketDeckBuild.pokemons_routes.updatePokemon import router as updatePokemon
from PocketDeckBuild.trainers_routes.addTrainer import router as addTrainer
from PocketDeckBuild.trainers_routes.deleteTrainer import router as deleteTrainer
from PocketDeckBuild.trainers_routes.getAllTrainers import router as getTrainers
from PocketDeckBuild.trainers_routes.updateTrainer import router as updateTrainer

# Structure de données #
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:5173",
    # Add more origins here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ===========================TEST============================
@app.get("/")
def hello_world():
    return {"Hello": "World"}


app.include_router(getPokemons)
app.include_router(addPokemon)
app.include_router(deletePokemon)
app.include_router(updatePokemon)
app.include_router(getTrainers)
app.include_router(addTrainer)
app.include_router(deleteTrainer)
app.include_router(updateTrainer)


# ==========================Startup=========================
@app.on_event("startup")
def startup_populate_db():
    db = session_local()
    num_pokemons = db.query(models.PokemonTable)
    if num_pokemons.count() == 0:
        Pokemon_table = pokemons_list
        for pokemon in Pokemon_table:
            # print([pokemon])
            # print(Pokemon_table[0]['name'])
            db.add(models.PokemonTable(**pokemon))
            # print(pokemon)
        db.commit()
        # print(num_pokemons)
        db.close()
    else:
        print(f"{num_pokemons.count()} pokemon est déjà dans la DB")
        db.close()
    num_trainers = db.query(models.TrainerTable)
    if num_trainers.count() == 0:
        Trainer_table = trainers_list
        for trainer in Trainer_table:
            # print([trainer])
            # print(Trainer_table[0]['name'])
            db.add(models.TrainerTable(**trainer))
            # print(trainer)
        db.commit()
        # print(num_trainers)
        db.close()
    else:
        print(f"{num_trainers.count()} trainer est déjà dans la DB")
        db.close()
