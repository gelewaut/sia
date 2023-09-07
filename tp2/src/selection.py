import numpy
import math
import random


def population_fitness(generation):
    population_fitnesses = []
    total_fitness = 0

    for i in range(len(generation)):
        population_fitnesses.append(generation[i].get_fitness())
        total_fitness += population_fitnesses[i]
    
    return population_fitnesses, total_fitness

def accumulated_population_fitness(generation):
    population_fitness, total_fitness = population_fitness(generation)
    accumulated_fitnesses = []
    relative_fitness = []
    sum_accumulated_fitnesses = 0

    for i in range(len(population_fitness)):        
        relative_fitness[i] += (population_fitness[i]/total_fitness)
        sum_accumulated_fitnesses += relative_fitness[i]
        accumulated_fitnesses[i] += sum_accumulated_fitnesses
    
    return accumulated_fitnesses,relative_fitness, sum_accumulated_fitnesses

def elite_selection(population, max_population):
    

    if (len(population) <= max_population):
        return population

    population_fitnesses, total_fitness = population_fitness(population)

    array = [(population[i], population_fitnesses[i]) for i in range(len(population))]
    array.sort(key=lambda x:x[1])

    next_gen = []
    aux = 0
    for i in range(len(array)):
        for _ in math.ceil((max_population - i)/len(array)):
            next_gen[aux] = array[i][0]
            aux += 1

    return next_gen

def roulette_selection(population, max_population):
    next_gen = []
    accumulated_fitnesses,relative_fitness, sum_accumulated_fitnesses = accumulated_population_fitness(population)
    chosen = [False] * len(population)


    while (len(next_gen) < max_population):
        random_number = random.random()

        for i in range(len(population)):
            if(random_number <= accumulated_fitnesses[i] and not chosen[i]):
                next_gen.append(population[i])
                chosen[i] = True
                break
            
    return next_gen

#Chequear si funciona bien este
def universal_selection(population, max_population):
    next_gen = []
    accumulated_fitnesses,relative_fitness, sum_accumulated_fitnesses = accumulated_population_fitness(population)
    chosen = [False] * len(population)


    while (len(next_gen) < max_population):
        r = random.random()
        random_number = (r+len(next_gen))/max_population
        for i in range(len(population)):
            if(random_number <= accumulated_fitnesses[i] and not chosen[i]):
                next_gen.append(population[i])
                chosen[i] = True
                break
            
    return next_gen

# def ranking_selection(population, max_population):







