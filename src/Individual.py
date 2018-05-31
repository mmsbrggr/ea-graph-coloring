import numpy as np


class Individual:
    def __init__(self, graph):
        self.graph = graph
        self.coloring = np.zeros(graph.number_vertices)
        self.fitness = None
