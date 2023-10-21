from oja_pca import OjaPCA
import pandas as pd
import numpy as np

if __name__ == "__main__":
    # Load or generate your dataset as matrix "X"
    entry = pd.read_csv("data/europe.csv").values
    countries = entry[:, 0]
    data = entry[:, 1:].astype(float)
    X = np.array(data)

    learning_rates = [0.1, 0.01, 0.001]
    iterations = [1000, 10000, 50000]
    results = []
    for learning_rate in learning_rates:
        for iteration in iterations:
            oja_pca = OjaPCA(learning_rate, iteration, True)
            oja_pca.fit(X)
            first_principal_component = oja_pca.get_first_principal_component()
            results.append([learning_rate, iteration, True, first_principal_component])
            print(first_principal_component)
            oja_pca = OjaPCA(learning_rate, iteration, False)
            oja_pca.fit(X)
            first_principal_component = oja_pca.get_first_principal_component()
            results.append([learning_rate, iteration, False, first_principal_component])
            print(first_principal_component)