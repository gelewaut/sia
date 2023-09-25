import numpy as np
import sys
import random

class Layer():
    def __init__(self, nodes_dim, activation_function, activation_derivative, learning_rate, biases):
        self.nodes_dim = nodes_dim
        self.activation_function = activation_function
        self.activation_derivative = activation_derivative
        self.learning_rate = learning_rate
        self.biases = biases
        self.excitations = []

    def get_biases(self):
        return self.biases

    def get_excitation(self):
        return self.excitations

    def calculate_activations(self):
        results = []
        for excitation in self.excitations:
            results.append(self.activation_function(excitation))
        return results

    def calculate_derivative(self):
        results = []
        for excitation in self.excitations:
            results.append(self.activation_derivative(excitation))
        return results

    def calculate_excitations(self, weights, last_excitations):
        results = []
        for j in range(self.nodes_dim):
            aux = 0
            for k in range(len(last_excitations)):
                aux += weights[j][k] * last_excitations[k]
            results.append(aux)
        
        self.excitations = results
