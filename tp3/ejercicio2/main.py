import sys
import json
import numpy as np
import pandas as pd
from perceptron import NonLinearPerceptron, LinearPerceptron
import matplotlib.pyplot as plt

if __name__ == "__main__": 
    with open(f"{sys.argv[2]}", "r") as f:
        config = json.load(f)
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

        aux = int(np.round(len(data) * config["training_percentage"]))
        testing = data[0:aux]
        training = data[aux:]

        if config["perceptron_type"] == "linear":
            neuron = LinearPerceptron(config["apprentice_rate"], config["epochs"], config["epsilon"])
            error , test = neuron.test_while_training(training, testing, maximum, minimum)
        elif config["perceptron_type"] == "non_linear":
            neuron = NonLinearPerceptron(config["apprentice_rate"], config["epochs"], config["epsilon"], config["beta"])
            error , test = neuron.test_while_training(training, testing, maximum, minimum)
        else:
            print("perceptron_type must be 'linear' or 'non_linear' ")
            pass
        
        x_axis_generations = list(range(0, len(error)))
        x_axis_generations_testing = list(range(0, len(test)))

        plt.plot(x_axis_generations, error, linestyle='-', label='Error - Training')
        plt.plot(x_axis_generations_testing, test, linestyle='-', label='Error - Testing')

        plt.xlabel('Round')
        plt.ylabel('Error')

        plt.title('Your Perceptron Data')

        plt.legend()

        plt.grid(True)
        plt.show()

