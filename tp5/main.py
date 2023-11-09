import numpy as np
from autoencoder import Autoencoder
from font import Font3
import configparser
from plot_letter import print_letter_7x8

if __name__ == '__main__':

    config = configparser.ConfigParser()
    config.read('config.ini')
    # Define Encoder
    beta = config.getint('General', 'beta')
    hidden_layers_str = config.get('General', 'hidden_layers')
    hidden_layers = [int(layer_size) for layer_size in hidden_layers_str.strip('[]').split(',')]
    encoding_size = config.getint('General', 'encoding_size')

    input_data = np.array(Font3).reshape(32, 7)
    input_size = input_data.shape[1]

    # Create autoencodeur
    autoencoder = Autoencoder(input_size, encoding_size, hidden_layers, beta)

    # Train autoencodeur
    learning_rate = 0.1
    epochs = 1000
    autoencoder.train(input_data, learning_rate, epochs)

    # Reconstruction des données d'exemple
    reconstructed_data = []
    for i in range(input_data.shape[0]):
        x = input_data[i].reshape(1, -1)
        decoded_data = autoencoder.decoder.forward_propagation(autoencoder.encoder.forward_propagation(x)[-1])[-1]
        reconstructed_data.append(decoded_data)

    # Affichage des données originales et reconstruites
    print("Données originales :")
    print(input_data)
    print("Données reconstruites :")
    print(np.array(reconstructed_data).reshape(32, 7))