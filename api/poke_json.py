import json

with open("pokemons.json", "r") as f:
    pokemons_list = json.load(f)
    print('ça marche')

list_pokemons = {k+1:v for k, v in enumerate(pokemons_list)}