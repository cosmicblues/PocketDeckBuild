from typing import Union
from pydantic import BaseModel

from api.model.models import Pokemon_table

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

class PokemonUpdate(BaseModel):
    """A class containing pydantic data validation for updating a Pokemon model row."""
