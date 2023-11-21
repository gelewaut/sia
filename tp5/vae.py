from autoencoder import Autoencoder, Encoder, Decoder
import sys
import numpy as np
from neuronal_network import NeuralNetwork

class Sampler(NeuralNetwork):
    def __init__(self, size):
        self.size = size
    
    def forward_propagation(self, x):
        e = np.random.standard_normal(size=(self.size))
        z = np.array_split(x[0], 2)
        sigma = np.array([z[0]])
        mu = np.array([z[1]])
        return sigma * e + mu, e, sigma, mu
    
    def backward_propagation(self, e, y):
        sigma_gradient = y * e
        mu_gradient = y
        return np.concatenate((sigma_gradient, mu_gradient), axis=1)
    
    def calculate_KL(self, sigma, mu, batch_size):
        # print(sigma, mu, np.exp(sigma), np.square(mu))
        return 0.5 * np.sum(-1 -sigma + np.square(mu) + (np.exp(sigma)), axis=0) / (self.size * batch_size)
        

class VAE(Autoencoder):
    def __init__(self, input_size, encoding_size, encoder_hidden_layers, decoder_hidden_layers, beta):
        layer_sizes = [input_size] + encoder_hidden_layers + [encoding_size * 2]
        self.encoder = Encoder(layer_sizes, beta)
        self.sampler = Sampler(encoding_size)
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
                
                # Encoder Forward Prop
                encoder_activations = self.encoder.forward_propagation(x)
                z, e, sigma, mu = self.sampler.forward_propagation(encoder_activations[-1])

                # Reparametrization
                # sigma = encoder_activations[-1][0][0]
                # mu = encoder_activations[-1][0][1]
                # e = np.random.normal(0,1)
                # z = (e * sigma) + mu

                # Decoder Forward Prop
                decoder_activations = self.decoder.forward_propagation(z)
                error = x - decoder_activations[-1]
                mse = np.mean(np.square(error))

                # Backpropagation for encoder and decoder
                sampler_delta = self.decoder.backward_propagation(decoder_activations, x, learning_rate, epoch, True)
                decoder_delta = self.sampler.backward_propagation(e, sampler_delta)

                # KL
                KL = self.sampler.calculate_KL(sigma, mu, input_data.shape[0])
                # print(KL)

                # BackProp Encoder
                # decoder_delta = np.array([[decoder_delta[0] * e - KL, decoder_delta[0] - KL]])
                self.encoder.backward_propagation(encoder_activations, decoder_delta, learning_rate, epoch, False)

                reconstruction_error = mse - np.mean(KL)
                # print(mse, np.mean(KL))
                total_reconstruction_error += reconstruction_error

            avg_reconstruction_error = total_reconstruction_error / input_data.shape[0]
            # print(avg_reconstruction_error)
            if avg_reconstruction_error < best_error:
                best_epoch = epoch
                best_error = avg_reconstruction_error
                self.best_weights_decoder = self.decoder.weights
                self.best_weights_encoder = self.encoder.weights
                self.best_biases_decoder = self.decoder.biases
                self.best_biases_encoder = self.encoder.biases

            if avg_reconstruction_error < max_error:
                break  # Stop training if the error is below the specified threshold

            if epoch%500==0:
                print(epoch)

        print(f"Epoch {epoch}/{max_epochs}, Avg. Reconstruction Error: {best_error:.4f}")

    def calculate_KL(self, sigma, mu):
        # print(sigma, mu, np.exp(sigma), np.square(mu))
        return 0.5 * np.sum(-1 - sigma + np.square(mu) + (np.exp(sigma)), axis=0)
    
    def test(self, input_data):
        encoder_activations = self.encoder.test(input_data , self.best_weights_encoder, self.best_biases_encoder)
        z, e, sigma, mu = self.sampler.forward_propagation(encoder_activations[-1])
        # print(z, e, sigma, mu)
        decoder_activations = self.decoder.test(z, self.best_weights_decoder, self.best_biases_decoder)

        return decoder_activations[-1], encoder_activations[-1]

    def generate(self, x):
        z, e, sigma, mu = self.sampler.forward_propagation(x)
        # print(z, e, sigma, mu)
        decoder_activations = self.decoder.test(z, self.best_weights_decoder, self.best_biases_decoder)

        return decoder_activations[-1]