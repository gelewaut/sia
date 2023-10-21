import numpy as np
import pandas as pd

class OjaPCA:
    def __init__(self, initial_rate=0.0001, max_iterations=1000, decreasing_rate=True):
        self.initial_rate = initial_rate
        self.max_iterations = max_iterations
        self.decreasing_rate = decreasing_rate
        self.X_means = None
        self.W = None
        self.X_normalized = None

    def fit(self, X):
        # Full normalization (centering and scaling)
        self.X_mean = np.mean(X, axis=0)
        self.X_std = np.std(X, axis=0)
        self.X_normalized = (X - self.X_mean) / self.X_std

        # Initialize the weight vector "W" with random values
        self.W = np.random.rand(X.shape[1])
        # Apply Oja's rule to find the first principal component
        for iteration in range(self.max_iterations):
            if self.decreasing_rate:
                learning_rate = self.initial_rate * np.exp(-self.initial_rate * iteration)
            else:
                learning_rate = self.initial_rate
            for x in self.X_normalized:
                y = x.dot(self.W)
                delta_W = learning_rate * y * (x - y * self.W)  # Update rule for Oja's rule
                self.W += delta_W

    def get_first_principal_component(self):
        return self.W


if __name__ == "__main__":
    # Example usage:
    # Create an instance of the OjaPCA class
    oja_pca = OjaPCA()

    # Load or generate your dataset as matrix "X"
    entry = pd.read_csv("data/europe.csv").values
    countries = entry[:, 0]
    data = entry[:, 1:].astype(float)
    X = np.array(data)

    # Fit the OjaPCA model to your data
    oja_pca.fit(X)

    # Get the first principal component
    first_principal_component = oja_pca.get_first_principal_component()

    print("First Principal Component (Vector W):", first_principal_component)