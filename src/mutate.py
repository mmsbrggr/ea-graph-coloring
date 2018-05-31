import random

mutation_prob = 0.1


def mutate(individual):
    if random.random() < mutation_prob:
        index1 = random.randint(0, individual.coloring.size - 1)
        index2 = random.randint(0, individual.coloring.size - 1)
        tmp = individual.coloring[index1]
        individual.coloring[index1] = individual.coloring[index2]
        individual.coloring[index2] = tmp
