import random

mutation_rate = 0.15


def mutate(individual):
    for i in range(int(individual.coloring.size / 20)):
        index1 = random.randint(0, individual.coloring.size - 1)
        index2 = random.randint(0, individual.coloring.size - 1)
        tmp = individual.coloring[index1]
        individual.set_color(index1, individual.coloring[index2])
        individual.set_color(index2, tmp)


def mutate_random_color(probability):
    def f(individual):
        for i in range(individual.coloring.size):
            if random.random() <= probability:
                individual.set_color(i, random.choice(individual.graph.colors))

    return f
