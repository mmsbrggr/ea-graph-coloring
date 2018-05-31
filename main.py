import os
import sys

from src.Parser import Parser
from src.fitness import fitness, fitness_only_bad_edges
from src.ga import genetic_algorithm, genetic_algorithm_2
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

    if argv[1]:
        # choose algorithm from command line
        solution = globals()[argv[1]](graph)
    else:
        solution = ga1(graph)

    print("Coloring:", solution.coloring)
    print("# Bad edges:", number_bad_edges(solution))
    print("# Colors:", number_colors(solution))


def ga1(graph):
    return genetic_algorithm(
        initialization_random(graph, 50),
        fitness,
        terminate_after_generations(1000),
        tournament_selection(tournament_size=3, selection_size=20),
        recombine_crossover,
        mutate,
        replace
    )


def ga2(graph):
    return genetic_algorithm_2(
        initialization_random(graph, 30),
        fitness_only_bad_edges,
        terminate_after_generations(1000),
        tournament_selection(tournament_size=4, selection_size=10),
        recombine_crossover,
        mutate_random_color(0.05),
        replace
    )


if __name__ == "__main__":
    main(sys.argv[1:])
