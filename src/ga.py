import copy
import random

import numpy as np

from src.fitness import number_bad_edges


def genetic_algorithm(graph,
                      initialization_func,
                      fitness_func,
                      termination_func,
                      selection_func,
                      recombine_func,
                      mutate_func,
                      replace_func,
                      local_search_func=None,
                      restart_after_step=True):

    best_solution = None
    is_solution = True
    population = []

    while is_solution:
        if not restart_after_step and population:
            # we don't now want to restart with a new fresh created population
            # but instead keep the current population
            for individual in population:
                for i in range(graph.number_vertices):
                    if individual.coloring[i] not in graph.colors:
                        # replace invalid (not anymore used) colors
                        individual.set_color(i, random.choice(graph.colors))
                individual.fitness = fitness_func(individual, population)
            # initialization_func shall return old, updated population
            initialization_func = lambda: population

        possible_solution, population = \
            genetic_algorithm_step(initialization_func,
                                   fitness_func,
                                   termination_func,
                                   selection_func,
                                   recombine_func,
                                   mutate_func,
                                   replace_func,
                                   local_search_func)
        is_solution = number_bad_edges(possible_solution) == 0
        if is_solution:
            best_solution = copy.deepcopy(possible_solution)
            graph.colors = range(1, np.unique(best_solution.coloring).size)
            print("Solution found for k =", np.unique(best_solution.coloring).size, "Restarting")

    return best_solution


def genetic_algorithm_step(initialization_func,
                           fitness_func,
                           termination_func,
                           selection_func,
                           recombine_func,
                           mutate_func,
                           replace_func,
                           local_search_func=None):
    t = 0
    population = initialization_func()
    best_individual = population[0]
    for individual in population:
        individual.fitness = fitness_func(individual, population)

    while termination_func(current_generation=t):
        t += 1

        reproducing_population = selection_func(population)
        assert len(reproducing_population) % 2 == 0

        children = []
        while reproducing_population:
            parent_1 = reproducing_population.pop()
            parent_2 = reproducing_population.pop()
            offspring = recombine_func(parent_1, parent_2)
            mutate_func(offspring)
            offspring.fitness = fitness_func(offspring, population)
            children.append(offspring)

        population = replace_func(population, children)

        # Debug info
        if t % 10 == 0:
            current_fitness = [i.fitness for i in population]
            current_fitness.sort()
            print('Generation', t, 'Colors', np.unique(best_individual.coloring).size, current_fitness)

        best_individual = min(population, key=lambda individual: individual.fitness)
        if number_bad_edges(best_individual) == 0:
            return best_individual, population

        # Try to improve the best individual a little bit
        if local_search_func:
            local_search_func(best_individual, fitness_func)

    return best_individual, population
