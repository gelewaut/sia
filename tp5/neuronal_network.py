import numpy as np


def activation_function(beta, x):
    return np.tanh(beta * x)


def derivative_function(beta, x):
    return beta * (1 - activation_function(beta, x) ** 2)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))


class NeuralNetwork:
    def __init__(self, layer_sizes, beta):
        self.layer_sizes = layer_sizes
        self.beta = beta
        self.num_layers = len(layer_sizes)
        self.weights = [np.random.randn(layer_sizes[i], layer_sizes[i+1]) for i in range(self.num_layers - 1)]
        self.biases = [np.zeros((1, layer_sizes[i+1])) for i in range(self.num_layers - 1)]
        
        #ADAM Parameters
        self.m = [np.zeros((layer_sizes[i], layer_sizes[i+1])) for i in range(self.num_layers - 1)]
        self.v = [np.zeros((layer_sizes[i], layer_sizes[i+1])) for i in range(self.num_layers - 1)]
        self.mg = [np.zeros((1, layer_sizes[i+1])) for i in range(self.num_layers - 1)]
        self.vg = [np.zeros((1, layer_sizes[i+1])) for i in range(self.num_layers - 1)]
        self.a = 0.001
        self.b1 = 0.9
        self.b2 = 0.999
        self.e = 10e-08

    def optimize_weights(self, weight_gradient, learning_rate, i, epoch):
        m_aux = self.b1 * self.m[i-1] + (1-self.b1)*weight_gradient
        v_aux = self.b2 * self.v[i-1] + (1-self.b2)*(weight_gradient**2)
        self.m[i-1] = m_aux
        self.v[i-1] = v_aux
        self.weights[i-1] -= (self.a * m_aux/(1-self.b1**epoch)) / (np.sqrt(v_aux/(1-self.b2**epoch)) + self.e)

    def optimize_biases(self, bias_gradient, learning_rate, i, epoch):
        m_aux = self.b1 * self.mg[i-1] + (1-self.b1)*bias_gradient
        v_aux = self.b2 * self.vg[i-1] + (1-self.b2)*(bias_gradient**2)
        self.mg[i-1] = m_aux
        self.vg[i-1] = v_aux
        self.biases[i-1] -= (self.a * m_aux/(1-self.b1**epoch)) / (np.sqrt(v_aux/(1-self.b2**epoch)) + self.e)

    def forward_propagation(self, x):
        activations = [x]
        for i in range(self.num_layers - 1):
            if i == self.num_layers - 2:  # Last Layer
                activation = sigmoid(np.dot(activations[-1], self.weights[i]) + self.biases[i])
            else:
                activation = np.tanh(np.dot(activations[-1], self.weights[i]) + self.biases[i])
            activations.append(activation)
        return activations

    def backward_propagation(self, activations, y, learning_rate, epoch, is_decoder):
        deltas = []
        is_decoder = True
        for i in range(self.num_layers - 1, 0, -1):
            activation = activations[i]
            prev_activation = activations[i - 1]

            if i == self.num_layers - 1:
                if is_decoder:
                    delta = (activation - y) * sigmoid_derivative(activation)
                else:
                    delta = y * (1 - activation ** 2)
            else:
                delta = deltas[0].dot(self.weights[i].T) * (1 - activation ** 2)  # Pour tanh

            deltas.insert(0, delta)
            weight_gradient = prev_activation.T.dot(delta)
            bias_gradient = np.sum(delta, axis=0, keepdims=True)
            self.optimize_weights(weight_gradient, learning_rate, i, epoch)
            self.optimize_biases(bias_gradient, learning_rate, i, epoch)
            # self.weights[i - 1] -= learning_rate * weight_gradient
            # self.biases[i - 1] -= learning_rate * bias_gradient
        
        return delta[0].dot(self.weights[0].T)

    def train(self, X, y, learning_rate, epochs):
        for epoch in range(epochs):
            for i in range(X.shape[0]):
                x = X[i].reshape(1, -1)
                y_true = y[i].reshape(1, -1)
                self.backward_propagation(x, y_true, learning_rate)

    def predict(self, x):
        return self.forward_propagation(x)[-1]
    
    def test(self, x, weights, biases):
        activations = [x]
        for i in range(self.num_layers - 1):
            if i == self.num_layers - 2:  # Last Layer
                activation = sigmoid(np.dot(activations[-1], weights[i]) + biases[i])
            else:
                activation = np.tanh(np.dot(activations[-1], weights[i]) + biases[i])
            activations.append(activation)
        return activations

# Example usage:
if __name__ == "__main__":
    # Define the network architecture and activation functions
    layer_sizes = [3, 10, 5, 1]  # Input layer, two hidden layers, output layer
    # Create the neural network
    nn = NeuralNetwork(layer_sizes, 1)

    # Generate some random data for training
    X = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])
    y = np.array([[0], [1], [1], [0], [1], [0], [0], [1]])

    # Train the network
    learning_rate = 0.1
    epochs = 10000
    nn.train(X, y, learning_rate, epochs)

    # Make predictions
    for input_data in X:
        prediction = nn.predict(input_data.reshape(1, -1))
        print(f"Input: {input_data}, Prediction: {prediction}")
