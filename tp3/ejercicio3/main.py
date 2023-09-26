import numpy as np
import sys
import random
import multilayer_perceptron as mp
import layer 
import copy

if __name__ == "__main__":
    number0 = [
    0, 1, 1, 1, 0,
    1, 0, 0, 0, 1,
    1, 0, 0, 1, 1,
    1, 0, 1, 0, 1,
    1, 1, 0, 0, 1,
    1, 0, 0, 0, 1,
    0, 1, 1, 1, 0
]

    number1 = [
    0, 0, 1, 0, 0, 
    0, 1, 1, 0, 0, 
    0, 0, 1, 0, 0, 
    0, 0, 1, 0, 0, 
    0, 0, 1, 0, 0, 
    0, 0, 1, 0, 0, 
    0, 1, 1, 1, 0 
    ]
    
    number2 = [
    0, 1, 1, 1, 0,
    1, 0, 0, 0, 1,
    0, 0, 0, 0, 1,
    0, 0, 0, 1, 0,
    0, 0, 1, 0, 0,
    0, 1, 0, 0, 0,
    1, 1, 1, 1, 1
    ] 

    number3 = [
    0, 1, 1, 1, 0,
    1, 0, 0, 0, 1,
    0, 0, 0, 0, 1,
    0, 0, 1, 1, 0,
    0, 0, 0, 0, 1,
    1, 0, 0, 0, 1,
    0, 1, 1, 1, 0
    ]
    
    number4 = [
    0, 0, 0, 1, 0,
    0, 0, 1, 1, 0,
    0, 1, 0, 1, 0,
    1, 0, 0, 1, 0,
    1, 1, 1, 1, 1,
    0, 0, 0, 1, 0,
    0, 0, 0, 1, 0
    ]

    number5 = [
    1, 1, 1, 1, 1,
    1, 0, 0, 0, 0,
    1, 1, 1, 1, 0,
    0, 0, 0, 0, 1,
    0, 0, 0, 0, 1,
    1, 0, 0, 0, 1,
    0, 1, 1, 1, 0
    ]

    number6 = [
    0, 0, 1, 1, 0,
    0, 1, 0, 0, 0,
    1, 0, 0, 0, 0,
    1, 1, 1, 1, 0,
    1, 0, 0, 0, 1,
    1, 0, 0, 0, 1,
    0, 1, 1, 1, 0
    ]

    number7 = [
    1, 1, 1, 1, 1,
    0, 0, 0, 0, 1,
    0, 0, 0, 1, 0,
    0, 0, 1, 0, 0,
    0, 1, 0, 0, 0,
    0, 1, 0, 0, 0,
    0, 1, 0, 0, 0
    ]
    
    number8 = [
    0, 1, 1, 1, 0,
    1, 0, 0, 0, 1,
    1, 0, 0, 0, 1,
    0, 1, 1, 1, 0,
    1, 0, 0, 0, 1,
    1, 0, 0, 0, 1,
    0, 1, 1, 1, 0
    ]

    number9 = [
    0, 1, 1, 1, 0,
    1, 0, 0, 0, 1,
    1, 0, 0, 0, 1,
    0, 1, 1, 1, 1,
    0, 0, 0, 0, 1,
    0, 0, 0, 1, 0,
    0, 1, 1, 0, 0
    ]

    numberx = [
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0
    ]
    
    input_nodes = 35
    input_nodes2 = 2
    output_nodes = 10
    output_nodes2 = 1
    output_nodes3 = 2
    hidden_layer_nodes = 35
    epochs = 3000
    apprentice_rate = 0.1  
    error_wanted = 0.000001
    
    beta = 2.5e-01

    empty_row = []
    first_row = copy.copy(empty_row)
    second_row = copy.copy(empty_row)
    second_row.append(1)
    # print(first_row)

    def activation_function(x):
        return np.tanh(beta*x)

    def activation_derivative(x):
        return beta*(1 - activation_function(x)**2)
    bias = 0.1
    examples = [number0, number1, number2, number3, number4, number5, number6, number7, number8, number9]
    targets = [[1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0], [-1.0, 1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0], [-1.0, -1.0, 1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0], 
    [-1.0, -1.0, -1.0, 1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0], [-1.0, -1.0, -1.0, -1.0, 1.0, -1.0, -1.0, -1.0, -1.0, -1.0], [-1.0, -1.0, -1.0, -1.0, -1.0, 1.0, -1.0, -1.0, -1.0, -1.0], [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 1.0, -1.0, -1.0, -1.0],
    [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 1.0, -1.0, -1.0], [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 1.0, -1.0], [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 1.0]]
    examples2 = [[1, 1], [-1, -1], [1, -1], [-1, 1]]
    targets2 = [[-1], [-1], [1], [1]]
    targets3 = [[1, -1], [-1, 1], [1, -1], [-1, 1], [1, -1], [-1, 1], [1, -1], [-1, 1], [1, -1], [-1, 1]]
    # examples_aux = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
    # targets_aux = [[0], [1], [4], [9], [16], [25], [36], [49], [64], [81]]
    layers = []
    layers.append(layer.Layer(input_nodes, activation_function, activation_derivative, bias))
    for i in range(2):
        layers.append(layer.Layer(hidden_layer_nodes, activation_function, activation_derivative, bias))
    layers.append(layer.Layer(output_nodes, activation_function, activation_derivative, bias))
    perceptron = mp.MultilayerPerceptron(layers, targets, epochs, error_wanted, examples, apprentice_rate)
    perceptron.train()
    test_inputs = number9
    # print("pesos despues de train: ", perceptron.weights)
    perceptron.test(test_inputs)
