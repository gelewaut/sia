import numpy as np


class Layer2:
    def __init__(self, nodes_dim, activation_function, activation_derivative):
        self.nodes_dim = nodes_dim
        self.activation_function = activation_function
        self.activation_derivative = activation_derivative
        self.activations = []
        self.excitations = []

    def calculate_activations(self, last_layer):
        if last_layer:
            self.activations = self.activation_function(self.excitations)
        else:
            self.activations = np.concatenate(([1], self.activation_function(self.excitations)))

    def calculate_derivative(self):
        return self.activation_derivative(self.excitations)

    def calculate_excitations(self, weights, last_activations):
        self.excitations = np.dot(weights, last_activations)
