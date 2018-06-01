import numpy as np


def fitness(individual, population=None):
    return 2 * number_bad_edges(individual) + number_colors(individual)


def fitness_only_bad_edges(individual, population=None):
    return number_bad_edges(individual)


def number_bad_edges(individual):
    graph = individual.graph
    color_adj = np.dot(graph.adj_matrix, individual.coloring_diagonal)
    bad_edges = [np.count_nonzero(color_adj[i] == individual.coloring[i]) for i in range(graph.number_vertices)]

    return np.sum(bad_edges)


def number_colors(individual):
    return np.unique(individual.coloring).size
