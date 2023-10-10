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
        
        training = np.append(data[0:7], data[14:21], axis=0)
        testing = np.append(data[7:14], data[21:], axis=0)
        neuron = NonLinearPerceptron(0.1, 10000, 0.01,1.6e-01)

        neuron01_1 = NonLinearPerceptron(0.1, 10000, 0.01,1.6e-01)
        errors01_1, testing_1 = neuron01_1.test_while_training(training, testing, maximum, minimum)


        x_axis_generations = list(range(0, len(errors01_1)))
        x_axis_generations_testing = list(range(0, len(testing_1)))

        plt.plot(x_axis_generations, errors01_1, linestyle='-', label='Error - Training')
        plt.plot(x_axis_generations_testing, testing_1, linestyle='-', label='Error - Testing')

        plt.xlabel('Round')
        plt.ylabel('Error')

        plt.title('Non Linear Perceptron - Training 50 % : Testing 50%')

        plt.legend()

        plt.grid(True)
        plt.show()

        training = data[0:7]
        testing = data[7:]

        neuron01_1 = NonLinearPerceptron(0.1, 10000, 0.01,1.6e-01)
        errors01_1, testing_1 = neuron01_1.test_while_training(training, testing, maximum, minimum)


        x_axis_generations = list(range(0, len(errors01_1)))
        x_axis_generations_testing = list(range(0, len(testing_1)))

        plt.plot(x_axis_generations, errors01_1, linestyle='-', label='Error - Training')
        plt.plot(x_axis_generations_testing, testing_1, linestyle='-', label='Error - Testing')

        plt.xlabel('Round')
        plt.ylabel('Error')

        plt.title('Non Linear Perceptron - Training 25 % : Testing 75%')

        plt.legend()

        plt.grid(True)
        plt.show()

        training = data[0:21]
        testing = data[21:]

        neuron01_1 = NonLinearPerceptron(0.1, 10000, 0.01,1.6e-01)
        errors01_1, testing_1 = neuron01_1.test_while_training(training, testing, maximum, minimum)


        x_axis_generations = list(range(0, len(errors01_1)))
        x_axis_generations_testing = list(range(0, len(testing_1)))

        plt.plot(x_axis_generations, errors01_1, linestyle='-', label='Error - Training')
        plt.plot(x_axis_generations_testing, testing_1, linestyle='-', label='Error - Testing')

        plt.xlabel('Round')
        plt.ylabel('Error')

        plt.title('Non Linear Perceptron - Training 75 % : Testing 25%')

        plt.legend()

        plt.grid(True)
        plt.show()
