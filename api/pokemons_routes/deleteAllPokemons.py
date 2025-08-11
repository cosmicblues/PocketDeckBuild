#from dataclasses import dataclass, asdict
#from typing import Union
from dataclasses import dataclass, asdict
from fastapi import APIRouter, HTTPException, Path, Depends
#from sqlalchemy.orm import Session
from schema.schemas import Pokemon
from api.poke_json import list_pokemons
from getAllPokemons import api