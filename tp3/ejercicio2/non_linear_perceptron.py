import random
import csv
import sys
import numpy as np
import pandas as pd
from perceptron import NonLinearPerceptron 
import matplotlib.pyplot as plt


if __name__ == "__main__":
    with open(f"{sys.argv[1]}", "r") as file:
        reader = pd.read_csv(file).values
        data = np.array([np.append(1, reader[0])])
        minimum = data[0][len(data[0]) - 1]
        maximum = data[0][len(data[0]) - 1]
        for i in range(1, len(reader)):
            aux = np.append(1, reader[i])
            if aux[len(aux) - 1] > maximum:
                maximum = aux[len(aux) - 1]
            if aux[len(aux) - 1] < minimum:
                minimum = aux[len(aux) - 1]
            data = np.append(data , np.array([aux]), axis=0)

        
        
        neuron01_1 = NonLinearPerceptron(0.1, 10000, 0.01,1.6e-01)
        neuron001_1 = NonLinearPerceptron(0.01, 10000, 0.01,1.6e-01)
        neuron0001_1 = NonLinearPerceptron(0.001, 10000, 0.01,1.6e-01)
        neuron00001_1 = NonLinearPerceptron(0.0001, 10000, 0.01,1.6e-01)
        neuron000001_1 = NonLinearPerceptron(0.00001, 10000, 0.01,1.6e-01)
        errors01_1 = neuron01_1.train(data, maximum, minimum)
        errors001_1 = neuron001_1.train(data, maximum, minimum)
        errors0001_1 = neuron0001_1.train(data, maximum, minimum)
        errors00001_1 = neuron00001_1.train(data, maximum, minimum)
        errors000001_1 = neuron000001_1.train(data, maximum, minimum)

        neuron01_25 = NonLinearPerceptron(0.1, 10000, 0.01,2.5e-01)
        neuron001_25 = NonLinearPerceptron(0.01, 10000, 0.01,2.5e-01)
        neuron0001_25 = NonLinearPerceptron(0.001, 10000, 0.01,2.5e-01)
        neuron00001_25 = NonLinearPerceptron(0.0001, 10000, 0.01,2.5e-01)
        neuron000001_25 = NonLinearPerceptron(0.00001, 10000, 0.01,2.5e-01)
        errors01_25 = neuron01_25.train(data, maximum, minimum)
        errors001_25 = neuron001_25.train(data, maximum, minimum)
        errors0001_25 = neuron0001_25.train(data, maximum, minimum)
        errors00001_25 = neuron00001_25.train(data, maximum, minimum)
        errors000001_25 = neuron000001_25.train(data, maximum, minimum)

        neuron01_5 = NonLinearPerceptron(0.1, 10000, 0.01,5e-01)
        neuron001_5 = NonLinearPerceptron(0.01, 10000, 0.01,5e-01)
        neuron0001_5 = NonLinearPerceptron(0.001, 10000, 0.01,5e-01)
        neuron00001_5 = NonLinearPerceptron(0.0001, 10000, 0.01,5e-01)
        neuron000001_5 = NonLinearPerceptron(0.00001, 10000, 0.01,5e-01)
        errors01_5 = neuron01_5.train(data, maximum, minimum)
        errors001_5 = neuron001_5.train(data, maximum, minimum)
        errors0001_5 = neuron0001_5.train(data, maximum, minimum)
        errors00001_5 = neuron00001_5.train(data, maximum, minimum)
        errors000001_5 = neuron000001_5.train(data, maximum, minimum)
        
        x_axis_generations = list(range(0, 10000))

        plt.plot(x_axis_generations, errors01_1, linestyle='-', label='0.1 B=1.6e-01')
        plt.plot(x_axis_generations, errors001_1, linestyle='-', label='0.01 B=1.6e-01')
        plt.plot(x_axis_generations, errors0001_1, linestyle='-', label='0.001 B=1.6e-01')
        plt.plot(x_axis_generations, errors00001_1, linestyle='-', label='0.0001 B=1.6e-01')
        plt.plot(x_axis_generations, errors000001_1, linestyle='-', label='0.00001 B=1.6e-01')

        plt.xlabel('Round')
        plt.ylabel('Error')

        plt.title('Non Linear Perceptron - Errors For Different Aprentice Rates And Beta = 1.6e-01')

        plt.legend()

        plt.grid(True)
        plt.show()

        plt.plot(x_axis_generations, errors01_25, linestyle='-', label='0.1 B=2.5e-01')
        plt.plot(x_axis_generations, errors001_25, linestyle='-', label='0.01 B=2.5e-01')
        plt.plot(x_axis_generations, errors0001_25, linestyle='-', label='0.001 B=2.5e-01')
        plt.plot(x_axis_generations, errors00001_25, linestyle='-', label='0.0001 B=2.5e-01')
        plt.plot(x_axis_generations, errors000001_25, linestyle='-', label='0.00001 B=2.5e-01')

        plt.xlabel('Round')
        plt.ylabel('Error')

        plt.title('Non Linear Perceptron - Errors For Different Aprentice Rates And Beta = 2.5e-01')

        plt.legend()

        plt.grid(True)
        plt.show()

        plt.plot(x_axis_generations, errors01_25, linestyle='-', label='0.1 B=5e-01')
        plt.plot(x_axis_generations, errors001_25, linestyle='-', label='0.01 B=5e-01')
        plt.plot(x_axis_generations, errors0001_25, linestyle='-', label='0.001 B=5e-01')
        plt.plot(x_axis_generations, errors00001_25, linestyle='-', label='0.0001 B=5e-01')
        plt.plot(x_axis_generations, errors000001_25, linestyle='-', label='0.00001 B=5e-01')


        plt.xlabel('Round')
        plt.ylabel('Error')

        plt.title('Non Linear Perceptron - Errors For Different Aprentice Rates And Beta = 5e-01')

        plt.legend()

        plt.grid(True)
        plt.show()