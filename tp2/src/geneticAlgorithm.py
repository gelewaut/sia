import numpy as np

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
    while(p+c < N):
        if(children[c_len-c] >= parents[p_len-p]):
            c += 1
            new_gen.append(children.pop())
        else:
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

def geneticAlgorithm (gen_0, N, mutation_probablity, 
                      mutation, K, A, B,
                      selection_1, selection_2, crossover):
    
    parents_1 = selection_1(gen_0, np.round(K*A))
    parents_2 = selection_2(gen_0, np.round(K*(1-A)))
    parents = parents_1 + parents_2

    children = crossover(parents)
    
    for child in children:
        mutation(child.get_attributes(), mutation_probablity)
    
    new_gen_1 = replace_traditional(parents, children, np.round(N*B))
    new_gen_2 = replace_young(parents, children, np.round(N*(1-B)))

    return new_gen_1 + new_gen_2