import random


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
            children += mutate_func(offspring)

        replace_func(fitness_func, population, children)

        # Debug info
        current = [i.fitness for i in population]
        current.sort()
        print('Generation', t, current)

    best_individual = population[0]
    for individual in population[1:]:
        if fitness_func(population, individual) > \
                fitness_func(population, best_individual):
            best_individual = individual

    return best_individual
