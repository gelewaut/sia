import numpy
import math


def __population_fitness__ (generation):
    population_fitnesses = []
    total_fitness = 0

    for i in range(len(generation)):
        population_fitnesses.append(generation[i].get_fitness())
        total_fitness += population_fitnesses[i]
    
    return population_fitnesses, total_fitness


def __elite_selection__(generation, new_generation, max_population):
    gen = generation + new_generation

    if (len(gen) <= max_population):
        return gen

    population_fitnesses, total_fitness = __population_fitness__(gen)

    array = [(gen[i], population_fitnesses[i]) for i in range(len(gen))]
    array.sort(key=lambda x:x[1])

    next_gen = []
    aux = 0
    for i in range(len(array)):
        for _ in math.ceil((max_population - i)/len(array)):
            next_gen[aux] = array[i][0]
            aux += 1

    return next_gen



