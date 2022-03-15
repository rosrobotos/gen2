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
    print(test_generation.sort_values('quality', ascending=False))

