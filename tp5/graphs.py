from font import Font3
from plot_letter import print_letter_7x8
import numpy as np
from autoencoder import Autoencoder
from autoencoder import Denoising
from autoencoder import Generative
import configparser
import matplotlib.pyplot as plt


# AUX FUNCTIONS

def digit_to_binary_flat(digit):
    binary_row = [int(bit) for binary_str in [format(element, '05b') for element in digit] for bit in binary_str]
    return binary_row


def binary_flat_to_digit(binary_flat):
    digits = []
    for i in range(0, len(binary_flat), 5):  # Chaque chiffre est représenté par 5 bits
        binary_str = ''.join(str(int(bit)) for bit in binary_flat[i:i + 5])
        digit = int(binary_str, 2)  # Convertir la chaîne binaire en entier
        digits.append(digit)
    return digits


def add_noise(data, noise_rate):
    noisy_data = np.array(data, dtype=float)
    mask = data == 0
    noise = np.random.uniform(0, noise_rate, size=data.shape)
    noisy_data[mask] = noise[mask]
    noisy_data[~mask] = 1 - noise[~mask]
    return noisy_data


def print_letter(letter):
    reshaped_letter = np.reshape(letter, (7, 5))
    plt.imshow(reshaped_letter, cmap='gray_r', interpolation='nearest', vmin=0, vmax=1)
    plt.axis('off')
    plt.colorbar().remove()
    plt.show()


# GRAPH FUNCTIONS

def error_vs_epochs(encoding_size, beta, input_data, learning_rate, max_epochs):
    reshaped_input_size = input_data.shape[1]
    graph, line = plt.subplots()

    layers_0 = [[20, 8], [8, 20]]
    layers_1 = [[27, 19, 11], [11, 19, 27]]
    layers_2 = [[30, 20, 10, 5], [5, 10, 20, 30]]
    layers_3 = [[30, 25, 20, 15, 10, 5], [5, 10, 15, 20, 25, 30]]
    layers_4 = [[31, 23, 19, 17, 13, 11, 7, 5, 3], [3, 5, 7, 11, 13, 17, 19, 23, 31]]

    all_layers = [layers_0, layers_1, layers_2, layers_3, layers_4]
    all_labels = ['a', 'b', 'c', 'd', 'e']

    for j in range(len(all_layers)):
        print(j)
        autoencoder = Autoencoder(reshaped_input_size, encoding_size, all_layers[j][0], all_layers[j][1], beta)
        epochs = []
        errors = []
        for i in range(1, 101):
            autoencoder.train(input_data, learning_rate, 0, max_epochs)
            epochs.append(i * max_epochs)
            errors.append(autoencoder.best_error)
        line.plot(epochs, errors, label=all_labels[j], linewidth=1)

    line.set_xlabel('Epocas')
    line.set_ylabel('Error')
    line.set_title('Autoencoders')
    line.legend()
    plt.show()


def print_all_letters(encoding_size, encoder_hidden_layers, decoder_hidden_layers, beta, input_data, learning_rate, max_error, max_epochs):
    reshaped_input_size = input_data.shape[1]
    autoencoder = Autoencoder(reshaped_input_size, encoding_size, encoder_hidden_layers, decoder_hidden_layers, beta)

    autoencoder.train(input_data, learning_rate, max_error, max_epochs)

    reconstructed_data = []
    for i in range(input_data.shape[0]):
        x = input_data[i].reshape(1, -1)
        encoded_data, latent_space = autoencoder.test(x)
        reconstructed_data.append(encoded_data)

    for index in range(len(reconstructed_data)):
        print_letter(reconstructed_data[index])


def error_vs_learning_rate(encoding_size, beta, input_data, encoder_hidden_layers, decoder_hidden_layers, max_epochs):
    reshaped_input_size = input_data.shape[1]

    learning_rates = [0.001, 0.01, 0.1, 1]
    errors = []
    for learning_rate in learning_rates:
        print(learning_rate)
        sum = 0
        for j in range(10):
            autoencoder = Autoencoder(reshaped_input_size, encoding_size, encoder_hidden_layers, decoder_hidden_layers, beta)
            autoencoder.train(input_data, learning_rate, 0, max_epochs)
            sum += autoencoder.best_error
        errors.append(sum/10)

    plt.bar([str(learning_rate) for learning_rate in learning_rates], errors)
    plt.xlabel('Tasa')
    plt.ylabel('Error')
    plt.show()


def error_vs_beta(encoding_size, beta, input_data, encoder_hidden_layers, decoder_hidden_layers, max_epochs, learning_rate):
    reshaped_input_size = input_data.shape[1]

    betas = []
    errors = []
    for i in range(1, 101):
        print(i)
        sum = 0
        for j in range(10):
            autoencoder = Autoencoder(reshaped_input_size, encoding_size, encoder_hidden_layers, decoder_hidden_layers, beta * i)
            autoencoder.train(input_data, learning_rate, 0, max_epochs)
            sum += autoencoder.best_error
        betas.append(i * beta)
        errors.append(sum/10)

    plt.plot(betas, errors)
    plt.xlabel('Beta')
    plt.ylabel('Error')
    plt.show()


def latent_space(encoding_size, encoder_hidden_layers, decoder_hidden_layers, beta, input_data, learning_rate,
                 max_error, max_epochs):
    reshaped_input_size = input_data.shape[1]
    autoencoder = Autoencoder(reshaped_input_size, encoding_size, encoder_hidden_layers, decoder_hidden_layers, beta)

    autoencoder.train(input_data, learning_rate, max_error, max_epochs)

    latent_space_graph = []
    for i in range(input_data.shape[0]):
        x = input_data[i].reshape(1, -1)
        encoded_data, latent_space = autoencoder.test(x)
        latent_space_graph.append(latent_space[0])

    letters = ['`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'DEL']

    i = 0
    for space in latent_space_graph:
        plt.scatter(space[0], space[1], marker='o', label=letters[i])
        i += 1
    x_coordinates, y_coordinates = zip(*latent_space_graph)
    plt.scatter(x_coordinates, y_coordinates, color='blue', marker='o', label='Points')
    for i, label in enumerate(letters):
        plt.annotate(label, (latent_space_graph[i][0], latent_space_graph[i][1]), textcoords="offset points",
                     xytext=(0, 5), ha='center')

    plt.title('Espacio Latente')
    plt.show()


def generate_new_letter(encoding_size, encoder_hidden_layers, decoder_hidden_layers, beta, input_data, learning_rate, max_error, max_epochs):
    reshaped_input_size = input_data.shape[1]
    autoencoder = Generative(reshaped_input_size, encoding_size, encoder_hidden_layers, decoder_hidden_layers, beta)

    autoencoder.train(input_data, learning_rate, max_error, max_epochs)

    fig, axs = plt.subplots(21, 21, figsize=(12, 12))
    columns = 0
    rows = 0
    for x in range(21):
        x_value = x * 0.05
        for y in reversed(range(21)):
            y_value = y * 0.05
            letter = autoencoder.test([x_value, y_value])
            ax = axs[columns, rows]
            reshaped_letter = np.reshape(letter, (7, 5))
            ax.imshow(reshaped_letter, cmap='gray_r', interpolation='nearest', vmin=0, vmax=1)
            ax.axis('off')
            columns += 1
        rows += 1
        columns = 0
    fig.tight_layout(pad=0.5)

    plt.show()


def denoise_structures(encoding_size, beta, input_data, learning_rate, max_epochs, noise_rate):
    reshaped_input_size = input_data.shape[1]
    graph, line = plt.subplots()

    noisy_data = add_noise(input_data, noise_rate)

    layers_0 = [[20, 8], [8, 20]]
    layers_1 = [[27, 19, 11], [11, 19, 27]]
    layers_2 = [[30, 20, 10, 5], [5, 10, 20, 30]]
    layers_3 = [[30, 25, 20, 15, 10, 5], [5, 10, 15, 20, 25, 30]]
    layers_4 = [[31, 23, 19, 17, 13, 11, 7, 5, 3], [3, 5, 7, 11, 13, 17, 19, 23, 31]]

    all_layers = [layers_0, layers_1, layers_2, layers_3, layers_4]
    all_labels = ['a', 'b', 'c', 'd', 'e']

    for j in range(len(all_layers)):
        print(j)
        autoencoder = Denoising(reshaped_input_size, encoding_size, all_layers[j][0], all_layers[j][1], beta)
        epochs = []
        errors = []
        for i in range(1, 101):
            autoencoder.train(noisy_data, input_data, learning_rate, max_epochs)
            epochs.append(i * max_epochs)
            errors.append(autoencoder.best_error)
        line.plot(epochs, errors, label=all_labels[j], linewidth=1)

    line.set_xlabel('Epocas')
    line.set_ylabel('Error')
    line.set_title('Denoising Autoencoders')
    line.legend()
    plt.show()


def error_vs_noise(encoding_size, beta, input_data, encoder_hidden_layers, decoder_hidden_layers, max_epochs, learning_rate):
    reshaped_input_size = input_data.shape[1]

    noises = []
    errors = []
    for i in range(1, 11):
        print(i)
        sum = 0
        for j in range(10):
            noisy_data = add_noise(input_data, noise_rate * i)
            autoencoder = Denoising(reshaped_input_size, encoding_size, encoder_hidden_layers, decoder_hidden_layers, beta)
            autoencoder.train(noisy_data, input_data, learning_rate, max_epochs)
            sum += autoencoder.best_error
        noises.append(noise_rate * i)
        errors.append(sum/10)

    plt.plot(noises, errors)
    plt.xlabel('Tasa')
    plt.ylabel('Error')
    plt.show()


def denoise(encoding_size, beta, input_data, learning_rate, max_epochs, noise_rate):
    reshaped_input_size = input_data.shape[1]
    noisy_data = add_noise(input_data, noise_rate)

    autoencoder = Denoising(reshaped_input_size, encoding_size, encoder_hidden_layers, decoder_hidden_layers, beta)
    autoencoder.train(noisy_data, input_data, learning_rate, max_epochs)

    reconstructed_data = []
    for i in range(input_data.shape[0]):
        x = noisy_data[i].reshape(1, -1)
        encoded_data, latent_space = autoencoder.test(x)
        reconstructed_data.append(encoded_data)

    for index in range(len(reconstructed_data)):
        print_letter(noisy_data[index])
        print_letter(reconstructed_data[index])


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')

    beta = config.getfloat('General', 'beta')
    encoder_hidden_layers_str = config.get('General', 'encoder_hidden_layers')
    encoder_hidden_layers = [int(layer_size) for layer_size in encoder_hidden_layers_str.strip('[]').split(',')]
    decoder_hidden_layers_str = config.get('General', 'decoder_hidden_layers')
    decoder_hidden_layers = [int(layer_size) for layer_size in decoder_hidden_layers_str.strip('[]').split(',')]
    encoding_size = config.getint('General', 'encoding_size')
    learning_rate = config.getfloat('General', 'learning_rate')
    max_epochs = config.getint('General', 'max_epochs')
    max_error = config.getfloat('General', 'max_error')
    noise_rate = config.getfloat('Denoising', 'noise_rate')

    # Original data
    original_data = np.array(Font3)
    dataset_size = original_data.shape[0]
    input_size = original_data.shape[1]
    original_data_reshape = original_data.reshape(dataset_size, input_size)
    # Convert each digit in original_data to binary and reshape
    binary_data = [digit_to_binary_flat(letter) for letter in original_data]

    # Reshape binary data to match the input size of 35 (5 * 7)
    input_data = np.array(binary_data).reshape(original_data.shape[0], -1)

    # error_vs_epochs(encoding_size, beta, input_data, learning_rate, max_epochs)
    # latent_space(encoding_size, encoder_hidden_layers, decoder_hidden_layers, beta, input_data, learning_rate, max_error, max_epochs)
    # denoise_structures(encoding_size, beta, input_data, learning_rate, max_epochs, noise_rate)
    # denoise(encoding_size, beta, input_data, learning_rate, max_epochs, noise_rate)
    # generate_new_letter(encoding_size, encoder_hidden_layers, decoder_hidden_layers, beta, input_data, learning_rate, max_error, max_epochs)
    # error_vs_beta(encoding_size, beta, input_data, encoder_hidden_layers, decoder_hidden_layers, max_epochs, learning_rate)
    # print_all_letters(encoding_size, encoder_hidden_layers, decoder_hidden_layers, beta, input_data, learning_rate, max_error, max_epochs)
    # error_vs_noise(encoding_size, beta, input_data, encoder_hidden_layers, decoder_hidden_layers, max_epochs, learning_rate)
    error_vs_learning_rate(encoding_size, beta, input_data, encoder_hidden_layers, decoder_hidden_layers, max_epochs)
