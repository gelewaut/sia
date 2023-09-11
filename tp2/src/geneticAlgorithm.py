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
                      selection_1, selection_2, crossover, metadata):
    parents_1 = selection_1(gen, np.round(K*A), metadata)
    parents_2 = selection_2(gen, np.round(K*(1-A)), metadata)
    parents = parents_1 + parents_2

    children = crossover(parents)
    
    for child in children:
        mutation(child.get_attributes(), mutation_probablity)
    
    new_gen_1 = replace_traditional(parents, children, np.round(N*B))
    new_gen_2 = replace_young(parents, children, np.round(N*(1-B)))

    return new_gen_1 + new_gen_2

def max_generations (cut_condition, gen, N, K, A, B,
                      mutation, mutation_probablity, 
                      selection_1, selection_2, crossover, metadata):
    count = 0
    while(count < cut_condition):
        metadata["gen_num"] = count
        gen = geneticAlgorithm(gen, N, K, A, B,
                               mutation, mutation_probablity, 
                               selection_1, selection_2, crossover, metadata)
        count += 1
    
    return gen

def max_time (cut_condition, gen, N, K, A, B,
                      mutation, mutation_probablity, 
                      selection_1, selection_2, crossover, metadata):
    timer = time.time()
    gen_num = 0
    while(time.time()-timer < cut_condition):
        metadata["gen_num"] = gen_num
        gen = geneticAlgorithm(gen, N, K, A, B,
                               mutation, mutation_probablity, 
                               selection_1, selection_2, crossover, metadata)
        gen_num += 1
    
    return gen

def content (cut_condition, gen, N, K, A, B,
                      mutation, mutation_probablity, 
                      selection_1, selection_2, crossover, metadata):
    gen.sort()
    best_fitness = gen[N-1].get_fitness()
    count = 0
    gen_num = 0
    while(count < cut_condition):
        metadata["gen_num"] = gen_num
        gen = geneticAlgorithm(gen, N, K, A, B,
                               mutation, mutation_probablity, 
                               selection_1, selection_2, crossover, metadata)
        gen.sort()
        aux = gen[N-1].get_fitness()
        if np.round(best_fitness) == np.round(aux):
            count += 1
        else:
            count = 0
        best_fitness = aux
        gen_num += 1
    
    return gen

#change
def structure (percentage, generations, genes, gen, N, K, A, B,
                      mutation, mutation_probablity, 
                      selection_1, selection_2, crossover, metadata):
    percentage = np.round(N*percentage)
    count = 0
    gen_num = 0
    while count < generations:
        values = []
        for ind in gen:
            att = ind.get_attributes().get_all()
            aux = 0
            mult = 100
            for i in range(1,6):
                aux += np.round(att[i]) * mult * genes[i]
                mult = mult * 1000
            val = np.round(att[0] * 10) * genes[0] + aux
            values.append(val)
        values.sort()

        aux = 0
        aux_value = values[0]
        for i in range(1,N):
            if aux >= percentage:
                count +=1
                break
            if values[i] == aux_value:
                aux += 1
            else:
                aux = 0
                aux_value = values[i]
        
        if aux < percentage:
            count = 0

        metadata["gen_num"] = gen_num
        gen = geneticAlgorithm(gen, N, K, A, B,
                        mutation, mutation_probablity, 
                        selection_1, selection_2, crossover, metadata)
        gen_num += 1

    return gen   


def optimum (cut_condition, gen, N, K, A, B,
                      mutation, mutation_probablity, 
                      selection_1, selection_2, crossover, metadata):

    gen_num = 0
    while(1):
        metadata["gen_num"] = gen_num
        gen = geneticAlgorithm(gen, N, K, A, B,
                               mutation, mutation_probablity, 
                               selection_1, selection_2, crossover, metadata)
        gen_num += 1
        gen.sort()
        best_fitness = gen[N-1].get_fitness()
        if best_fitness >= cut_condition:
            return gen