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
        self.best_weights_decoder = None
        self.best_weights_encoder = None
        self.best_biases_decoder = None
        self.best_biases_encoder = None


    def train(self, input_data, learning_rate, max_error, max_epochs):
        epoch = 0
        best_epoch = sys.maxsize
        best_error = sys.maxsize
        while epoch < max_epochs:
            epoch += 1
            total_reconstruction_error = 0.0
            for i in range(input_data.shape[0]):
                x = input_data[i].reshape(1, -1)
                encoder_activations = self.encoder.forward_propagation(x)
                decoder_activations = self.decoder.forward_propagation(encoder_activations[-1])
                error = x - decoder_activations[-1]

                # Backpropagation for encoder and decoder
                decoder_delta = self.decoder.backward_propagation(decoder_activations, x, learning_rate, epoch, True)
                self.encoder.backward_propagation(encoder_activations, decoder_delta, learning_rate, epoch, False)
                # self.encoder.backward_propagation(encoder_activations, encoder_activations[-1], learning_rate, epoch, False)

                # Compute reconstruction error
                reconstruction_error = np.mean(np.square(error))
                total_reconstruction_error += reconstruction_error

            avg_reconstruction_error = total_reconstruction_error / input_data.shape[0]
            if avg_reconstruction_error < best_error:
                best_epoch = epoch
                best_error = avg_reconstruction_error
                self.best_weights_decoder = self.decoder.weights
                self.best_weights_encoder = self.encoder.weights
                self.best_biases_decoder = self.decoder.biases
                self.best_biases_encoder = self.encoder.biases


            if avg_reconstruction_error < max_error:
                break  # Stop training if the error is below the specified threshold

        print(f"Epoch {epoch}/{max_epochs}, Avg. Reconstruction Error: {best_error:.4f}")

    def test(self, input_data):
        encoder_activations = self.encoder.test(input_data ,self.best_weights_encoder, self.best_biases_encoder)
        decoder_activations = self.decoder.test(encoder_activations[-1], self.best_weights_decoder, self.best_biases_decoder)

        return decoder_activations[-1]

