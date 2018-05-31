import random

import numpy as np

from src.fitness import number_bad_edges


def genetic_algorithm(initialization_func,
                      fitness_func,
                      termination_func,
                      selection_func,
                      recombine_func,
                      mutate_func,
                      replace_func):
    t = 0
    population = initialization_func()
    while termination_func(current_generation=t):
        t += 1

        reproducing_population = selection_func(fitness_func, population)
        assert len(reproducing_population) % 2 == 0

        children = []
        while reproducing_population:
            parent_1 = reproducing_population.pop()
            parent_2 = reproducing_population.pop()
            offspring = recombine_func(parent_1, parent_2)
            mutate_func(offspring)
            children.append(offspring)

        population = replace_func(fitness_func, population, children)

        # Debug info
        if t % 10 == 0:
            current_fitness = [fitness_func(i, population) for i in population]
            current_fitness.sort()
            print('Generation', t, current_fitness)

    best_individual = min(population, key=lambda individual: fitness_func(individual, population))

    return best_individual


def genetic_algorithm_2(initialization_func,
                        fitness_func,
                        termination_func,
                        selection_func,
                        recombine_func,
                        mutate_func,
                        replace_func):
    t = 0
    population = initialization_func()
    best_individual = population[0]
    while termination_func(current_generation=t):
        t += 1

        reproducing_population = selection_func(fitness_func, population)
        assert len(reproducing_population) % 2 == 0

        children = []
        while reproducing_population:
            parent_1 = reproducing_population.pop()
            parent_2 = reproducing_population.pop()
            offspring = recombine_func(parent_1, parent_2)
            mutate_func(offspring)
            children.append(offspring)

        population = replace_func(fitness_func, population, children)

        # Debug info
        if t % 10 == 0:
            current_fitness = [fitness_func(i, population) for i in population]
            current_fitness.sort()
            print('Generation', t, 'Colors', np.unique(best_individual.coloring).size, current_fitness)

        # check if we found a new best indivdual with less colours and no conflicts
        new_best = False
        min_colors = np.unique(best_individual.coloring).size
        for individual in population:
            if np.unique(individual.coloring).size < min_colors and number_bad_edges(individual) == 0:
                best_individual = individual
                min_colors = np.unique(best_individual.coloring).size
                new_best = True

        # force the whole population to use only colours of the new best individual
        if new_best:
            graph = best_individual.graph
            # set new colors
            graph.colors = np.unique(best_individual.coloring)
            # force new colors for all individuals
            for individual in population:
                for i in range(individual.coloring.size):
                    if individual.coloring[i] not in graph.colors:
                        individual.coloring[i] = random.choice(graph.colors)

    return best_individual
