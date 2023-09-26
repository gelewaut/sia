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
        self.excitations = []

    def get_biases(self):
        return self.biases

    def get_activations(self):
        return self.activations

    def set_activations(self, activations):
        self.activations = activations

    def calculate_activations(self, weights, last_activations):
        results = []
        self.calculate_excitations(weights, last_activations)
        for excitation in self.excitations:
            results.append(self.activation_function(excitation))
        # print('------------------------------------')
        # print(results)
        # print('------------------------------------')        
        self.activations = results

    def calculate_derivative(self):
        results = []
        for excitation in self.excitations:
            results.append(self.activation_derivative(excitation))
        return results

    def calculate_excitations(self, weights, last_activations):
        results = []
        for j in range(self.nodes_dim):
            aux = 0
            for k in range(len(last_activations)):
                # print(len(last_excitations))
                # print(len(weights[j]))
                aux += weights[j][k] * last_activations[k]
                # print(aux)
            results.append(aux)
        # print('------------------------------------')
        # print('excitations:')
        # print(results)
        # print('------------------------------------')
        self.excitations = results
