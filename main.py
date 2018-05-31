import sys

from src.fitness import fitness
from src.ga import genetic_algorithm
from src.initialization import initialization_random
from src.mutate import mutate
from src.recombine import recombine
from src.replace import replace
from src.selection import tournament_selection
from src.termination import terminate_after_generations


def main(argv):
    instance = None  # TODO read from file
    solution = ga1(instance)
    # TODO print / write solution


def ga1(instance):
    return genetic_algorithm(
        initialization_random(instance, 10),
        fitness,
        terminate_after_generations(100),
        tournament_selection(tournament_size=3, selection_size=8),
        recombine,
        mutate,
        replace
    )


if __name__ == "__main__":
    main(sys.argv[1:])
