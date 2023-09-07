import src.classes as classes
import src.mutation as mutation
import src.crossover as cross
import src.selection as selection
import random
import src.geneticAlgorithm as gen

min_value = 0.0
max_value = 150.0
min_height = 1.3
max_height = 2.0

if __name__ == "__main__":
    population = []
    for i in range(10):
        height = random.uniform(min_height, max_height)
        strength, agility, expertise, resistance, hp = gen.normalize(
            random.uniform(min_value, max_value), 
            random.uniform(min_value, max_value), 
            random.uniform(min_value, max_value), 
            random.uniform(min_value, max_value), 
            random.uniform(min_value, max_value))
        att = classes.Attributes(height, strength, agility, expertise, resistance, hp)
        population.append(classes.Warrior(att))
    
    population.sort()
    for i in population:
        print(i)
    print("---------------")
    
    population = gen.geneticAlgorithm(population, 10, 0.5, mutation.multigen_mutation, 8, 1, 0, selection.no_selection, selection.no_selection, cross.one_point_cross)
    
    population.sort()
    for i in population:
        print(i)