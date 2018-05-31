

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
