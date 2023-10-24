import configparser

import matplotlib.pyplot as plt
import numpy as np
import pandas
from scipy import stats
from kohonen import Kohonen

if __name__ == "__main__":
    file = "data/europe.csv"
    reader = pandas.read_csv(file).values
    variables = pandas.read_csv(file).keys().values
    countries = reader[:, 0]
    values = reader[:, 1:].astype(float)
    values = stats.zscore(values, axis=0)

    config = configparser.ConfigParser()
    config.read('../config.ini')

    k = config.getint('Kohonen', 'k')
    radius = k if config.getint('Kohonen', 'radius') == 0 else config.getint('Kohonen', 'radius')
    eta = config.getfloat('Kohonen', 'eta')
    epochs = config.getint('Kohonen', 'epochs')

    grid = Kohonen(k, eta, radius)
    grid.train(values, epochs)
    result, group_by_countries = grid.test(values, countries)
    print(group_by_countries)
    rows, cols = result.shape


    # # Unified Distance Matrix
    # average_distances = grid.unified_distance_matrix()
    # plt.imshow(average_distances, cmap='gray', interpolation='nearest')
    # plt.colorbar()
    # plt.show()

    # Coordenadas de los cuadrados
    # x = np.linspace(0, 1, cols+1)[:-1]  # Distribuye las columnas uniformemente
    # y = np.linspace(0, 1, rows+1)[:-1]
    # rows, cols = result.shape
    # data = np.random.rand(10, 10)

    plt.figure(figsize=(k, k))

    # rows, cols = data.shape

    x = np.arange(0, cols)
    y = np.arange(0, rows)

    X, Y = np.meshgrid(x, y)

    colors = result.flatten()

    # Agregar líneas de cuadrícula con desfase

    plt.pcolormesh(X, Y, result, cmap='coolwarm', shading='auto')

    cbar = plt.colorbar()
    cbar.set_label('Countries')

    plt.gca().set_aspect('equal')

    for i in range(rows):
        for j in range(cols):
            plt.text(j, i, group_by_countries[i][j], color='white', ha='center', va='center', fontweight='bold', fontsize='10')

    plt.xticks(np.arange(0, cols), np.arange(0, cols))
    plt.yticks(np.arange(0, rows), np.arange(0, rows))

    plt.show()

    plt.pcolormesh(X, Y, result, cmap='coolwarm', shading='auto')

    cbar = plt.colorbar()
    cbar.set_label('Number of Countries')

    plt.gca().set_aspect('equal')

    for i in range(rows):
        for j in range(cols):
            plt.text(j, i, int(result[i][j]), color='white', ha='center', va='center', fontweight='bold', fontsize='10')

    plt.xticks(np.arange(0, cols), np.arange(0, cols))
    plt.yticks(np.arange(0, rows), np.arange(0, rows))

    plt.show()

    for v in range(len(variables)-1):
        result, group_by_countries = grid.test_by_variable(values, countries, v)
        plt.pcolormesh(X, Y, result, cmap='coolwarm', shading='auto')

        cbar = plt.colorbar()
        cbar.set_label('Number of Countries')

        plt.gca().set_aspect('equal')

        for i in range(rows):
            for j in range(cols):
                plt.text(j, i, int(result[i][j]), color='white', ha='center', va='center', fontweight='bold', fontsize='10')

        plt.xticks(np.arange(0, cols), np.arange(0, cols))
        plt.yticks(np.arange(0, rows), np.arange(0, rows))
        plt.title(variables[v+1])

        plt.show()
