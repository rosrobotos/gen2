"""
functions for creating creatures and generations.

create_creture() return creature))))
create_generation return generation)))
"""

__version__ = 0.1
__author__ = 'Rosrobotos'

import pandas as pd
import random as rnd


def create_creture(gen_lengh=10, creature_name='one'):
    creature = pd.Series(data=[rnd.randint(0, 1) for i in range(gen_lengh)], name=creature_name)
    return creature


def create_generation(generation_size=50):
    generation = pd.DataFrame(data=[create_creture(creature_name=(str(i))+'n') for i in range(generation_size)])

    return generation
