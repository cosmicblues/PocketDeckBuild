from dataclasses import dataclass
from typing import Union
import json

# Structure de données #
with open("pokemons.json", "r") as f:
    pokemons_list = json.load(f)

list_pokemons = {k+1:v for k, v in enumerate(pokemons_list)}

@dataclass
class Pokemon() :
    id: int
    name: str
    types: list[str]
    hp: int
    attack1: int
    attack2: int
    weakness: str
    evolution_id: Union[int, None] = None