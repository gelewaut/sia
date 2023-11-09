import sys

from neuronal_network import NeuralNetwork
import numpy as np


class Encoder(NeuralNetwork):
    pass


class Decoder(NeuralNetwork):
    pass


class Autoencoder:
    def __init__(self, input_size, encoding_size, encoder_hidden_layers, decoder_hidden_layers, beta):
        layer_sizes = [input_size] + encoder_hidden_layers + [encoding_size]
        self.encoder = Encoder(layer_sizes, beta)
        layer_sizes = [encoding_size] + decoder_hidden_layers + [input_size]
        self.decoder = Decoder(layer_sizes, beta)

    def train(self, input_data, learning_rate, max_error, max_epochs):
        epoch = 0
        best_epoch = sys.maxsize
        best_error = sys.maxsize
        while epoch < max_epochs:
            total_reconstruction_error = 0.0
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
                total_reconstruction_error += reconstruction_error

            avg_reconstruction_error = total_reconstruction_error / input_data.shape[0]
            if avg_reconstruction_error < best_error:
                best_epoch = epoch
                best_error = avg_reconstruction_error

            if avg_reconstruction_error < max_error:
                break  # Stop training if the error is below the specified threshold

            epoch += 1
        print(f"Epoch {epoch}/{max_epochs}, Avg. Reconstruction Error: {best_error:.4f}")