import numpy
import pandas
import sys
import random
from scipy import stats

def initialize_weights(dim, data):
    length = len(data)

    neurons = numpy.empty((k, k), dtype=numpy.ndarray)
    for i in range(dim):
        for j in range(dim):
            aux = random.randint(0,length-1)
            neurons[i][j] = numpy.copy(data[aux])

    return neurons
            
def find_winner(grid, input):
    k = len(grid)
    min_i=0
    min_j=0
    min_w = sys.maxsize

    for i in range(k):
        for j in range(k):
            dist = numpy.linalg.norm(input-grid[i][j])
            if dist < min_w:
                min_w = dist
                min_i = i
                min_j = j
    
    return min_i, min_j

def update_weights(grid, input, i, j, radius, eta):
    k = len(grid)
    for ii in range(k):
        for jj in range(k):
            if numpy.sqrt((ii-i)**2 + (jj-j)**2) < radius and not (i==ii and j==jj):
                grid[ii][jj] += eta * (input - grid[ii][jj])

def final_results(grid, inputs, countries):
    k = len(grid)
    result = numpy.empty((k, k), dtype=numpy.ndarray)
    for n in range(len(inputs)):
        i,j = find_winner(grid, inputs[n])
        if result[i][j] is not None:
            result[i][j] = numpy.append(result[i][j], [n])
        else:
            result[i][j] = numpy.array([n])
    
    print(result)



if __name__ == "__main__":
    with open(f"{sys.argv[1]}", "r") as file:
        reader = pandas.read_csv(file).values
        countries = reader[:,0]
        values = reader[:, 1:].astype(float)
        values = stats.zscore(values, axis=0)
        
        k = 4 
        epoch = 0
        radius = 1
        eta = 0.1
        grid = initialize_weights(k, values)
        length = len(values)

        while epoch < 500:
            aux = random.randint(0, length-1)
            data = values[aux]
            i,j = find_winner(grid, data)
            update_weights(grid, data, i, j, radius, eta)
            epoch += 1
        
        final_results(grid, values, countries)
        



