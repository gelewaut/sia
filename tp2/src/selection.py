import numpy
import math
import random

def no_selection(population, max_population, metadata):
    parents = []
    population.sort()
    for _ in range(max_population):
        parents.append(population.pop())
    return parents

def population_fitness(generation):
    population_fitnesses = []
    total_fitness = 0

    for i in range(len(generation)):
        population_fitnesses.append(generation[i].get_fitness())
        total_fitness += population_fitnesses[i]
    
    return population_fitnesses, total_fitness

def accumulated_population_fitness(generation):
    population_fitnesses, total_fitness = population_fitness(generation)
    accumulated_fitnesses = []
    relative_fitness = []
    sum_accumulated_fitnesses = 0

    for i in range(len(population_fitnesses)):        
        relative_fitness.append(population_fitnesses[i]/total_fitness)
        sum_accumulated_fitnesses += relative_fitness[i]
        accumulated_fitnesses.append(sum_accumulated_fitnesses)
    
    return accumulated_fitnesses,relative_fitness, sum_accumulated_fitnesses

def elite_selection(population, max_population, metadata):
    if (len(population) <= max_population):
        return population

    population.sort()

    next_gen = []
    
    for i in range(len(population)):
        for _ in range(math.ceil((max_population - i)/len(population))):
            next_gen.append(population[len(population) - i - 1])

    return next_gen

def roulette_selection(population, max_population, metadata):
    next_gen = []
    accumulated_fitnesses,relative_fitness, sum_accumulated_fitnesses = accumulated_population_fitness(population)


    while (len(next_gen) < max_population):
        random_number = random.random()

        for i in range(len(population)):
            if(random_number <= accumulated_fitnesses[i]):
                next_gen.append(population[i])
                break
            
    return next_gen

def universal_selection(population, max_population, metadata):
    next_gen = []
    accumulated_fitnesses,relative_fitness, sum_accumulated_fitnesses = accumulated_population_fitness(population)

    j=0
    r = random.random()
    while (len(next_gen) < max_population):
        random_number = (r+j)/max_population
        for i in range(len(population)):
            if(random_number <= accumulated_fitnesses[i]):
                next_gen.append(population[i])
                j+=1
                break

    return next_gen

def ranking_selection(population, max_population, metadata):
    next_gen = []
    population_fitnesses, total_fitness = population_fitness(population)

    population_fitnesses.sort()

    new_fitnesses = []
    for i in range(len(population)):
        new_fitnesses.append((population_fitnesses.index(population[i].get_fitness())-1)/len(population))

    accumulated_fitnesses = []
    relative_fitness = []
    sum_accumulated_fitnesses = 0

    for i in range(len(new_fitnesses)):        
        relative_fitness.append(new_fitnesses[i]/total_fitness)
        sum_accumulated_fitnesses += relative_fitness[i]
        accumulated_fitnesses.append(sum_accumulated_fitnesses)


    while (len(next_gen) < max_population):
        random_number = random.random()
        for i in range(len(population)):
            if(random_number <= accumulated_fitnesses[i]):
                next_gen.append(population[i])
                break
            
    return next_gen

def prob_tournament_selection(population, max_population, metadata):
    threshold = 1 - random.uniform(0,0.5)
    new_gen = []

    while len(population) > 1 and len(new_gen) < max_population:
        chosen = [(i < 2) for i in range(0, len(population))]
        random.shuffle(chosen)
        aux = []
        for i in range(len(population)):
            if chosen[i]:
                aux.append(population[i])
        
        aux.sort()
        r = random.random()
        winner = aux[1 if r < threshold else 0]
        new_gen.append(winner)
        population.remove(winner)
    
    if len(population) == 1:
        new_gen.append(population[0])

    population.clear()    

    return new_gen

def det_tournament_selection(population, max_population, metadata):

    if len(population) <= max_population:
        return population
    
    inds_per_tournament =  math.ceil(len(population) / 2.0)
    new_gen = []

    for i in range(0, max_population):
        chosen = [(i < inds_per_tournament) for i in range(0, len(population))]
        random.shuffle(chosen)
        aux = []

        for i in range(0, len(population)):
            if chosen[i]:
                aux.append(population[i])

        aux.sort()
        winner = aux[len(aux)-1]
        new_gen.append(winner)
        population.remove(winner)

    return new_gen

def boltzmann_selection(population, max_population, metadata):
    tc = metadata["tc"]
    to = metadata["to"]
    k = metadata["k"]
    n = metadata["gen_num"]
    temperature = tc + (to - tc )*math.exp(-k*n)
    exp_values = []
    average = 0

    for individual in population:
        aux = math.exp(individual.get_fitness()/temperature)
        exp_values.append(aux)
        average += aux

    average = average/len(population)
    for i in range(len(exp_values)):
        exp_values[i] = exp_values[i]/average

    next_gen = []
    chosen = [False] * len(population)

    while (len(next_gen) < max_population):
        random_number = random.random()

        for i in range(len(population)):
            if(random_number <= exp_values[i] and not chosen[i]):
                next_gen.append(population[i])
                chosen[i] = True
                break

    return next_gen
            

        











