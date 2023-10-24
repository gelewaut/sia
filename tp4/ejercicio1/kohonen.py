import numpy
import sys
import random


class Kohonen:
    def __init__(self, k, eta, radius):
        self.k = k
        self.eta = eta
        self.radius = radius
        self.grid = numpy.empty((k, k), dtype=numpy.ndarray)

    def train(self, inputs, epochs):
        self.initialize_weights(inputs)
        length = len(inputs)
        epoch = 0

        while epoch < epochs:
            aux = random.randint(0, length - 1)
            data = inputs[aux]
            i, j = self.find_winner(data)
            self.update_weights(data, i, j)
            epoch += 1
            self.eta = 1/(epoch+1)
            if self.radius > 2:
                self.radius -= 1
            else:
                self.radius = numpy.sqrt(2)

    def initialize_weights(self, data):
        length = len(data)

        for i in range(self.k):
            for j in range(self.k):
                aux = random.randint(0, length - 1)
                self.grid[i][j] = numpy.copy(data[aux])

    def find_winner(self, input):
        min_i = 0
        min_j = 0
        min_w = sys.maxsize

        for i in range(self.k):
            for j in range(self.k):
                dist = numpy.linalg.norm(input - self.grid[i][j])
                if dist < min_w:
                    min_w = dist
                    min_i = i
                    min_j = j

        return min_i, min_j

    def update_weights(self, input, i, j):
        for ii in range(self.k):
            for jj in range(self.k):
                if numpy.sqrt((ii - i) ** 2 + (jj - j) ** 2) <= self.radius and not (i == ii and j == jj):
                    self.grid[ii][jj] += self.eta * (input - self.grid[ii][jj])

    def test(self, inputs, countries):
        numbers = numpy.zeros((self.k, self.k))
        group_by_countries = [["" for _ in range(self.k)] for _ in range(self.k)]
        for n in range(len(inputs)):
            i, j = self.find_winner(inputs[n])
            numbers[i][j] += 1
            group_by_countries[i][j] += '\n' + countries[n]

        return numbers, group_by_countries

    def find_winner_by_variable(self, input, variable):
        min_i = 0
        min_j = 0
        min_w = sys.maxsize

        for i in range(self.k):
            for j in range(self.k):
                dist = numpy.linalg.norm(input[variable] - self.grid[i][j][variable])
                if dist < min_w:
                    min_w = dist
                    min_i = i
                    min_j = j

        return min_i, min_j

    def test_by_variable(self, inputs, countries, variable):
        numbers = numpy.zeros((self.k, self.k))
        group_by_countries = [["" for _ in range(self.k)] for _ in range(self.k)]
        for n in range(len(inputs)):
            i, j = self.find_winner_by_variable(inputs[n], variable)
            numbers[i][j] += 1
            group_by_countries[i][j] += '\n' + countries[n]

        return numbers, group_by_countries

    def unified_distance_matrix(self):
        matrix = numpy.empty((self.k, self.k), dtype=int)
        for i in range(self.k):
            for j in range(self.k):
                distance = 0.0
                neighbors = 0

                if i > 0:
                    distance += numpy.linalg.norm(self.grid[i][j] - self.grid[i-1][j])
                    neighbors += 1
                    if j > 0:
                        distance += numpy.linalg.norm(self.grid[i][j] - self.grid[i-1][j-1])
                        neighbors += 1
                    if j < self.k - 1:
                        distance += numpy.linalg.norm(self.grid[i][j] - self.grid[i-1][j+1])
                        neighbors += 1
                if i < self.k-1:
                    distance += numpy.linalg.norm(self.grid[i][j] - self.grid[i+1][j])
                    neighbors += 1
                    if j > 0:
                        distance += numpy.linalg.norm(self.grid[i][j] - self.grid[i+1][j-1])
                        neighbors += 1
                    if j < self.k - 1:
                        distance += numpy.linalg.norm(self.grid[i][j] - self.grid[i+1][j+1])
                        neighbors += 1
                if j > 0:
                    distance += numpy.linalg.norm(self.grid[i][j] - self.grid[i][j-1])
                    neighbors += 1
                if j < self.k-1:
                    distance += numpy.linalg.norm(self.grid[i][j] - self.grid[i][j+1])
                    neighbors += 1

                matrix[i][j] = distance / neighbors
        return matrix
