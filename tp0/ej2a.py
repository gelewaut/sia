import json
import sys
from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect
import matplotlib.pyplot as plt
import numpy as np


POKEBALL = "ultraball"
ITERS = 100
LEVEL = 100
HP = 1.0
STATUS = ["none","poison","burn","paralysis","sleep","freeze"]

if __name__ == "__main__":
    factory = PokemonFactory("pokemon.json")
    available_pokemon = []
    with open("pokemon.json", "r") as file:
        pokemon_db = json.load(file)
        available_pokemon = [key for key in pokemon_db]

    pokemons = [] 
    for name in available_pokemon:
        none_success = 0   
        rates = []
        for i,status in enumerate(StatusEffect):
            pokemon = factory.create(name, LEVEL, status, HP)
            success = 0
            for _ in range(ITERS):
                attempt, rate = attempt_catch(pokemon, POKEBALL, 0.15)
                if attempt:
                    success += 1 
            if i == 0 :
                none_success = success/ITERS
            success = success/ITERS
            if none_success != 0:
                rates.append(success/none_success)
            else:
                rates.append(0)
        pokemons.append(rates)

    catchs = np.array(pokemons)
    print(catchs)

    x = np.arange(len(pokemons))
    ancho_barras = 0.1  # Ancho de las barras

    for i, status in enumerate(STATUS):
        plt.bar(x + i * ancho_barras, catchs[:, i], width=ancho_barras, label=status)

    plt.xlabel('Pokemons')
    plt.ylabel('Efficiency compared to none status')
    plt.title('Status Eficiency by Pokemon using Ultraball')
    plt.xticks(x + (len(STATUS) - 1) * ancho_barras / 2, available_pokemon)
    plt.legend()
    plt.show()