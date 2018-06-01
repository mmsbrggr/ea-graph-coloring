import random

from src.Individual import Individual


def one_point_crossover(parent_1, parent_2):
    individual = Individual(parent_1.graph)
    rand_point = random.randint(0, individual.graph.number_vertices - 1)
    active = parent_1
    for i in range(individual.graph.number_vertices):
        if i == rand_point:
            active = parent_2
        individual.coloring[i] = active.coloring[i]
    return individual


def random_crossover(parent_1, parent_2):
    individual = Individual(parent_1.graph)
    for i in range(individual.graph.number_vertices):
        if random.random() <= 0.5:
            individual.coloring[i] = parent_1.coloring[i]
        else:
            individual.coloring[i] = parent_2.coloring[i]
    return individual
