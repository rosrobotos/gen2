"""
I'm trying build genetic algorithm again....

"""

__version__ = 0.1
__author__ = 'Rosrobotos'

# import nympy.matplotlib as mpl
# import pygame
# import deep
import pandas as pd
import numpy as np

import genlib

GENOM_SIZE = 10
GENERATION_SIZE = 50
GENERATIONS_COUNT = 50
MUTATION_CHANCE = 0.1

if __name__ == '__main__':
    print('start \n')
    print('create testing creature \n')

    test_creatre = genlib.create_creture()
    print(test_creatre)

    print('create test generation \n')
    test_generation = genlib.create_generation()
    print(test_generation)
    print(test_generation.describe())

# test_generation['Summury'] = test_generation.apply(lambda x: sum(x), axis=0)
# test_generation = test_generation.assign(Summury = lambda x: (sum(x)))
# print(test_generation)

# test_generation.columns.append()

# test_generation.iloc[i].sum()

#test_generation['summury'] = np.where(test_generation.sum())
print(test_generation.sum(axis=1))