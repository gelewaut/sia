import matplotlib.pyplot as plt
import numpy as np
import csv

character_file = 'aux.csv'

generation_avgs = []
generation_min = []
generation_max = []
combination_names = []


if __name__ == "__main__": 
    with open(character_file, mode='r') as file:
        character_reader = csv.reader(file)
        for row in character_reader:
            combination_names.append(row[0])
            media = 0
            min_aux = int(row[1])
            max_aux = int(row[1])
            for j in range(1, len(row)):
                media += int(row[j])
                if int(row[j]) < min_aux:
                    min_aux = int(row[j])
                if int(row[j]) > max_aux:
                    max_aux = int(row[j])
            media = media/(len(row) - 1)
            generation_avgs.append(media)    
            generation_min.append(min_aux)    
            generation_max.append(max_aux)    

    x_axis_names = combination_names

    print(generation_min)
    print(generation_max)
    plt.bar(x_axis_names, generation_avgs)
    # plt.bar(x_axis_names, generation_avgs, yerr = [generation_min, generation_max])
    plt.xlabel('Combinations')
    plt.ylabel('Generation average')
    plt.title("Ranking - Average generation to reach optimum")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

    