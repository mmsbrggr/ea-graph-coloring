import numpy as np


class Graph:

    def __init__(self, number_vertices):
        self.number_vertices = number_vertices
        self.adj_matrix = np.zeros((number_vertices, number_vertices))

    def add_edge(self, vertex1, vertex2):
        self.adj_matrix[vertex1][vertex2] = 1
        self.adj_matrix[vertex2][vertex1] = 1

    def are_neighbors(self, vertex1, vertex2):
        return self.adj_matrix[vertex1, vertex2] == 1
