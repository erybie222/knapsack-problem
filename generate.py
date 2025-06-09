import random

def generate_random_instance(n, capacity, max_weight=1000, max_value=1000):
    weights = [random.randint(1, max_weight) for _ in range(n)]
    values  = [random.randint(1, max_value)  for _ in range(n)]
    return weights, values, capacity