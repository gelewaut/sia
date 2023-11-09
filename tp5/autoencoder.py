from neuronal_network import NeuralNetwork
import numpy as np


class Encoder(NeuralNetwork):
    pass


class Decoder(NeuralNetwork):
    pass


class Autoencoder:
    def __init__(self, input_size, encoding_size, hidden_layers, beta):
        layer_sizes = [input_size] + hidden_layers + [encoding_size]
        self.encoder = Encoder(layer_sizes, beta)
        layer_sizes = [encoding_size] + hidden_layers + [input_size]
        self.decoder = Decoder(layer_sizes, beta)

    def train(self, input_data, learning_rate, epochs):
        for epoch in range(epochs):
            for i in range(input_data.shape[0]):
                x = input_data[i].reshape(1, -1)
                encoded_data = self.encoder.forward_propagation(x)[-1]
                decoded_data = self.decoder.forward_propagation(encoded_data)[-1]
                error = x - decoded_data

                # Backpropagation for encoder and decoder
                self.encoder.backward_propagation(x, encoded_data, learning_rate)
                self.decoder.backward_propagation(encoded_data, x, learning_rate)

                # Compute reconstruction error
                reconstruction_error = np.mean(np.square(error))
                print(f"Epoch {epoch + 1}/{epochs}, Reconstruction Error: {reconstruction_error:.4f}")






