def replace(fitness_func, population, children):
    sorted_population = sorted(population, key=lambda individual: fitness_func(individual))

    i = len(population) - 1
    for child in children:
        sorted_population[i] = child
        i -= 1

    return sorted_population
