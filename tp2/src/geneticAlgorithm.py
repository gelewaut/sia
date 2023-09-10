import numpy as np
import time

POINTS = 150

def normalize(strength, agility, expertise, resistance, hp):
    points =  strength + agility + expertise + resistance + hp
    points -= POINTS
    cant = 0
    for i in strength, agility, expertise, resistance, hp:
        if i!=0:
            cant += 1 
    while not np.isclose(points,0.0) and cant > 0:
        delta = points/cant
        if strength != 0:
            if strength - delta < 0:
                points -= strength
                strength = 0
                cant -= 1
            else:
                strength -= delta
                points -= delta

        if agility != 0: 
            if agility - delta < 0:
                points -= agility
                agility = 0
                cant -= 1
            else:
                agility -= delta
                points -= delta

        if expertise != 0:
            if expertise - delta < 0:
                points -= expertise
                expertise = 0
                cant -= 1
            else:
                expertise -= delta
                points -= delta

        if resistance != 0:
            if resistance - delta < 0:
                points -= resistance
                resistance = 0
                cant -= 1
            else:
                resistance -= delta
                points -= delta
    
        if hp != 0:
            if hp - delta < 0:
                points -= hp
                hp = 0
                cant -= 1
            else:
                hp -= delta
                points -= delta
        
    return [strength, agility, expertise, resistance, hp]


# poblacion 0
# N
# probablidad de mutar
# K 
# A
# B
# metodo seleccion 1
# metodo seleccion 2
# cruce
# rempazo

def replace_traditional(parents, children, N):
    parents.sort()
    children.sort()
    new_gen = []
    p_len = len(parents)-1
    c_len = len(children)-1
    p = 0
    c = 0
    while(p+c < N and c_len-c >= 0 and p_len-p >= 0):
        if(children[c_len-c] >= parents[p_len-p]):
            c += 1
            new_gen.append(children.pop())
        else:
            p += 1
            new_gen.append(parents.pop())

    if c_len-c >= 0:
        while(p+c < N):
            c += 1
            new_gen.append(children.pop())
    
    if p_len-p >= 0:
        while(p+c < N):
            p += 1
            new_gen.append(parents.pop())

    return new_gen 

def replace_young(parents, children, N):
    parents.sort()
    children.sort()
    new_gen = []
    p_len = len(parents)-1
    c_len = len(children)-1
    p = 0
    c = 0
    while(p+c < N):
        if(c_len-c > 0):
            c += 1
            new_gen.append(children.pop())
        else:
            p += 1
            new_gen.append(parents.pop())
    
    return new_gen

def geneticAlgorithm (gen, N, K, A, B,
                      mutation, mutation_probablity, 
                      selection_1, selection_2, crossover):
    
    parents_1 = selection_1(gen, np.round(K*A))
    parents_2 = selection_2(gen, np.round(K*(1-A)))
    parents = parents_1 + parents_2

    children = crossover(parents)
    
    for child in children:
        mutation(child.get_attributes(), mutation_probablity)
    
    new_gen_1 = replace_traditional(parents, children, np.round(N*B))
    new_gen_2 = replace_young(parents, children, np.round(N*(1-B)))

    return new_gen_1 + new_gen_2

def max_generations (cut_condition, gen, N, K, A, B,
                      mutation, mutation_probablity, 
                      selection_1, selection_2, crossover):
    count = 0
    while(count < cut_condition):
        gen = geneticAlgorithm(gen, N, K, A, B,
                               mutation, mutation_probablity, 
                               selection_1, selection_2, crossover)
        count += 1
    
    return gen

def max_time (cut_condition, gen, N, K, A, B,
                      mutation, mutation_probablity, 
                      selection_1, selection_2, crossover):
    count = time.time()
    while(time.time()-count < cut_condition):
        gen = geneticAlgorithm(gen, N, K, A, B,
                               mutation, mutation_probablity, 
                               selection_1, selection_2, crossover)
    
    return gen

def content (cut_condition, gen, N, K, A, B,
                      mutation, mutation_probablity, 
                      selection_1, selection_2, crossover):
    gen.sort()
    best_fitness = gen[N-1].get_fitness()
    count = 0

    while(count < cut_condition):
        gen = geneticAlgorithm(gen, N, K, A, B,
                               mutation, mutation_probablity, 
                               selection_1, selection_2, crossover)
        gen.sort()
        aux = gen[N-1].get_fitness()
        if np.round(best_fitness) == np.round(aux):
            count += 1
        best_fitness = aux
    
    return gen

#change
def structure (percentage, generations, genes, gen, N, K, A, B,
                      mutation, mutation_probablity, 
                      selection_1, selection_2, crossover):
    pass
    gen = geneticAlgorithm(gen, N, K, A, B,
                        mutation, mutation_probablity, 
                        selection_1, selection_2, crossover)


def optimum (cut_condition, gen, N, K, A, B,
                      mutation, mutation_probablity, 
                      selection_1, selection_2, crossover):

    while(1):
        gen = geneticAlgorithm(gen, N, K, A, B,
                               mutation, mutation_probablity, 
                               selection_1, selection_2, crossover)
        gen.sort()
        best_fitness = gen[N-1].get_fitness()
        if best_fitness >= cut_condition:
            return gen