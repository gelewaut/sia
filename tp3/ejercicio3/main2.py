import numpy as np

import layer2
import multilayer_perceptron2 as mp

if __name__ == "__main__":
    exercise = "c"

    examples_a = np.array([[1, -1, 1], [1, 1, -1], [1, -1, -1], [1, 1, 1]])
    targets_a = np.array([[1], [1], [-1], [-1]])
    test_a = examples_a[1]

    file = open('TP3-ej3-digitos.txt')
    lines = file.readlines()

    examples_b_c = []
    targets_b = []
    targets_c = []
    number = [1]
    for i in range(len(lines)):
        digits = lines[i].split()
        for digit in digits:
            number.append(int(digit))
        if (i + 1) % 7 == 0:
            target_b = np.array([1, 0]) if len(examples_b_c) % 2 == 0 else np.array([0, 1])
            targets_b.append(target_b)
            target_c = np.full(10, -1)
            target_c[len(examples_b_c)] = 1
            targets_c.append(target_c)
            examples_b_c.append(number)
            number = [1]

    test_b_c = examples_b_c[4]

    output_nodes_a = 1
    hidden_layer_nodes_a = 6
    hidden_layers_a = 6

    output_nodes_b = 2
    hidden_layer_nodes_b = 6
    hidden_layers_b = 6

    output_nodes_c = 10
    hidden_layer_nodes_c = 35
    hidden_layers_c = 2

    beta_a = 1
    beta_b = 1
    beta_c = 2.5e-01

    epochs = 30000
    apprentice_rate = 0.1
    error_wanted = 0.00001


    def activation_function(x):
        return np.tanh(beta * x)


    def activation_derivative(x):
        return beta * (1 - activation_function(x) ** 2)


    examples = []
    targets = []
    test = []
    output_nodes = 0
    hidden_layer_nodes = 0
    hidden_layers = 0
    beta = 0

    if exercise == "a":
        examples = examples_a
        targets = targets_a
        test = test_a
        output_nodes = output_nodes_a
        hidden_layer_nodes = hidden_layer_nodes_a
        hidden_layers = hidden_layers_a
        beta = beta_a
    elif exercise == "b":
        examples = examples_b_c
        targets = targets_b
        test = test_b_c
        output_nodes = output_nodes_b
        hidden_layer_nodes = hidden_layer_nodes_b
        hidden_layers = hidden_layers_b
        beta = beta_b
    elif exercise == "c":
        examples = examples_b_c
        targets = targets_c
        test = test_b_c
        output_nodes = output_nodes_c
        hidden_layer_nodes = hidden_layer_nodes_c
        hidden_layers = hidden_layers_c
        beta = beta_c

    layers = []
    for i in range(hidden_layers):
        layers.append(layer2.Layer2(hidden_layer_nodes, activation_function, activation_derivative))
    layers.append(layer2.Layer2(output_nodes, activation_function, activation_derivative))
    perceptron = mp.MultilayerPerceptron2(layers, targets, epochs, error_wanted, examples, apprentice_rate)
    perceptron.train()
    perceptron.test(test)
