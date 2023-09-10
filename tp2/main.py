import src.classes as classes
import src.mutation as mutation
import src.crossover as cross
import src.selection as selection
import random
import json
import sys
import src.geneticAlgorithm as gen

min_value = 0.0
max_value = 150.0
min_height = 1.3
max_height = 2.0

characters = {
    "warrior": lambda x: classes.Warrior(x),
    "archer": lambda x: classes.Archer(x),
    "defender": lambda x: classes.Defender(x),
    "spy": lambda x: classes.Spy(x)
}

mutation_functions = {
    "simple": mutation.gen_mutation,
    "multi": mutation.multigen_mutation
}

cross_functions = {
    "one_point": cross.one_point_cross,
    "two_point": cross.two_point_cross,
    "ring": cross.ring_cross,
    "uniform": cross.uniform_cross
}

selection_functions = {
    "no" : selection.no_selection,
    "elite" : selection.elite_selection,
    "roulette": selection.roulette_selection,
    "universal": selection.universal_selection
}

if __name__ == "__main__": 
    with open(f"{sys.argv[1]}", "r") as f:
        config = json.load(f)

        population = []
        N = config["N"]
        K = config["K"]
        A = config["A"]
        B = config["B"]
        mutation_probability = config["mutation_probability"]
        mutation_1 = mutation_functions[config["mutation"]]
        selection_1 = selection_functions[config["selection_1"]]
        selection_2 = selection_functions[config["selection_2"]]
        crossover = cross_functions[config["crossover"]]

        for i in range(N):
            height = random.uniform(min_height, max_height)
            strength, agility, expertise, resistance, hp = gen.normalize(
                random.uniform(min_value, max_value), 
                random.uniform(min_value, max_value), 
                random.uniform(min_value, max_value), 
                random.uniform(min_value, max_value), 
                random.uniform(min_value, max_value))
            att = classes.Attributes(height, strength, agility, expertise, resistance, hp)
            population.append(characters[config["class"]](att))
        
        population.sort()
        for i in population:
            print(i)
        print("---------------")

        if config["cut_method"] == "max_generations":
            cut_condition = config["cut_condition"]
            population = gen.max_generations(cut_condition, population, N, K, A, B,
                                         mutation_1, mutation_probability,
                                         selection_1, selection_2, crossover)
        if config["cut_method"] == "max_time":
            cut_condition = config["cut_condition"]
            population = gen.max_time(cut_condition, population, N, K, A, B,
                                         mutation_1, mutation_probability,
                                         selection_1, selection_2, crossover)
        
        if config["cut_method"] == "content":
            cut_condition = config["cut_condition"]
            population = gen.content(cut_condition, population, N, K, A, B,
                                         mutation_1, mutation_probability,
                                         selection_1, selection_2, crossover)
        
        if config["cut_method"] == "structure":
            percentage = config["cut_condition"]["percentage"]
            generations = config["cut_condition"]["generations"]
            aux = config["cut_condition"]["genes"]
            genes = [aux["height"], aux["strength"], aux["agility"], aux["expertise"], aux["resistance"], aux["hp"]]
            population = gen.structure(percentage, generations, genes, population, N, K, A, B,
                                         mutation_1, mutation_probability,
                                         selection_1, selection_2, crossover)
        
        if config["cut_method"] == "optimum":
            cut_condition = config["cut_condition"]
            population = gen.optimum(cut_condition, population, N, K, A, B,
                                         mutation_1, mutation_probability,
                                         selection_1, selection_2, crossover)
        
        population.sort()
        for i in population:
            print(i)