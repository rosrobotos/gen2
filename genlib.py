"""
functions for creating creatures and generations.

create_creature() return creature (pandas Series)
create_generation return generation (pandas DataFrame)
"""

__version__ = 0.11
__author__ = 'github.com/rosrobotos'

import pandas as pd
import random as rnd


def create_creature(gen_length=10, creature_name='one'):
    creature = pd.Series(
                        data=[
                             rnd.randint(0, 1) for i in range(gen_length)
                             ],
                        name=creature_name
                        )
    return creature


def create_generation(generation_size=50):
    generation = pd.DataFrame(
                              data=[
                                   create_creature(creature_name=(str(i + 1)) + 'th')
                                   for i in range(generation_size)
                                   ]
                             )
    generation['quality'] = generation.sum(axis=1)
    return generation
