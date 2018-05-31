import random

from src.Individual import Individual


def initialization_random(graph, population_size):
    def f():
        population = []
        for i in range(population_size):
            individual = Individual(graph)
            for j in range(graph.number_vertices):
                individual.coloring[j] = random.choice(graph.colors)
            population.append(individual)
        return population

    return f
