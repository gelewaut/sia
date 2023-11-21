from font import Font3
from plot_letter import print_letter_7x8
import numpy as np
import csv
from vae import VAE
import configparser
import matplotlib.pyplot as plt
import seaborn as sns
from ej1 import digit_to_binary_flat, binary_flat_to_digit
from emojis import emoji_size, emoji_images, emoji_chars, emoji_names


if __name__ == '__main__': 
    config = configparser.ConfigParser()
    config.read('config.ini')

    beta = config.getfloat('VAE', 'beta')
    encoder_hidden_layers_str = config.get('VAE', 'encoder_hidden_layers')
    encoder_hidden_layers = [int(layer_size) for layer_size in encoder_hidden_layers_str.strip('[]').split(',')]
    decoder_hidden_layers_str = config.get('VAE', 'decoder_hidden_layers')
    decoder_hidden_layers = [int(layer_size) for layer_size in decoder_hidden_layers_str.strip('[]').split(',')]
    encoding_size = config.getint('VAE', 'encoding_size')

    # emoji_indexes = np.array([0, 3, 4, 6, 7, 95])
    emoji_indexes = np.array( [0, 3, 7, 8, 9, 29, 31, 46, 50,
                              57, 62,85, 95] )

    data = np.array(emoji_images)
    dataset_input = data[emoji_indexes]
    dataset_input_list = list(dataset_input)


    # Original data
    original_data = dataset_input
    dataset_size = original_data.shape[0]
    input_size = original_data.shape[1]
    original_data_reshape = original_data.reshape(dataset_size, input_size)
    # Convert each digit in original_data to binary and reshape
    # binary_data = [digit_to_binary_flat(letter) for letter in original_data]

    # Reshape binary data to match the input size of 35 (5 * 7)
    input_data = np.array(original_data_reshape).reshape(original_data.shape[0], -1)
    reshaped_input_size = input_data.shape[1]
    autoencoder = VAE(reshaped_input_size, encoding_size, encoder_hidden_layers, decoder_hidden_layers, beta)

    learning_rate = 0.01
    max_epochs = 10000
    max_error = 0.01

    autoencoder.train(input_data, learning_rate, max_error, max_epochs)

    reconstructed_data = []

    fig, axs = plt.subplots(21, 21, figsize=(12, 12))
    columns = 0
    rows = 0
    for x in range(21):
        x_value = x * 0.05
        for y in reversed(range(21)):
            y_value = y * 0.05
            letter = autoencoder.generate([[x_value, y_value]])
            ax = axs[columns, rows]
            reshaped_letter = np.reshape(letter, (20, 20))
            ax.imshow(reshaped_letter, cmap='gray_r', interpolation='nearest', vmin=0, vmax=1)
            ax.axis('off')
            columns += 1
        rows += 1
        columns = 0
    fig.tight_layout(pad=0.5)

    plt.show()