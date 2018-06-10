import random

import numpy as np


def local_search(neighbourhood_func,
                 choose_neighbour_func,
                 stopping_criteria_func):
    def f(initial_solution, fitness_func):
        iterations = 0
        best = initial_solution
        initial_score = best_score = initial_solution.fitness
        while stopping_criteria_func(iterations):
            #print('get neighbourhood')
            neighbours = neighbourhood_func(best)

            #print('pick candidate')
            candidate, candidate_score = choose_neighbour_func(best_score, neighbours, fitness_func)

            if candidate and candidate_score <= best_score:
                candidate.fitness = fitness_func(candidate)
                best = candidate
                best_score = candidate_score

            iterations += 1

        if best_score < initial_score:
            print('Local search found an improvement')
        return best

    return f


def next_improvement(best_score, neighbors, score_fun):
    """
    Returns the first neighbors which is better than the current solution
    """
    for neighbor in neighbors:
        score = score_fun(neighbor)
        if score < best_score:
            return neighbor, score
    return None, None


def one_colour_change_neighborhood(individual):
    """
    Neighborhood of solutions where the color of one vertex that has a
    conflict is changed to a random other color
    """
    graph = individual.graph
    color_adj = np.dot(graph.adj_matrix, individual.coloring_diagonal)
    bad_edges = [np.count_nonzero(color_adj[i] == individual.coloring[i]) for i in range(graph.number_vertices)]

    for i, vertex in enumerate(bad_edges):
        if bad_edges[i] == 0:
            continue

        color = random.choice(graph.colors)
        if color != individual.coloring[i]:
            original_color = individual.coloring[i]
            individual.set_color(i, color)
            yield individual
            individual.set_color(i, original_color)  # reverse changes


def terminate_after_steps(max_steps):
    def f(current_step):
        return current_step < max_steps

    return f
