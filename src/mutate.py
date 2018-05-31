import random

mutation_prob = 0.1


def mutate(individual):
    if random.random() < mutation_prob:
        index1 = random.randint(0, individual.coloring.size - 1)
        index2 = random.randint(0, individual.coloring.size - 1)
        tmp = individual.coloring[index1]
        individual.coloring[index1] = individual.coloring[index2]
        individual.coloring[index2] = tmp


def mutate_random_color(probability):
    def f(individual):
        for i in range(individual.coloring.size):
            if random.random() <= probability:
                individual.coloring[i] = random.choice(individual.graph.colors)

    return f
