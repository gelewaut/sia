import numpy as np
import random
from src.geneticAlgorithm import normalize

min_value = 0.0
max_value = 150.0
min_height = 1.3
max_height = 2.0
min_prob = 0.0
max_prob = 1.0

gens = 5
strength = 0
agility = 1
expertise = 2
resistance = 3
hp = 4

def set_new_gen_normalize(attributes, gen, new_gen):
    # print('gen:', gen)
    # print('new_gen: ', new_gen)
    if gen == strength:
        new_strength, new_agility, new_expertise, new_resistance, new_hp = normalize(
            new_gen, 
            attributes.get_agility(), 
            attributes.get_expertise(), 
            attributes.get_resistance(), 
            attributes.get_hp())
    elif gen == agility:
        new_strength, new_agility, new_expertise, new_resistance, new_hp = normalize(
            attributes.get_strength(), 
            new_gen, 
            attributes.get_expertise(), 
            attributes.get_resistance(), 
            attributes.get_hp())
    elif gen == expertise:
        new_strength, new_agility, new_expertise, new_resistance, new_hp = normalize(
            attributes.get_strength(), 
            attributes.get_agility(),  
            new_gen,
            attributes.get_resistance(), 
            attributes.get_hp())
    elif gen == resistance:
        new_strength, new_agility, new_expertise, new_resistance, new_hp = normalize(
            attributes.get_strength(), 
            attributes.get_agility(),  
            attributes.get_expertise(), 
            new_gen,
            attributes.get_hp())
    elif gen == hp:
        new_strength, new_agility, new_expertise, new_resistance, new_hp = normalize(
            attributes.get_strength(), 
            attributes.get_agility(),  
            attributes.get_expertise(), 
            attributes.get_resistance(), 
            new_gen)
    else:
        new_height = random.uniform(min_height, max_height)
        attributes.set_height(new_height)
        new_strength, new_agility, new_expertise, new_resistance, new_hp = attributes.get_strength(), attributes.get_agility(), attributes.get_expertise(), attributes.get_resistance(), attributes.get_hp()
    
    # print(new_strength, new_agility, new_expertise, new_resistance, new_hp)

    attributes.set_strength(new_strength)
    attributes.set_agility(new_agility)
    attributes.set_expertise(new_expertise)
    attributes.set_resistance(new_resistance)
    attributes.set_hp(new_hp)


def gen_mutation(attributes, probability):
    mutation_prob = random.uniform(min_prob, max_prob)
    # print('Mutation probability = ', mutation_prob)
    if mutation_prob <= probability:
        chosen_gen = random.randint(0, gens)
        new_gen = random.uniform(min_value, max_value)
        set_new_gen_normalize(attributes, chosen_gen, new_gen)

def multigen_mutation(attributes, probability):
    mutation_prob = random.uniform(min_prob, max_prob)
    # print(mutation_prob)
    if mutation_prob <= probability:
        new_height = random.uniform(min_height, max_height)
        new_strength, new_agility, new_expertise, new_resistance, new_hp = normalize(
            random.uniform(min_value, max_value), 
            random.uniform(min_value, max_value), 
            random.uniform(min_value, max_value), 
            random.uniform(min_value, max_value), 
            random.uniform(min_value, max_value))
    
        # print(new_strength, new_agility, new_expertise, new_resistance, new_hp)
        # print(new_strength + new_agility + new_expertise + new_resistance + new_hp)


        attributes.set_strength(new_strength)
        attributes.set_agility(new_agility)
        attributes.set_expertise(new_expertise)
        attributes.set_resistance(new_resistance)
        attributes.set_hp(new_hp)
        attributes.set_height(new_height)