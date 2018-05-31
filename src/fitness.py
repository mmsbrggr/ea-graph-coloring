import numpy as np


def fitness(individual, population=None):
    return 2 * number_bad_edges(individual) + number_colors(individual)


def fitness_only_bad_edges(individual, population=None):
    return number_bad_edges(individual)


def number_bad_edges(individual):
    graph = individual.graph
    count = 0

    # Loop over diagonal matrix
    for vertex1 in range(graph.number_vertices):
        for vertex2 in range(vertex1 + 1, graph.number_vertices):
            if graph.are_neighbors(vertex1, vertex2)\
                    and individual.coloring[vertex1] == individual.coloring[vertex2]:
                count += 1

    return count


def number_colors(individual):
    return np.unique(individual.coloring).size
