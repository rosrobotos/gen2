"""
functions for creating creatures and generations.

create_creature() return creature (pandas Series)
create_generation return generation (pandas DataFrame)
"""

__version__ = 0.14
__author__ = 'github.com/rosrobotos'

import random
import random as rnd
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

pd.plotting.register_matplotlib_converters()


def create_creature(
                    gen_length=10,
                    creature_name='one'
                    ):
    creature = pd.Series(
                         data=[rnd.randint(0, 1) for i in range(gen_length)],
                         name=creature_name
                        )
    return creature


def create_generation(
                      generation_size=50,
                      gen_length=10
                     ):
    generation = pd.DataFrame(
                              data=[
                                    create_creature(
                                                    creature_name=(str(i + 1)) + 'th',
                                                    gen_length=gen_length
                                                   ) for i in range(generation_size)
                                   ]
                             )
    generation['quality'] = generation.sum(axis=1)
    return generation


def print_quality_count(generation):
    """ print quality values, and indexes for any of this values"""

    print(
          '\n',
          'count of any quality',
          generation.quality.value_counts(),
          '\n'
         )


def indexes_of_quality(generation):
    for i in generation.quality.unique():
        print(
              'quality = ', i, ': ',
              generation.loc[generation.quality == i, 'quality'].index.values,
              '\n',
              '__'
             )


def create_many_generations(
                            number_of_generations=10,
                            generation_size=50,
                            gen_length=10
                           ):
    list_of_dataframes = pd.Series(
                                    data=[
                                        create_generation(
                                                          generation_size=generation_size,
                                                          gen_length=gen_length
                                                         ) for i in range(number_of_generations)
                                         ],
                                    name='creature_name'
                                 )

    return list_of_dataframes


def one_generation_pyplot(generation):
    sns.barplot(
                x=generation.index,
                y=generation.sort_values('quality').quality
               )
    plt.show()


def many_generations_pyplot(list_of_generations):
    qualities = [sum(generation.quality) for generation in list_of_generations]
    sns.lineplot(data=qualities)
    plt.show()


def mutation(creature):
    point = random.randint(0, len(creature))
    creature[point] = int(not(creature[point].values))
    return creature


def almost_generation(generation):
    sample = generation.sample()
    sample = mutation(sample)

    updatedgenration = pd.DataFrame(columns=generation.columns)
    for creatureindex in generation.index:
        if creatureindex == sample.index:
            print(creatureindex, ' == ', sample.index)
            updatedgenration.loc[creatureindex] = sample
            #updatedgenration.append(sample)
        else:
            updatedgenration.loc[creatureindex] = generation.loc[creatureindex]


    return updatedgenration



