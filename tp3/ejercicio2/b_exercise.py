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
        
        training = data[0:14]
        testing = data[14:]

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

        training = data[0:5]
        testing = data[5:]

        neuron01_1 = NonLinearPerceptron(0.1, 10000, 0.01,1.6e-01)
        errors01_1, testing_1 = neuron01_1.test_while_training(training, testing, maximum, minimum)


        x_axis_generations = list(range(0, len(errors01_1)))
        x_axis_generations_testing = list(range(0, len(testing_1)))

        plt.plot(x_axis_generations, errors01_1, linestyle='-', label='Error - Training')
        plt.plot(x_axis_generations_testing, testing_1, linestyle='-', label='Error - Testing')

        plt.xlabel('Round')
        plt.ylabel('Error')

        plt.title('Non Linear Perceptron - Training 20 % : Testing 80%')

        plt.legend()

        plt.grid(True)
        plt.show()

        training = data[0:23]
        testing = data[23:]

        neuron01_1 = NonLinearPerceptron(0.1, 10000, 0.01,1.6e-01)
        errors01_1, testing_1 = neuron01_1.test_while_training(training, testing, maximum, minimum)


        x_axis_generations = list(range(0, len(errors01_1)))
        x_axis_generations_testing = list(range(0, len(testing_1)))

        plt.plot(x_axis_generations, errors01_1, linestyle='-', label='Error - Training')
        plt.plot(x_axis_generations_testing, testing_1, linestyle='-', label='Error - Testing')

        plt.xlabel('Round')
        plt.ylabel('Error')

        plt.title('Non Linear Perceptron - Training 80 % : Testing 20%')

        plt.legend()

        plt.grid(True)
        plt.show()
