import numpy as np
import random
from src.geneticAlgorithm import normalize

def mutate(attributes):

    min_value = 0.0
    max_value = 150.0
    
    new_strength, new_agility, new_expertise, new_resistance, new_hp = normalize(
        random.uniform(min_value, max_value), 
        random.uniform(min_value, max_value), 
        random.uniform(min_value, max_value), 
        random.uniform(min_value, max_value), 
        random.uniform(min_value, max_value))
    
    print(new_strength, new_agility, new_expertise, new_resistance, new_hp)

    attributes.set_strength(new_strength)
    attributes.set_agility(new_agility)
    attributes.set_expertise(new_expertise)
    attributes.set_resistance(new_resistance)
    attributes.set_hp(new_hp)