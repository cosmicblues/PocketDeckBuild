# from dataclasses import dataclass, asdict
# from typing import Union
from fastapi import Depends

# from sqlalchemy.orm import Session
from sqlalchemy.orm import Session

from PocketDeckBuild.database.database import get_db
from PocketDeckBuild.model.crud.pokemons_crud import SqlPokemonCRUD as Crud
from PocketDeckBuild.pokemons_routes.getAllPokemons import router
from PocketDeckBuild.schema.schemas_pokemons import PokemonInDB, PokemonUpdate


# ===========================PUT============================
@router.put("/pokemons/{pid}", response_model=PokemonInDB)
def update_pokemon(
    pid: int,
    pokemon: PokemonUpdate,
    dbb: Session = Depends(get_db),
):
    prev_pokemon = Crud.get_pokemon_by_id_if_exists(pid, dbb)

    pokemon_update = PokemonUpdate(
        pokemon_id=pid,
        name=pokemon.name if pokemon.name else prev_pokemon.name,
        types=pokemon.types if pokemon.types else prev_pokemon.types,
        hp=pokemon.hp if pokemon.hp else prev_pokemon.hp,
        attack=pokemon.attack if pokemon.attack else prev_pokemon.attack,
        weakness=pokemon.weakness if pokemon.weakness else prev_pokemon.weakness,
        evolution_id=pokemon.evolution_id
        if pokemon.evolution_id
        else prev_pokemon.evolution_id,
    )
    return Crud.update_pokemon(dbb, pokemon_update)
