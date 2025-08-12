from sqlalchemy.orm import Session

from api.model.models import Pokemon_table
from api.schema.schemas import PokemonCreate, PokemonUpdate

class PokemonCRUD:
    """Abtract class defining all CRUD operations for Pokemon model."""

    @staticmethod
    def get_pokemons(dbb: Session):
        raise NotImplementedError

    @staticmethod
    def get_pokemon_by_id(dbb: Session, id: int):
        raise NotImplementedError

    @staticmethod
    def create_pokemon(dbb: Session, id: PokemonCreate):
        raise NotImplementedError

    @staticmethod
    def update_pokemon(dbb: Session, pokemon: PokemonUpdate):
        raise NotImplementedError

    @staticmethod
    def delete_pokemon(dbb: Session, id: int):
        raise NotImplementedError
    
class SqlPokemonCRUD(PokemonCRUD):
    """A class containing SQL CRUD operations for Pokemon model."""

    @staticmethod
    def get_pokemons(dbb: Session):
        return dbb.query(Pokemon_table).all()

    @staticmethod
    def get_pokemon_by_id(dbb: Session, id: int):
        return dbb.query(Pokemon_table).filter(Pokemon_table.id == id).first()

    @staticmethod
    def create_pokemon(dbb: Session, pokemon: PokemonCreate):
        db_pokemon = Pokemon_table(**pokemon.dict())
        dbb.add(db_pokemon)
        dbb.commit()
        dbb.refresh(db_pokemon)
        return db_pokemon

    @staticmethod
    def update_pokemon(dbb: Session, pokemon: PokemonUpdate):
        pokemon_in_db = SqlPokemonCRUD.get_pokemon_by_id(dbb, Pokemon_table.id)
        pokemon_in_db.name = pokemon.name
        pokemon_in_db.types = pokemon.types
        pokemon_in_db.hp = pokemon.hp
        pokemon_in_db.attack = pokemon.attack
        pokemon_in_db.weakness = pokemon.weakness
        pokemon_in_db.evolution_id = pokemon.evolution_id

        dbb.commit()
        return pokemon_in_db

    @staticmethod
    def delete_pokemon(dbb: Session, id: int):
        pokemon = SqlPokemonCRUD.get_pokemon_by_id(dbb, id)
        dbb.delete(pokemon)
        dbb.commit()
        return pokemon