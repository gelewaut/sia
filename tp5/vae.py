from autoencoder import Autoencoder, Encoder, Decoder
import sys
import numpy as np
from neuronal_network import NeuralNetwork

class Sampler(NeuralNetwork):
    def __init__(self, size):
        self.size = size
    
    def forward_propagation(self, x):
        e = np.random.normal(0,1)
        z = np.split(x, self.size)
        return (z[0] * e) + z[1]
    
    def backward_propagation(self, activations, y, learning_rate, epoch, is_decoder):
        return super().backward_propagation(activations, y, learning_rate, epoch, is_decoder)

class VAE(Autoencoder):
    def __init__(self, input_size, encoding_size, encoder_hidden_layers, decoder_hidden_layers, beta):
        layer_sizes = [input_size] + encoder_hidden_layers + [encoding_size]
        self.encoder = Encoder(layer_sizes, beta)
        layer_sizes = [encoding_size - 1] + decoder_hidden_layers + [input_size]
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
                
                # Encoder Forward Prop
                encoder_activations = self.encoder.forward_propagation(x)
                # z = self.trick.forward_propagation(encoder_activations)

                # Reparametrization
                sigma = encoder_activations[-1][0][0]
                mu = encoder_activations[-1][0][1]
                e = np.random.normal(0,1)
                z = (e * sigma) + mu

                # Decoder Forward Prop
                decoder_activations = self.decoder.forward_propagation(z)
                error = x - decoder_activations[-1]
                mse = np.mean(np.square(error))

                # Backpropagation for encoder and decoder
                decoder_delta = self.decoder.backward_propagation(decoder_activations, x, learning_rate, epoch, True)

                # KL
                KL = self.calculate_KL(sigma, mu)

                # BackProp Encoder
                decoder_delta = np.array([[decoder_delta[0] * e - KL, decoder_delta[0] - KL]])
                self.encoder.backward_propagation(encoder_activations, decoder_delta, learning_rate, epoch, False)

                reconstruction_error = mse
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

    def calculate_KL(self, sigma, mu):
        return 0.5 * np.sum(1 + sigma - np.square(mu) - (np.exp(sigma)))
    
    def test(self, input_data):
        encoder_activations = self.encoder.test(input_data , self.best_weights_encoder, self.best_biases_encoder)
        sigma = encoder_activations[-1][0][0]
        mu = encoder_activations[-1][0][1]
        e = np.random.normal(0,1)
        z = (e * sigma) + mu
        print(sigma, mu, e, z)
        decoder_activations = self.decoder.test(z, self.best_weights_decoder, self.best_biases_decoder)

        return decoder_activations[-1], encoder_activations[-1]

    def generate(self, x):
        sigma = x[0][0]
        mu = x[0][1]
        e = np.random.normal(0,1)
        z = (e * sigma) + mu
        print(sigma, mu, e, z)
        decoder_activations = self.decoder.test(z, self.best_weights_decoder, self.best_biases_decoder)

        return decoder_activations[-1]