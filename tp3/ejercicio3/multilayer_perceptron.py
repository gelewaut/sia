import numpy as np
import sys
import random

class MultilayerPerceptron():

    def __init__(self, layers, weights, targets, error_function, error_derivative):
        self.layers = layers
        self.weights = weights
        self.targets = targets
        self.error_function = error_function
        self.error_derivative = error_derivative

    def get_weights(self):
        return self.weights

    def set_weights(self, weights):
        self.weights = weights

    def initialize_weights(self):
        weights = self.get_weights()
        for weight_col in weights:
            for weight in weight_col:
                weight = random.uniform(0, 1)

    def excitation_function(biases, last_layer_weights, last_layer_activations, last_layer_dim):
        result = []
        for i in range(len(biases)):
            result.append(0)
            for j in range(last_layer_dim):
                result += last_layer_weights[j]*last_layer_activations[j]
            result[i] += biases[i]
        return result

    def mean_squared_error(n, real_values, expected_values):
        result = 0
        for i in range(len(real_values)):
            result += (real_values[i] - expected_values[i])**2
        result *= (1/n)

    def calculate_output_gradients(output_layer):
        gradients = [] 
        activations = output_layer.calculate_derivative()
        for i in range(len(output_layer)):
            gradients.append(self.targets[i] - output_layer.excitations[i])*activations[i]
        return gradients   

    def calculate_layer_gradients(actual_layer, next_layer_gradients, next_weights):
        activations = actual_layer.calculate_derivative()
        gradients = []
        for j in range(len(activations)):
            aux = 0
            for i in range(len(next_weights)):
                aux += next_weights[i][j]*next_layer_gradients[i]
            
            aux *= activations[j]
            
            gradients.append(aux)
        
        return gradients
    
    def calculate_gradients(layers, weights):
        gradients_by_layer = np.empty(len(layers) - 1)
        last_layer = layers[len(layers) - 1]

        i = len(layers) - 2
        gradients_by_layer[i] = MultilayerPerceptron.calculate_output_gradients()
        i -= 1
        while i > 0:
            gradients_by_layer[i] = MultilayerPerceptron.calculate_layer_gradients(layers[i], gradients_by_layer[i+1], weights.weights[i+1])
            i -= 1
        return gradients_by_layer

    # def update_weights(self):
    #     new_weight = 0
    #     for m in range(self.layers):
    #         for j in range(self.layers[m + 1]):
    #             for k in range(self.layers[m]):
                    # self.weights[m][j][k] = 
        

    # def train(layers, activation_function, activation_derivative, expected_values, error_function):


        

            

