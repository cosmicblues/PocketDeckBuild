from .pokemons_crud import SqlPokemonCRUD
from .trainers_crud import SqlTrainerCRUD

class Crud(SqlPokemonCRUD):
    """A class containing all Crud operations for all models in database."""

class Crud2(SqlTrainerCRUD):
    """A class containing all Crud operations for all models in database."""