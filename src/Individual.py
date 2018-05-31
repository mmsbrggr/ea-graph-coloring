class Individual(object):
    def __init__(self, graph):
        self.graph = graph
        self.coloring = [x for x in range(graph.number_vertices)]
