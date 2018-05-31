import os
import sys

from src.Parser import Parser
from src.fitness import fitness
from src.ga import genetic_algorithm
from src.initialization import initialization_random
from src.mutate import mutate
from src.recombine import recombine_crossover
from src.replace import replace
from src.selection import tournament_selection
from src.termination import terminate_after_generations


def main(argv):
    file_name = argv[0]
    path = os.path.join(os.getcwd(), 'instances', file_name + '.col')
    graph = Parser().get_graph_from_file(path)

    solution = ga1(graph)

    print(solution.coloring)


def ga1(graph):
    return genetic_algorithm(
        initialization_random(graph, 10),
        fitness,
        terminate_after_generations(100),
        tournament_selection(tournament_size=3, selection_size=8),
        recombine_crossover,
        mutate,
        replace
    )


if __name__ == "__main__":
    main(sys.argv[1:])
