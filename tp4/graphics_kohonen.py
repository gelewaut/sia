import matplotlib.pyplot as plt
import numpy as np
import pandas
import sys
import random
from scipy import stats
import kohonen

if __name__ == "__main__":
    with open(f"{sys.argv[1]}", "r") as file:
        reader = pandas.read_csv(file).values
        countries = reader[:,0]
        values = reader[:, 1:].astype(float)
        values = stats.zscore(values, axis=0)

        k = 2
        radius = 1
        eta = 0.1

        grid = kohonen.Kohonen(k, eta, radius)
        grid.train(values, 500)
        result, group_by_countries = grid.test(values, countries)
        print(countries)
        rows, cols = result.shape

        # Coordenadas de los cuadrados
        # x = np.linspace(0, 1, cols+1)[:-1]  # Distribuye las columnas uniformemente
        # y = np.linspace(0, 1, rows+1)[:-1]
        rows, cols = result.shape
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