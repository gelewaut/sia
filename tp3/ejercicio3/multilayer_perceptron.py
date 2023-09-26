import numpy as np
import sys
import random
import copy


class MultilayerPerceptron():

    def __init__(self, layers, targets, epochs, error_wanted, examples, apprentice_rate):
        self.layers = layers
        self.inputs = None
        self.target = None
        self.weights = None
        self.targets = targets
        # self.error_function = error_function
        # self.error_derivative = error_derivative
        self.epochs = epochs
        self.error_wanted = error_wanted
        self.examples = examples
        self.weights_min = None
        self.apprentice_rate = apprentice_rate

    def get_weights(self):
        return self.weights

    def set_weights(self, weights):
        self.weights = weights

    def get_inputs(self):
        return self.inputs

    def initialize_weights(self): 
        # columns = max(self.layers, key=lambda layer: layer.nodes_dim).nodes_dim
        # new_weights = np.zeros((len(self.layers) - 1, columns , columns), dtype=float)   # CHEQUEAR ACA SI ALGO SE ROMPE
        new_weights = []
        empty_row = []
        for m in range(len(self.layers) - 1):
            new_weights.append(copy.copy(empty_row))  
            for j in range(self.layers[m + 1].nodes_dim):
                new_weights[m].append(copy.copy(empty_row))
                for k in range(self.layers[m].nodes_dim):
                    new_weights[m][j].append(random.uniform(0.1, 0.5))
        self.weights = new_weights
        #weights = self.get_weights()
        #for weight_col in weights:
        #    for weight in weight_col:
        #        weight = random.uniform(0, 1)

    # def excitation_function(self, biases, last_layer_weights, last_layer_activations, last_layer_dim):
    #     result = []
    #     for i in range(len(biases)):
    #         result.append(0)
    #         for j in range(last_layer_dim):
    #             result += last_layer_weights[j] * last_layer_activations[j]
    #         result[i] += biases[i]
    #     return result

    def forward_propagation(self):
        last_activations = self.get_inputs()
        for m in range(1, len(self.layers)):
            print(m)
            self.layers[m].calculate_activations(self.weights[m - 1], last_activations)
            last_activations = self.layers[m - 1].get_activations()

    def calculate_output_gradients(self, output_layer):
        gradients = []
        derivatives = output_layer.calculate_derivative()
        for i in range(output_layer.nodes_dim):
            gradients.append((self.target[i] - output_layer.get_activations()[i]) * derivatives[i])
        return gradients

    def calculate_layer_gradients(self, actual_layer, next_layer_gradients, next_weights, next_dim):
        derivatives = actual_layer.calculate_derivative()
        gradients = []
        for j in range(len(derivatives)):
            aux = 0
            for i in range(next_dim):
                aux += next_weights[i][j] * next_layer_gradients[i]
            aux *= derivatives[j]
            gradients.append(aux)

        return gradients

    def calculate_gradients(self, layers, weights):
        # columns = max(self.layers, key=lambda layer: layer.nodes_dim).nodes_dim
        # gradients_by_layer = np.zeros((len(self.layers) - 1, columns), dtype=float)
        last_layer = layers[len(layers) - 1]
        gradients_by_layer = []
        empty_row = []
        for m in range(len(self.layers) - 1):
            gradients_by_layer.append(copy.copy(empty_row))  
        m = len(layers) - 2
        gradients_by_layer[m] = self.calculate_output_gradients(last_layer)
        m -= 1
        while m >= 0:
            gradients_by_layer[m] = self.calculate_layer_gradients(layers[m + 1], gradients_by_layer[m + 1], weights[m + 1], layers[m + 2].nodes_dim)
            m -= 1
        return gradients_by_layer

    def back_propagation(self):
        self.layers[0].set_activations(self.inputs)
        gradients = self.calculate_gradients(self.layers, self.weights)
        for m in range(len(self.layers) - 1):
            for j in range(self.layers[m + 1].nodes_dim):
                for k in range(self.layers[m].nodes_dim):
                    self.weights[m][j][k] += self.apprentice_rate * gradients[m][j] * self.layers[m].get_activations()[k]
                    # print( gradients[m][j] )

    def mean_squared_error(self, n, real_output, target_output):
        result = 0
        for i in range(len(real_output)):
            result += (real_output[i] - target_output[i]) ** 2
        result *= (1 / n)

    def get_error(self):
        error = 0
        for i in range(len(self.target)):
            error += (self.layers[len(self.layers)-1].get_activations()[i] - self.target[i])**2
        error /= 2
        return error

    def train(self):
        error = -1
        epochs = self.epochs
        min_error = sys.maxsize
        self.initialize_weights()
        # print("pesos antes de train: ", self.weights)
        while epochs != 0 and min_error > self.error_wanted:
            example = random.randint(0, len(self.examples)-1)
            self.inputs = self.examples[example]
            print(self.inputs)
            self.target = self.targets[example]
            self.forward_propagation()
            self.back_propagation()
            error = self.get_error()
            # print("error actual: ", error)
            # print("error minimo: ", min_error)
            if error < min_error:
                min_error = error
                self.weights_min = self.weights
            epochs -= 1
        print(epochs)

    def test(self, inputs):
        self.inputs = inputs
        self.forward_propagation()
        print(self.layers[len(self.layers) - 1].get_activations())
        return self.layers[len(self.layers) - 1]

            





