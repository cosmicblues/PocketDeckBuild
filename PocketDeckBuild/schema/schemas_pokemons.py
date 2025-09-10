from typing import Union

from pydantic import BaseModel


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
