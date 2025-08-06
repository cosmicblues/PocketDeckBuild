from typing import Union
from pydantic import BaseModel

from models import Pokemon_table

class Pokemon(BaseModel) :
    id: int
    name: str
    types: list[str]
    hp: int
    attack: int
    weakness: str
    evolution_id: Union[int, None] = None