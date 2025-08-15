import json

with open("trainers.json", "r") as f:
    trainer_list = json.load(f)
    #print(pokemons_list)

list_trainers = {k+1:v for k, v in enumerate(trainer_list)}