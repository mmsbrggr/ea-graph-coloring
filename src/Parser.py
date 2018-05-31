from src.Graph import Graph

preamble_symbol = "p"
edge_symbol = "e"


class Parser:

    @staticmethod
    def get_graph_from_file(file_name):
        graph = None
        with open(file_name) as file:
            lines = file.readlines()
            for line in lines:
                words = line.split()
                if words[0] is preamble_symbol:
                    graph = Graph(int(words[2]))
                elif words[0] is edge_symbol:
                    graph.add_edge(int(words[1]) - 1, int(words[2]) - 1)

        return graph
