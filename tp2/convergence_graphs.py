import matplotlib.pyplot as plt
import numpy as np
import csv

class_type = ''

elite_file = class_type + '_elite_selection.csv'
universal_file = class_type + '_universal_selection.csv'
roulette_file = class_type + '_roulette_selection.csv'
prob_tournament_file = class_type + '_prob_tournament_selection.csv'
det_tournament_file = class_type + '_det_tournament_selection.csv'
ranking_file = class_type + '_ranking_selection.csv'
boltzmann_file = class_type + '_boltzmann_selection.csv'

if __name__ == "__main__": 

    y_axis_elite = []
    y_axis_universal = []
    y_axis_roulette = []
    y_axis_prob_tournament = []
    y_axis_det_tournament = []
    y_axis_ranking = []
    y_axis_boltzmann = []


    with open(elite_file, mode='r') as file:
        elite_reader = csv.reader(file)
        for i in elite_reader:
            for elem in i:
                fitness_media = float(elem.replace(',', '.'))
                y_axis_elite.append(fitness_media)
    
    with open(universal_file, mode='r') as file:
        universal_reader = csv.reader(file)
        for i in universal_reader:
            for elem in i:
                fitness_media = float(elem.replace(',', '.'))
                y_axis_universal.append(fitness_media)

    with open(roulette_file, mode='r') as file:
        roulette_reader = csv.reader(file)
        for i in roulette_reader:
            for elem in i:
                fitness_media = float(elem.replace(',', '.'))
                y_axis_roulette.append(fitness_media)

    with open(prob_tournament_file, mode='r') as file:
        prob_tournament_reader = csv.reader(file)
        for i in prob_tournament_reader:
            for elem in i:
                fitness_media = float(elem.replace(',', '.'))
                y_axis_prob_tournament.append(fitness_media)

    with open(det_tournament_file, mode='r') as file:
        det_tournament_reader = csv.reader(file)
        for i in det_tournament_reader:
            for elem in i:
                fitness_media = float(elem.replace(',', '.'))
                y_axis_det_tournament.append(fitness_media)

    with open(ranking_file, mode='r') as file:
        ranking_reader = csv.reader(file)
        for i in ranking_reader:
            for elem in i:
                fitness_media = float(elem.replace(',', '.'))
                y_axis_ranking.append(fitness_media)
            
    with open(boltzmann_file, mode='r') as file:
        boltzmann_reader = csv.reader(file)
        for i in boltzmann_reader:
            for elem in i:
                fitness_media = float(elem.replace(',', '.'))
                y_axis_boltzmann.append(fitness_media)

    x_axis_generations = list(range(1, 101))

    plt.plot(x_axis_generations, y_axis_elite, linestyle='-', label='Elite')
    plt.plot(x_axis_generations, y_axis_universal, linestyle='-', label='Universal')
    plt.plot(x_axis_generations, y_axis_roulette, linestyle='-', label='Roulette')
    plt.plot(x_axis_generations, y_axis_prob_tournament, linestyle='-', label='Probabilistic tournament')
    plt.plot(x_axis_generations, y_axis_det_tournament, linestyle='-', label='Deterministic tournament')
    plt.plot(x_axis_generations, y_axis_ranking, linestyle='-', label='Ranking')
    plt.plot(x_axis_generations, y_axis_boltzmann, linestyle='-', label='Boltzmann')




    plt.xlabel('Generation number')
    plt.ylabel('Fitness media of each generation')

    plt.title('Genetic algorithm for ' + class_type)

    plt.legend()

    plt.grid(True)
    plt.show()