import numpy as np


class Individual:
    def __init__(self, graph):
        self.graph = graph
        self.coloring = np.zeros(graph.number_vertices)
        self.coloring_diagonal = np.zeros((graph.number_vertices, graph.number_vertices))
        self.fitness = None

    def set_color(self, i, color):
        self.coloring[i] = color
        self.coloring_diagonal[i][i] = color
