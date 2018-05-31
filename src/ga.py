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
                      replace_func):

    best_solution = None
    is_solution = True

    while is_solution:
        possible_solution = genetic_algorithm_step(initialization_func,
                                                    fitness_func,
                                                    termination_func,
                                                    selection_func,
                                                    recombine_func,
                                                    mutate_func,
                                                    replace_func)
        is_solution = number_bad_edges(possible_solution) == 0
        if is_solution:
            best_solution = possible_solution
            graph.colors = range(1, np.unique(best_solution.coloring).size)
            print("Solution found for k =", np.unique(best_solution.coloring).size, "Restarting")

    return best_solution


def genetic_algorithm_step(initialization_func,
                        fitness_func,
                        termination_func,
                        selection_func,
                        recombine_func,
                        mutate_func,
                        replace_func):
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
            return best_individual

    return best_individual
