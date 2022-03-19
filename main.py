"""
I'm trying build genetic algorithm again....

"""

__version__ = 0.21
__author__ = 'github.com/rosrobots'

import matplotlib.pyplot as plt
import pandas as pd
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

    genlib.describe_generation(test_generation)
