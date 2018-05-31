import os
import sys

from src.Parser import Parser
from src.fitness import fitness, fitness_only_bad_edges
from src.ga import genetic_algorithm
from src.initialization import initialization_random
from src.mutate import mutate, mutate_random_color
from src.recombine import recombine_crossover
from src.replace import replace
from src.selection import tournament_selection
from src.termination import terminate_after_generations
from src.fitness import number_colors, number_bad_edges


def main(argv):
    file_name = argv[0]
    path = os.path.join(os.getcwd(), 'instances', file_name + '.col')
    graph = Parser().get_graph_from_file(path)

    if len(argv) >= 2:
        # choose algorithm from command line
        solution = globals()[argv[1]](graph)
    else:
        solution = ga1(graph)

    print("Coloring:", solution.coloring)
    print("# Bad edges:", number_bad_edges(solution))
    print("# Colors:", number_colors(solution))


def ga1(graph):
    return genetic_algorithm(
        graph,
        initialization_random(graph, 50),
        fitness,
        terminate_after_generations(10000),
        tournament_selection(tournament_size=2, selection_size=30),
        recombine_crossover,
        mutate_random_color(0.05),
        replace
    )


if __name__ == "__main__":
    main(sys.argv[1:])
