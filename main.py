"""
I'm trying build genetic algorithm again....

"""

__version__ = 0.2
__author__ = 'github.com/rosrobotos'

import matplotlib.pyplot as plt

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


plt.plot(test_generation.index, test_generation.quality)
plt.show()