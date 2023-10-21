import numpy as np

class OjaPCA:
    def __init__(self, initial_rate, decreasing_rate, X_normalized):
        self.initial_rate = initial_rate
        self.decreasing_rate = decreasing_rate
        self.X_normalized = X_normalized
        self.W = np.random.rand(X_normalized.shape[1])

    def fit(self, epochs):
        for epoch in range(epochs):
            if self.decreasing_rate:
                learning_rate = self.initial_rate * np.exp(-self.initial_rate * epoch)
            else:
                learning_rate = self.initial_rate
            for x in self.X_normalized:
                y = x.dot(self.W)
                delta_W = learning_rate * y * (x - y * self.W)
                self.W += delta_W

    def get_first_principal_component(self):
        return self.W
