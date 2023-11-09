import numpy as np


def activation_function(beta, x):
    return np.tanh(beta * x)


def derivative_function(beta, x):
    return beta * (1 - activation_function(beta, x) ** 2)

class NeuralNetwork:
    def __init__(self, layer_sizes, beta):
        self.layer_sizes = layer_sizes
        self.beta = beta
        self.num_layers = len(layer_sizes)
        self.weights = [np.random.randn(layer_sizes[i], layer_sizes[i+1]) for i in range(self.num_layers - 1)]
        self.biases = [np.zeros((1, layer_sizes[i+1])) for i in range(self.num_layers - 1)]

    def forward_propagation(self, x):
        activations = [x]
        layer_input = x
        for i in range(self.num_layers - 1):
            layer_output = np.dot(layer_input, self.weights[i]) + self.biases[i]
            activation = activation_function(self.beta, layer_output)
            activations.append(activation)
            layer_input = activation
        return activations

    def backward_propagation(self, x, y, learning_rate):
        activations = self.forward_propagation(x)
        layer_input = x
        deltas = []
        for i in range(self.num_layers - 1, 0, -1):
            activation = activations[i]
            prev_activation = activations[i - 1]
            if i == self.num_layers - 1:
                delta = (activation - y) * derivative_function(self.beta, activation)
            else:
                delta = delta.dot(self.weights[i].T) * derivative_function(self.beta, activation)
            deltas.insert(0, delta)
            weight_gradient = prev_activation.T.dot(delta)
            bias_gradient = np.sum(delta, axis=0, keepdims=True)
            self.weights[i-1] -= learning_rate * weight_gradient
            self.biases[i-1] -= learning_rate * bias_gradient

    def train(self, X, y, learning_rate, epochs):
        for epoch in range(epochs):
            for i in range(X.shape[0]):
                x = X[i].reshape(1, -1)
                y_true = y[i].reshape(1, -1)
                self.backward_propagation(x, y_true, learning_rate)

    def predict(self, x):
        return self.forward_propagation(x)[-1]

# Example usage:
if __name__ == "__main__":
    # Define the network architecture and activation functions
    layer_sizes = [2, 3, 2, 1]  # Input layer, two hidden layers, output layer
    # Create the neural network
    nn = NeuralNetwork(layer_sizes, 1)

    # Generate some random data for training
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])

    # Train the network
    learning_rate = 0.1
    epochs = 10000
    nn.train(X, y, learning_rate, epochs)

    # Make predictions
    for input_data in X:
        prediction = nn.predict(input_data.reshape(1, -1))
        print(f"Input: {input_data}, Prediction: {prediction}")
