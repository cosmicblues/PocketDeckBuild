from typing import Union
from pydantic import BaseModel

from api.model.models import Pokemon_table
from api.model.models import Trainer_table

class Pokemon(BaseModel):
    id: int
    name: str
    types: str
    hp: int
    attack: int
    weakness: str
    evolution_id: Union[int, None] = None

class PokemonCreate(BaseModel):
    """A class containing pydantic data validation for creating a Pokemon model row."""
    id: int
    name: str
    types: str
    hp: int
    attack: int
    weakness: str
    evolution_id: Union[int, None] = None
    
class PokemonUpdate(BaseModel):
    """A class containing pydantic data validation for updating a Pokemon model row."""
    id: int
    name: str
    types: str
    hp: int
    attack: int
    weakness: str
    evolution_id: Union[int, None] = None

class PokemonInDB(Pokemon):
    """A class containing pydantic data validation for in database Pizza model."""

    id: int

class Trainer(BaseModel):

    id: int
    name: str
    effect: str

class TrainerCreate(BaseModel):

    id: int
    name: str
    effect: str

class TrainerUpdate(BaseModel):

    id: int
    name: str
    effect: str

class TrainerInDB(Pokemon):
    """A class containing pydantic data validation for in database Pizza model."""

    id: int