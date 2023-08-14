import json
import sys
from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect
import matplotlib.pyplot as plt
import numpy as np


POKEBALLS = ["pokeball", "ultraball", "fastball", "heavyball"]
ITERS = 100
LEVEL = 100
HP = 1.0
STATUS = StatusEffect.NONE

if __name__ == "__main__":
    factory = PokemonFactory("pokemon.json")
    available_pokemon = []
    with open("pokemon.json", "r") as file:
        pokemon_db = json.load(file)
        available_pokemon = [key for key in pokemon_db]

    pokemons = []    
    for name in available_pokemon:
        pokemon = factory.create(name, LEVEL, STATUS, HP)
        rates = []
        base_success = 0.0
        for i,pokeball in enumerate(POKEBALLS):
            success = 0
            for _ in range(ITERS):
                attempt, rate = attempt_catch(pokemon, pokeball, 0.15)
                if attempt:
                    success += 1
            if i == 0 or base_success == 0:
                base_success = success/ITERS
            success = success/ITERS
            if base_success != 0:
                rates.append(success/base_success)
            else:
                rates.append(0)
        pokemons.append(rates)

    catchs = np.array(pokemons)
    print(catchs)

    x = np.arange(len(pokemons))
    ancho_barras = 0.2  # Ancho de las barras

    for i, pokeball in enumerate(POKEBALLS):
        plt.bar(x + i * ancho_barras, catchs[:, i], width=ancho_barras, label=pokeball)

    plt.xlabel('Pokemons')
    plt.ylabel('Efficiency compared to basic pokeball')
    plt.title('Pokeball Eficiency by Pokemon')
    plt.xticks(x + (len(POKEBALLS) - 1) * ancho_barras / 2, available_pokemon)
    plt.legend()
    plt.show()