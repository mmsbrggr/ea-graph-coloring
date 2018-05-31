def terminate_after_generations(max_generations):
    def f(current_generation):
        return current_generation < max_generations

    return f
