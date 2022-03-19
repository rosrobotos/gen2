"""
functions for creating creatures and generations.

create_creature() return creature (pandas Series)
create_generation return generation (pandas DataFrame)
"""

__version__ = 0.12
__author__ = 'github.com/rosrobotos'

import pandas as pd
import random as rnd

pd.plotting.register_matplotlib_converters()


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


def describe_generation(generation):
    """ print quality values, and indexes for any of this values"""

    print('\n count of any quality')
    print(generation.quality.value_counts())

    for i in generation.quality.unique():
        print(' quality = ', i, end=': ')
        print(generation.loc[generation.quality == i, 'quality'].index.values)
        print('__')
