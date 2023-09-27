import numpy as np
import sys

# Activation function
def step_function(x):
    return 1 if x >= 0 else -1

# Error function
def error_function(calculated, targets):
    squared_diff = (calculated - targets) ** 2
    return squared_diff.mean()  # Average squared error

# Perceptron training function
def train_perceptron(inputs, targets, learning_rate, limit, epsilon):
    inputs_with_bias = np.insert(inputs, 0, 1, axis=1)
    
    num_samples, num_features = inputs.shape
    w = np.random.rand(num_features+1)
    min_error = sys.maxsize
    w_min = None
    epochs = 0
    
    while epochs < limit and min_error > epsilon:
        mu = np.random.randint(num_samples)  # Random integer between 0 and p-1
        exitement = np.dot(inputs_with_bias[mu], w)
        activation = step_function(exitement)
        delta_w = learning_rate * (targets[mu] - activation) * inputs_with_bias[mu]
        w += delta_w
        calculated = np.dot(inputs_with_bias, w)
        error = error_function(calculated, targets)
        if error < min_error:
            min_error = error
            w_min = np.copy(w)
        epochs += 1
    return w_min

def main():
    # Input data and classification targets for the OR function
    inputs = np.array([[-1, 1], [1, -1], [-1, -1], [1, 1]])
    targets1 = np.array([-1, -1, -1, 1])
    targets2 = np.array([1, 1, -1, -1])
    test_inputs = np.array([[1, 1], [-1, -1], [-1, 1], [1, -1]])
    
    # Hyperparameters
    learning_rate = 0.1
    limit = 1000
    epsilon = 0.01

    # Train the perceptron for the AND operator
    final_weights1 = train_perceptron(inputs, targets1, learning_rate, limit, epsilon)
    
    # Train the perceptron for the XOR operator
    final_weights2 = train_perceptron(inputs, targets2, learning_rate, limit, epsilon)

    # Test the perceptrons
    print("For AND operator:")
    for i in range(len(test_inputs)):
        weighted_sum1 = np.dot(test_inputs[i], final_weights1[1:]) + final_weights1[0]
        prediction1 = step_function(weighted_sum1)
        print(f"Input: {test_inputs[i]}, Predicted Class: {prediction1}")
    print(final_weights1)
        
    print("\nFor XOR operator:")
    for i in range(len(test_inputs)):
        weighted_sum2 = np.dot(test_inputs[i], final_weights2[1:]) + final_weights2[0]
        prediction2 = step_function(weighted_sum2)
        print(f"Input: {test_inputs[i]}, Predicted Class: {prediction2}")
    print(final_weights2)
    
if __name__ == "__main__":
    main()
