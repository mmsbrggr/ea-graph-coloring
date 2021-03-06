import random


def tournament_selection(tournament_size, selection_size):
    """
    Selects tournament_size number of random individuals for a tournament and
    the best individual is the winner. Returns selection_size numbers of
    winners.

    Note that it is possible that one individual is chosen more than once for
    the same tournament and that selected_individuals can contain the same
    individual more than once.
    """

    def f(population):
        selected_individuals = []
        for i in range(selection_size):
            tournament_leader = random.choice(population)
            if random.random() < 0.9:
                for j in range(tournament_size):
                    individual = random.choice(population)
                    if individual.fitness < \
                       tournament_leader.fitness:
                        tournament_leader = individual

            selected_individuals.append(tournament_leader)

        return selected_individuals

    return f
