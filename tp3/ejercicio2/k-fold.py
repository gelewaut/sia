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

        # training = data[0:4]
        # testing = data[4:]

        # neuron1 = NonLinearPerceptron(0.1, 10000, 0.01,1.6e-01)
        # neuron1.train(training, maximum, minimum)
        # print(neuron1.test(testing, maximum, minimum))
        ks= []
        errors = []

        k=7
        for i in range(0, int(28/k)):
            training = data[i*k:(i+1)*k]
            testing = np.append(data[0:i*k], data[(i+1)*k:], axis=0)
            neuron = NonLinearPerceptron(0.1, 10000, 0.01,1.6e-01)
            neuron.train(training, maximum, minimum)
            errors.append(neuron.test(testing, maximum, minimum))
            ks.append(i)
        
        print(errors)
        plt.plot(ks, errors, linestyle='-', label='Error')

        plt.xlabel('Round')
        plt.ylabel('Error')

        plt.title('Non Linear Perceptron - K-Fold Cross Validation')

        plt.legend()

        plt.grid(True)
        plt.show()