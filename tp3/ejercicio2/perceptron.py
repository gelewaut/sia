import numpy as np
import sys
import random

class Perceptron():

    def __init__(self, apprentice_rate, limit, epsilon):
        self.apprentice_rate = apprentice_rate
        self.epsilon = epsilon
        self.w_min = None
        self.limit = limit
        self.min_error = sys.maxsize
        self.error = None
        self.epochs = 0

    def train(self, data):
        length = len(data[0])
        w = self.initialize_weights(length - 1)
        errors = []

        while self.min_error > self.epsilon and self.epochs < self.limit:
            aux = random.randint(0, len(data)-1)
            test_data = data[aux]
            excitement = self.linear_output(test_data, w)
            activation = self.activation_fun(excitement)
            delta_w = self.calculate_delta_weights(test_data[length - 1], activation, test_data)
            w = self.new_weights(w, delta_w)
            error = self.compute_error(data, w)
            if error < self.min_error:
                self.min_error = error
                self.w_min = w
            self.epochs += 1
            errors.append(error)
        
        return errors
    
    def test(self, data):
        return self.compute_error(data, self.w_min)
        

    def linear_output(self, data, weights):
        aux = 0
        for i in range(len(data) - 1):
            aux += weights[i]*data[i]

        return aux

    def new_weights(self, weights, delta_weights):
        for i in range(len(weights)):
            weights[i] = weights[i] + delta_weights[i]
        return weights

    def initialize_weights(self, length):
        aux = []
        for _ in range(length):
            aux.append(random.randint(10,10))
        return aux
    
    def compute_error(self, data, weights):
        pass

    def calculate_delta_weights(self, expected, output, data):
        pass

    def activation_fun(self, excitement):
        pass


class NonLinearPerceptron (Perceptron):

    def __init__(self, apprentice_rate, limit, epsilon, beta):
        super().__init__(apprentice_rate, limit, epsilon)
        self.beta = beta

    def compute_error(self, data, weights):
        aux = 0
        for aux_data in data:
            aux += pow(aux_data[len(aux_data) - 1] - np.tanh(self.beta * self.linear_output(aux_data, weights)), 2)
        return aux/2

    def calculate_delta_weights(self, expected, output, data):
        delta_weights = []  
        aux = self.apprentice_rate * (expected - output) * (self.beta*(1 - pow(np.tanh(output),2)))
        for i in range(len(data) - 1):
            delta_weights.append(aux * data[i])

        return delta_weights

    def activation_fun(self, excitement):
        return np.tanh(self.beta * excitement)
    
class LinearPerceptron (Perceptron):
    def __init__(self, apprentice_rate, limit, epsilon):
        super().__init__(apprentice_rate, limit, epsilon)
    
    def compute_error(self, data, weights):
        aux = 0
        for aux_data in data:
            aux += pow(aux_data[len(aux_data) - 1] - self.linear_output(aux_data, weights), 2)
        return aux/2

    def calculate_delta_weights(self, expected, output, data):
        delta_weights = []  
        aux = self.apprentice_rate * (expected - output)
        for i in range(len(data) - 1):
            delta_weights.append(aux * data[i])

        return delta_weights

    def activation_fun(self, excitement):
        return excitement



        

        