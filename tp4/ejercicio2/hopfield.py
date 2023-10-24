import numpy
import sys
import random

class Hopfield():
    def __init__(self, patterns):
        self.patterns = patterns
        self.n = len(self.patterns[0])
        self.weights = self.calculate_weights()

    def calculate_weights(self):
        weights = numpy.zeros((self.n, self.n))
        for i in range(self.n):
            for j in range(i+1, self.n):
                aux = 0
                for p in self.patterns:
                    aux += (p[i]*p[j])
                aux /= self.n

                weights[i][j] = aux
                weights[j][i] = aux
                        
        return weights

    def sign(self, s, s_next):
        result = []
        for i in range(len(s_next)):
            if s_next[i] > 0:
                result.append(1)
            elif s_next[i] < 0:
                result.append(-1)
            else:
                result.append(s[i])
        return result


    def algorithm(self, input, epochs):
        epoch = 0
        to_return = []
        to_return.append(input)
        s = numpy.array(self.sign(input, self.weights.dot(input)))
        to_return.append(s)
        while epoch < epochs:
            epoch += 1
            s_next = numpy.array(self.sign(s, self.weights.dot(s)))
            if numpy.array_equal(s, s_next):
                to_return.append(s_next)
                return to_return
            s = s_next
            to_return.append(s)
        
        to_return.append(s_next)
        return to_return
            
    def get_weights(self):
        return self.weights
    
    def get_energy(self, s):
        return self.weights.dot(s).dot(s) / -2.0