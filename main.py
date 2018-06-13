import os
import sys
from datetime import datetime

from src.local_search import local_search, next_improvement, \
    one_colour_change_neighborhood, terminate_after_steps
from src.Parser import Parser
from src.fitness import fitness, fitness_only_bad_edges
from src.ga import genetic_algorithm
from src.initialization import initialization_random
from src.mutate import mutate, mutate_random_color
from src.recombine import one_point_crossover
from src.replace import replace
from src.selection import tournament_selection
from src.termination import terminate_after_generations, terminate_after
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

    if solution:
        result_str = '\n\r'.join(['Coloring: %s' % solution.coloring,
                                  '# Bad edges: %s' % number_bad_edges(solution),
                                  '# Colors: %s' % number_colors(solution)])
    else:
        result_str = 'No solution found!'
    print(result_str)

    script_dir = os.path.dirname(__file__)
    directory = os.path.join(script_dir, 'results')
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(os.path.join(directory, '%s_%s.txt' % (file_name, datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))), 'w') as f:
        f.write(result_str)


def ga1(graph):
    return genetic_algorithm(
        graph,
        initialization_random(graph, 30),
        fitness,
        terminate_after_generations(10000),
        tournament_selection(tournament_size=2, selection_size=30),
        one_point_crossover,
        mutate,
        replace
    )


def ga2(graph):
    return genetic_algorithm(
        graph,
        initialization_random(graph, 50),
        fitness,
        terminate_after(max_generations=10000, max_minutes=30),
        tournament_selection(tournament_size=2, selection_size=16),
        one_point_crossover,
        mutate,
        replace,
        local_search(one_colour_change_neighborhood, next_improvement, terminate_after_steps(10)),
        restart_after_step=True
    )


if __name__ == "__main__":
    # run this program via commandline with:
    # py -3 main.py instance-name algorithm-name(optional)
    # e.g.: py -3 main.py queen5_5 ga2
    main(sys.argv[1:])
