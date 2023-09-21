import sys
import numpy as np
import pandas as pd
from perceptron import LinearPerceptron
import matplotlib.pyplot as plt

if __name__ == "__main__":
    with open(f"{sys.argv[1]}", "r") as file:
        reader = pd.read_csv(file).values
        data = np.array([np.append(1, reader[0])])
        for i in range(1, len(reader)):
            data = np.append(data , np.array([np.append(1, reader[i])]), axis=0)

        neuron01 = LinearPerceptron(0.1, 10000, 0.01)
        neuron001 = LinearPerceptron(0.01, 10000, 0.01)
        neuron0001 = LinearPerceptron(0.001, 10000, 0.01)
        neuron00001 = LinearPerceptron(0.0001, 10000, 0.01)
        neuron000001 = LinearPerceptron(0.00001, 10000, 0.01)
        errors01 = neuron01.train(data)
        errors001 = neuron001.train(data)
        errors0001 = neuron0001.train(data)
        errors00001 = neuron00001.train(data)
        errors000001 = neuron000001.train(data)
        
        x_axis_generations = list(range(0, 10000))

        plt.plot(x_axis_generations, errors001, linestyle='-', label='0.01')
        plt.plot(x_axis_generations, errors0001, linestyle='-', label='0.001')
        plt.plot(x_axis_generations, errors00001, linestyle='-', label='0.0001')
        plt.plot(x_axis_generations, errors000001, linestyle='-', label='0.00001')


        plt.xlabel('Round')
        plt.ylabel('Error')

        plt.title('Linear Perceptron - Errors For Different Aprentice Rates')

        plt.legend()

        plt.grid(True)
        plt.show()
        
        