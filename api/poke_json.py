import json

with open("pokemons.json", "r") as f:
    pokemons_list = json.load(f)
    #print(pokemons_list)

list_pokemons = {k+1:v for k, v in enumerate(pokemons_list)}