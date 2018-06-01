import numpy as np


class Graph:

    def __init__(self, number_vertices):
        self.number_vertices = number_vertices
        self.adj_matrix = np.zeros((number_vertices, number_vertices))
        self.max_degree = None
        self.colors = None

    def add_edge(self, vertex1, vertex2):
        self.adj_matrix[vertex1][vertex2] = 1
        self.adj_matrix[vertex2][vertex1] = 1

    def are_neighbors(self, vertex1, vertex2):
        return self.adj_matrix[vertex1, vertex2] == 1

    def make_triangular(self):
        self.adj_matrix = np.triu(self.adj_matrix)

    def set_max_degree(self):
        self.max_degree = int(np.max(np.sum(self.adj_matrix, axis=1)))

    def set_colors(self):
        number_colors = min(self.number_vertices, self.max_degree)
        self.colors = range(1, number_colors + 1)
