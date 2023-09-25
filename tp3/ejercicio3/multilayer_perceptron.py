import numpy as np
import sys
import random


class MultilayerPerceptron():

    def __init__(self, layers, weights, targets, error_function, error_derivative, epochs, error_wanted):
        self.layers = layers
        self.weights = weights
        self.targets = targets
        self.error_function = error_function
        self.error_derivative = error_derivative
        self.epochs = epochs
        self.error_wanted = error_wanted

    def get_weights(self):
        return self.weights

    def set_weights(self, weights):
        self.weights = weights

    def initialize_weights(self):  # TODO arreglar
        weights = self.get_weights()
        for weight_col in weights:
            for weight in weight_col:
                weight = random.uniform(0, 1)

    # def excitation_function(self, biases, last_layer_weights, last_layer_activations, last_layer_dim):
    #     result = []
    #     for i in range(len(biases)):
    #         result.append(0)
    #         for j in range(last_layer_dim):
    #             result += last_layer_weights[j] * last_layer_activations[j]
    #         result[i] += biases[i]
    #     return result

    def forward_propagation(self):
        last_excitations = self.layers[0].get_excitation()
        for m in range(1, len(self.layers)):  # TODO inicializar el excitation de la layer 0 con la data de entrada al principio para no tocarlo aca
            self.layers[m].calculate_excitations(self.weights[m - 1], last_excitations)
            last_excitations = self.layers[m - 1].get_excitation()

    def calculate_output_gradients(self, output_layer):
        gradients = []
        activations = output_layer.calculate_derivative()
        for i in range(len(output_layer)):
            gradients.append((self.targets[i] - output_layer.excitations[i]) * activations[i])
        return gradients

    def calculate_layer_gradients(self, actual_layer, next_layer_gradients, next_weights):
        activations = actual_layer.calculate_derivative()
        gradients = []
        for j in range(len(activations)):
            aux = 0
            for i in range(len(next_weights)):
                aux += next_weights[i][j] * next_layer_gradients[i]
            aux *= activations[j]
            gradients.append(aux)

        return gradients

    def calculate_gradients(self, layers, weights):
        gradients_by_layer = np.empty(len(layers) - 1)
        last_layer = layers[len(layers) - 1]

        m = len(layers) - 2
        gradients_by_layer[m] = self.calculate_output_gradients(last_layer)
        m -= 1
        while m > 0:
            gradients_by_layer[m] = self.calculate_layer_gradients(layers[m], gradients_by_layer[m + 1], weights[m])
            m -= 1
        return gradients_by_layer

    def back_propagation(self, apprentice_rate):
        gradients = self.calculate_gradients(self.layers, self.weights)

        for m in range(len(self.layers) - 1):
            for j in range(len(self.layers[m + 1])):
                for k in range(len(self.layers[m])):
                    self.weights[m][j][k] += apprentice_rate * gradients[m][j] * self.layers[m].get_excitation[k]

    def mean_squared_error(self, n, real_values, expected_values):
        result = 0
        for i in range(len(real_values)):
            result += (real_values[i] - expected_values[i]) ** 2
        result *= (1 / n)

    def get_error(real_outputs, expected_outputs):
        error = 0
        for i in range(len(real_outputs)):
            error += (real_outputs[i] - expected_outputs[i])**2
        error /= 2
        return error

    # def train(self):
    #     error = -1
    #     epochs = self.epochs
    #     while epochs != 0 and error > self.error_wanted:


