import numpy as np
import configparser

import layer2
import multilayer_perceptron2 as mp

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.ini')

    exercise = config.get('General', 'exercise')
    epochs = config.getint('General', 'epochs')
    apprentice_rate = config.getfloat('General', 'apprentice_rate')
    error_wanted = config.getfloat('General', 'error_wanted')

    examples_a = np.array([[1, -1, 1], [1, 1, -1], [1, -1, -1], [1, 1, 1]])
    targets_a = np.array([[1], [1], [-1], [-1]])
    test_a = examples_a[config.getint('ExerciseA', 'test')]

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

    test_b = examples_b_c[config.getint('ExerciseB', 'test')]
    test_c = examples_b_c[config.getint('ExerciseC', 'test')]

    output_nodes_a = config.getint('ExerciseA', 'output_nodes')
    hidden_layer_nodes_a = config.getint('ExerciseA', 'hidden_layer_nodes')
    hidden_layers_a = config.getint('ExerciseA', 'hidden_layers')

    output_nodes_b = config.getint('ExerciseB', 'output_nodes')
    hidden_layer_nodes_b = config.getint('ExerciseB', 'hidden_layer_nodes')
    hidden_layers_b = config.getint('ExerciseB', 'hidden_layers')

    output_nodes_c = config.getint('ExerciseC', 'output_nodes')
    hidden_layer_nodes_c = config.getint('ExerciseB', 'hidden_layer_nodes')
    hidden_layers_c = config.getint('ExerciseB', 'hidden_layers')

    beta_a = config.getfloat('ExerciseA', 'beta')
    beta_b = config.getfloat('ExerciseB', 'beta')
    beta_c = config.getfloat('ExerciseC', 'beta')


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
        test = test_b
        output_nodes = output_nodes_b
        hidden_layer_nodes = hidden_layer_nodes_b
        hidden_layers = hidden_layers_b
        beta = beta_b
    elif exercise == "c":
        examples = examples_b_c
        targets = targets_c
        test = test_c
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
