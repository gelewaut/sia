import json
import sys
from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect
# import matplotlib.pyplot as plt
# import numpy as np


if __name__ == "__main__":
    factory = PokemonFactory("pokemon.json")
    with open(f"{sys.argv[1]}", "r") as f:
        config = json.load(f)
        pokeball = config["pokeball"]
        pokemon = factory.create(config["pokemon"], config["level"], getattr(StatusEffect,config["status"]), config["hp"])
        print("No noise: ", attempt_catch(pokemon, pokeball))
        for _ in range(10):
            print("Noisy: ", attempt_catch(pokemon, pokeball, 0.15))
