"""Define utility functions."""
from sqlalchemy.orm import Session
from api.model.crud.crud import Crud
from api.database.database import SessionLocal


def get_pokemon_by_id_if_exists(pid: int, dbb: Session):
    pokemon = Crud.get_pokemon_by_id(dbb, pid)
    if not pokemon:
        raise Exception(f"No such pokemon with {pid} found.")
    return pokemon

def get_db():
    local_db: Session = SessionLocal()
    try:
        yield local_db
    finally:
        local_db.close()