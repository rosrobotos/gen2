"""
I'm trying build genetic algorithm again....

"""

__version__ = 0.21
__author__ = 'github.com/rosrobots'

import genlib

GENOM_SIZE = 10
GENERATION_SIZE = 10
GENERATIONS_COUNT = 10
MUTATION_CHANCE = 0.1

if __name__ == '__main__':
    print('start \n')

    many_generations = genlib.create_many_generations(
                                                      number_of_generations=GENERATIONS_COUNT,
                                                      generation_size=GENERATION_SIZE,
                                                      gen_length=GENOM_SIZE
                                                     )
    genlib.many_generations_pyplot(many_generations)