import configparser

import numpy
from matplotlib import pyplot as plt
from scipy import stats
from sklearn.decomposition import PCA

from oja_pca import OjaPCA
import pandas as pd
import numpy as np

if __name__ == "__main__":
    # Load or generate your dataset as matrix "X"
    entry = pd.read_csv("data/europe.csv").values
    countries = entry[:, 0]
    data = entry[:, 1:].astype(float)
    data = stats.zscore(data, axis=0)

    config = configparser.ConfigParser()
    config.read('../config.ini')
    eta = config.getfloat('Oja', 'eta')
    decreasing_eta = config.getboolean('Oja', 'decreasing_eta')
    epochs = config.getint('Oja', 'epochs')

    oja = OjaPCA(eta, decreasing_eta, data)
    oja.fit(epochs)
    fpc = oja.get_first_principal_component()
    print(fpc)

    pca = PCA()
    pca.fit(data)
    print("PC1 Vector:", pca.components_[0])

    print(numpy.linalg.norm(pca.components_[0] - fpc))

    # distances = []
    # epochs_axis = []
    # for i in range(10):
    #     oja.fit(epochs)
    #     fpc = oja.get_first_principal_component()
    #     print(fpc)
    #     distances.append(numpy.linalg.norm(pca.components_[0] - fpc))
    #     epochs_axis.append((i+1)*epochs)

    # plt.xlabel('Epocas')
    # plt.ylabel('Distancia')
    # plt.plot(epochs_axis, distances, color='red', linestyle='-')
    # plt.show()

    index = []
    for x in data:
        index.append(fpc.dot(x))

    combined_list = list(zip(countries, index))
    sorted_combined_list = sorted(combined_list, key=lambda d: -d[1])
    
    l1, l2 = zip(*sorted_combined_list)

    # print(sorted_combined_list)
    
    plt.figure(figsize=(15, 10))
    plt.bar(l1, l2)
    plt.xlabel('Countries')
    plt.ylabel('Values')
    plt.xticks(rotation=45)
    for i, value in enumerate(l2):
        if value > 0: 
            plt.text(i, value, str(f'{value:.2f}'), ha='center', va='bottom')
        else: 
            plt.text(i, value, str(f'{value:.2f}'), ha='center', va='top')
    plt.show()

    index = []
    for x in data:
        index.append(pca.components_[0].dot(x))

    combined_list = list(zip(countries, index))
    sorted_combined_list = sorted(combined_list, key=lambda d: -d[1])
    
    l1, l2 = zip(*sorted_combined_list)

    # print(sorted_combined_list)
    
    plt.figure(figsize=(15, 10))
    plt.bar(l1, l2)
    plt.xlabel('Countries')
    plt.ylabel('Values')
    plt.xticks(rotation=45)
    for i, value in enumerate(l2):
        if value > 0: 
            plt.text(i, value, str(f'{value:.2f}'), ha='center', va='bottom')
        else: 
            plt.text(i, value, str(f'{value:.2f}'), ha='center', va='top')
    plt.show()


