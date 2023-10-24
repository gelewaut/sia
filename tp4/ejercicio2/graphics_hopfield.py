import numpy as np
import hopfield
import seaborn as sns
import matplotlib.pyplot as plt

def create_letter_plot(letter, ax, cmap='Blues'):
    p = sns.heatmap(letter, ax=ax, annot=False, cbar=False, square=True, linewidth=2, linecolor='black')
    p.xaxis.set_visible(False)
    p.yaxis.set_visible(False)
    return p

def print_letters_line(letters, cmap='Blues', cmaps=[]):
    fig, ax = plt.subplots(1,len(letters))
    fig.set_dpi(360)
    if not cmaps:
        cmaps = [cmap]*len(letters)
    if len(cmaps) != len(letters):
        raise Exception('cmap list should be the same length as letters')
    for i, subplot in enumerate(ax):
        create_letter_plot(letters[i].reshape(5,5), ax=subplot, cmap=cmaps[i])
    plt.show()

if __name__ == "__main__":
    A = [1,1,1,1,1,
        1,-1,-1,-1,1,
        1,1,1,1,1,
        1,-1,-1,-1,1,
        1,-1,-1,-1,1]
    
    L = [1,-1,-1,-1,-1,
        1,-1,-1,-1,-1,
        1,-1,-1,-1,-1,
        1,-1,-1,-1,-1,
        1,1,1,1,1]
    
    T = [1,1,1,1,1,
        -1,-1,1,-1,-1,
        -1,-1,1,-1,-1,
        -1,-1,1,-1,-1,
        -1,-1,1,-1,-1]
    
    V = [1,-1,-1,-1,1,
        1,-1,-1,-1,1,
        -1,1,-1,1,-1,
        -1,1,-1,1,-1,
        -1,-1,1,-1,-1]

    F = [1,1,1,1,1,
        1,-1,-1,-1,-1,
        1,1,1,1,-1,
        1,-1,-1,-1,-1,
        1,-1,-1,-1,-1]

    P = [1,1,1,1,1,
        1,-1,-1,-1,1,
        1,1,1,1,1,
        1,-1,-1,-1,-1,
        1,-1,-1,-1,-1]
    
    R = [1,1,1,1,1,
        1,-1,-1,-1,1,
        1,1,1,1,1,
        1,-1,-1,1,-1,
        1,-1,-1,-1,1]
          
    input = np.array(
        [1,1,1,1,1,
        1,-1,1,-1,1,
        1,1,1,1,1,
        1,-1,-1,-1,1,
        1,-1,-1,-1,1])
    
    n = 5
    hop = hopfield.Hopfield([A, L, T, V])
    # hop = hopfield.Hopfield([A, F, P, R])

    result = hop.algorithm(input, 30)
    output = result[len(result) - 1]

    for r in result:
        print(hop.get_energy(r))
    # fill with empty letters
    result += [np.ones((5,5))*-1] * (n - len(result)%n)
    # iterate as groups of n
    for letter_group in [result[i * n:(i + 1) * n] for i in range(len(result) // n )]:
        print_letters_line(letter_group)
    