import random

from src.Individual import Individual


def recombine_crossover(parent_1, parent_2):
    individual = Individual(parent_1.graph)
    for i in range(individual.graph.number_vertices):
        if random.random() <= 0.5:
            individual.coloring[i] = parent_1.coloring[i]
        else:
            individual.coloring[i] = parent_2.coloring[i]
    return individual
