import numpy as np
import sys
import random

class Layer():
    def __init__(self, nodes_dim, activation_function, activation_derivative, biases):
        self.nodes_dim = nodes_dim
        self.activation_function = activation_function
        self.activation_derivative = activation_derivative
        self.biases = biases
        self.activations = []

    def get_biases(self):
        return self.biases

    def get_activations(self):
        return self.activations

    def set_activations(self, activations):
        self.activations = activations

    def calculate_activations(self, weights, last_excitations):
        results = []
        excitations = self.calculate_excitations(weights, last_excitations)
        for excitation in excitations:
            results.append(self.activation_function(excitation))
        self.activations = results

    def calculate_derivative(self):
        results = []
        for activation in self.activations:
            results.append(self.activation_derivative(activation))
        return results

    def calculate_excitations(self, weights, last_excitations):
        results = []
        for j in range(self.nodes_dim):
            aux = 0
            for k in range(len(last_excitations)):
                # print(len(last_excitations))
                # print(len(weights[j]))
                aux += weights[j][k] * last_excitations[k]
            results.append(aux)
        
        return results
