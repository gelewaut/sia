from font import Font3
from plot_letter import print_letter_7x8
import numpy as np
from autoencoder import Autoencoder
import configparser
import matplotlib.pyplot as plt


# Function to convert a digit to binary representation of size 5
def digit_to_binary_flat(digit):
    binary_row = [int(bit) for binary_str in [format(element, '05b') for element in digit] for bit in binary_str]
    return binary_row


def binary_flat_to_digit(binary_flat):
    digits = []
    for i in range(0, len(binary_flat), 5):  # Chaque chiffre est représenté par 5 bits
        binary_str = ''.join(str(int(bit)) for bit in binary_flat[i:i+5])
        digit = int(binary_str, 2)  # Convertir la chaîne binaire en entier
        digits.append(digit)
    return digits


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
    autoencoder = Autoencoder(reshaped_input_size, encoding_size, encoder_hidden_layers, decoder_hidden_layers, beta)

    learning_rate = 0.01
    max_epochs = 10000
    max_error = 1/35

    autoencoder.train(input_data, learning_rate, max_error, max_epochs)

    # Reconstruction of example data
    reconstructed_data = []
    latent_space_graph = []
    for i in range(input_data.shape[0]):
        x = input_data[i].reshape(1, -1)
        encoded_data, latent_space = autoencoder.test(x)
        binary_output = np.round(encoded_data)  # Arrondir pour obtenir des valeurs binaires
        reconstructed_data.append(binary_output)
        latent_space_graph.append(latent_space[0])

    letters=['`', 'a', 'b', 'c', 'd', 'e', 'f', 'g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','{','|','}','~','DEL']
    # i=0
    # for space in latent_space_graph:
    #     plt.scatter(space[0], space[1], marker='o', label=letters[i])
    #     i+=1
    # x_coordinates, y_coordinates = zip(*latent_space_graph)
    # plt.scatter(x_coordinates, y_coordinates, color='blue', marker='o', label='Points')
    for i, label in enumerate(letters):
        plt.annotate(label, (latent_space_graph[i][0], latent_space_graph[i][1]), textcoords="offset points", xytext=(0, 5), ha='center')
    plt.title('Scatter Plot with Letters')

    # Display the plot
    plt.show()
    
    reconstructed_data = np.array(reconstructed_data).reshape(dataset_size, 35)

    digit_reconstructed_data = [binary_flat_to_digit(binary_row) for binary_row in reconstructed_data]

    # Afficher les données originales et reconstruites
    for index in range(len(digit_reconstructed_data)):
        print_letter_7x8(original_data_reshape[index])
        print_letter_7x8(digit_reconstructed_data[index])

