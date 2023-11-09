import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def int_to_bits_matrix(letter):
    letter_matrix = []
    for line in letter:
        bin_value = bin(line)[2:].zfill(8)  # Supprimez le 'b' indésirable
        letter_matrix.append(bin_value)
    matrix = np.array([[int(pixel) for pixel in row] for row in letter_matrix])
    return matrix

# Créer une fonction pour afficher une lettre
def create_letter_plot(letter, ax, cmap='Blues'):
    p = sns.heatmap(letter, ax=ax, annot=False, cbar=False, square=True, linewidth=2, linecolor='black', cmap=cmap)
    p.xaxis.set_visible(False)
    p.yaxis.set_visible(False)


def print_letter_7x8(letter, cmap='Blues'):
    fig, ax = plt.subplots(1, 1, figsize=(8, 7))
    fig.set_dpi(360)

    letter_matrix = int_to_bits_matrix(letter)
    create_letter_plot(letter_matrix, ax=ax, cmap=cmap)

    plt.show()

