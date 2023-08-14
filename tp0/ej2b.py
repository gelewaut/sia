import json
import sys
from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect
import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":
    factory = PokemonFactory("pokemon.json")
    with open(f"{sys.argv[1]}", "r") as f:
        config = json.load(f)
        pokeball = "pokeball"
        pokemon_chances = []
        for i in range(100):
            pokemon = factory.create(config["pokemon"], config["level"], StatusEffect.NONE, i/100)
            aux = 0
            for _ in range(10):
                success,rate = attempt_catch(pokemon, pokeball, 0.15)
                aux += rate
            print(aux/10)
            pokemon_chances.append(aux/10)

    x = np.arange(100)  
    plt.plot(x, pokemon_chances, marker='o', linestyle='None')
    plt.xlabel('hp percentage')
    plt.ylabel('catch percentage')
    plt.title("Catch of pokemon with different hp")
    # plt.legend()

    plt.show()