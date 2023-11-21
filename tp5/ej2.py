from font import Font3
from plot_letter import print_letter_7x8
import numpy as np
import csv
from vae import VAE
import configparser
import matplotlib.pyplot as plt
from ej1 import digit_to_binary_flat, binary_flat_to_digit

if __name__ == '__main__': 
    config = configparser.ConfigParser()
    config.read('config.ini')

    beta = config.getfloat('General', 'beta')
    encoder_hidden_layers_str = config.get('General', 'encoder_hidden_layers')
    encoder_hidden_layers = [int(layer_size) for layer_size in encoder_hidden_layers_str.strip('[]').split(',')]
    decoder_hidden_layers_str = config.get('General', 'decoder_hidden_layers')
    decoder_hidden_layers = [int(layer_size) for layer_size in decoder_hidden_layers_str.strip('[]').split(',')]
    encoding_size = config.getint('General', 'encoding_size')

    # Original data
    original_data = np.array(Font3)
    dataset_size = original_data.shape[0]
    input_size = original_data.shape[1]
    original_data_reshape = original_data.reshape(dataset_size, input_size)
    # Convert each digit in original_data to binary and reshape
    binary_data = [digit_to_binary_flat(letter) for letter in original_data]

    # Reshape binary data to match the input size of 35 (5 * 7)
    input_data = np.array(binary_data).reshape(original_data.shape[0], -1)
    reshaped_input_size = input_data.shape[1]
    autoencoder = VAE(reshaped_input_size, encoding_size, encoder_hidden_layers, decoder_hidden_layers, beta)

    learning_rate = 0.01
    max_epochs = 10000
    max_error = 0.01

    autoencoder.train(input_data, learning_rate, max_error, max_epochs)

    reconstructed_data = []
    latent_space_graph = []

    letter = np.random.choice(len(input_data))
    # for i in range(input_data.shape[0]):
    #     x = input_data[i].reshape(1, -1)
    #     encoded_data, latent_space = autoencoder.test(x)
    #     binary_output = np.round(encoded_data)  # Arrondir pour obtenir des valeurs binaires
    #     reconstructed_data.append(binary_output)

    x = input_data[letter].reshape(1, -1)

    for _ in range(5):
        encoded_data, latent_space = autoencoder.test(x)
        binary_output = np.round(encoded_data)
        reconstructed_data.append(binary_output)
        # autoencoder.generate(latent_space)
        # binary_output = np.round(encoded_data)
        # reconstructed_data.append(binary_output)

    reconstructed_data = np.array(reconstructed_data).reshape(10, 35)

    digit_reconstructed_data = [binary_flat_to_digit(binary_row) for binary_row in reconstructed_data]

    # Afficher les données originales et reconstruites
    print_letter_7x8(original_data_reshape[letter])
    for index in range(len(digit_reconstructed_data)):
        print_letter_7x8(digit_reconstructed_data[index])