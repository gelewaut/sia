import random
import sys

import numpy
import numpy as np


class MultilayerPerceptron2:
    def __init__(self, layers, targets, epochs, error_wanted, examples, apprentice_rate):
        self.layers = layers
        self.inputs = None
        self.target = None
        self.weights = None
        self.targets = targets
        self.epochs = epochs
        self.error_wanted = error_wanted
        self.examples = examples
        self.weights_min = None
        self.apprentice_rate = apprentice_rate

    def initialize_weights(self):
        new_weights = {}
        for m in range(len(self.layers)):
            new_weights[m] = []
            if m == 0:
                for j in range(self.layers[m].nodes_dim):
                    new_weights[m].append(np.random.uniform(-1, 1, size=len(self.examples[0])))
            else:
                for j in range(self.layers[m].nodes_dim):
                    new_weights[m].append(np.random.uniform(-1, 1, size=self.layers[m - 1].nodes_dim + 1))

        self.weights = new_weights

    def forward_propagation(self):
        last_activations = self.inputs
        for m in range(len(self.layers)):
            last_layer = (m == len(self.layers)-1)
            self.layers[m].calculate_excitations(self.weights[m], last_activations)
            self.layers[m].calculate_activations(last_layer)
            last_activations = self.layers[m].activations

    def calculate_gradients(self):
        gradients = {}
        for m in reversed(range(len(self.layers))):
            gradients[m] = []
            derivatives = self.layers[m].calculate_derivative()
            if m == len(self.layers) - 1:
                delta_array = self.target - self.layers[m].activations
                gradients[m] = derivatives * delta_array
            else:
                product_array = numpy.matmul(numpy.transpose(numpy.matrix(self.weights[m + 1])),
                                             numpy.transpose(numpy.matrix(gradients[m + 1])))
                product_array_t = numpy.transpose(product_array)
                for j in range(self.layers[m].nodes_dim):
                    gradients[m].append(derivatives[j] * numpy.ravel(product_array_t)[j + 1])
        return gradients

    def back_propagation(self):
        gradients = self.calculate_gradients()
        activations = self.inputs
        for m in range(len(self.layers) - 1):
            weight_update = np.outer(gradients[m], activations) * self.apprentice_rate
            self.weights[m] += weight_update
            activations = self.layers[m].activations

    def get_error(self):
        error = 0
        for i in range(len(self.targets)):
            self.inputs = self.examples[i]
            self.forward_propagation()
            for j in range(len(self.targets[i])):
                error += (self.layers[len(self.layers)-1].activations[j] - self.targets[i][j])**2
                # print(self.layers[len(self.layers)-1].activations)
        error /= 2
        return error

    def train(self):
        epochs = self.epochs
        min_error = sys.maxsize
        self.initialize_weights()
        while epochs != 0 and min_error > self.error_wanted:
            example = random.randint(0, len(self.examples) - 1)
            self.inputs = self.examples[example]
            self.target = self.targets[example]
            self.forward_propagation()
            self.back_propagation()
            error = self.get_error()
            if error < min_error:
                min_error = error
                self.weights_min = self.weights
            epochs -= 1

    def test(self, inputs):
        self.inputs = inputs
        self.weights = self.weights_min
        self.forward_propagation()
        # print(self.layers[len(self.layers) - 1].activations)

