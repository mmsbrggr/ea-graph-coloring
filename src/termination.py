import datetime


def terminate_after_generations(max_generations):
    def f(current_generation):
        return current_generation < max_generations

    return f


def terminate_after(max_generations, max_minutes):
    start_time = datetime.datetime.now()

    def f(current_generation):
        if current_generation < max_generations and \
                (datetime.datetime.now() - start_time).total_seconds() / 60 < max_minutes:
            return True
        return False
    return f
