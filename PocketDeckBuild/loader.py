import json

# def pokemons_json():
with open("data/pokemons.json", "r") as f:
    pokemons_list = json.load(f)
    # print(pokemons_list)

    list_pokemons = {k + 1: v for k, v in enumerate(pokemons_list)}
    # return list_pokemons


# def trainers_json():
with open("data/trainers.json", "r") as f:
    trainers_list = json.load(f)
    # print(pokemons_list)

    list_trainers = {k + 1: v for k, v in enumerate(trainers_list)}
# return list_trainers
