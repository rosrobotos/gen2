"""
I'm trying build genetic algorithm again....

"""

__version__ = 0.2
__author__ = 'github.com/rosrobotos'

import matplotlib.pyplot as plt
import seaborn as sns

import genlib

GENOM_SIZE = 10
GENERATION_SIZE = 50
GENERATIONS_COUNT = 50
MUTATION_CHANCE = 0.1

if __name__ == '__main__':
    print('start \n')
    print('create testing creature \n')

    test_creature = genlib.create_creature()
    print(test_creature)

    print('create test generation \n')
    test_generation = genlib.create_generation()
    print(test_generation)

    #   sns.barplot(x=test_generation.index, y=test_generation.sort_values('quality').quality)
    #   plt.show()

    print('\n')
    print(test_generation.sort_values('quality').iloc[-5:])
    print(test_generation.sort_values('quality').iloc[-5:].index)
    print(test_generation.quality.unique())
    for i in test_generation.quality.unique():
        print(test_generation.iloc[[test_generation.quality == i]])
        print('\n')
