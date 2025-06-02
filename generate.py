import random

def generate_instance(n , b, max_weight=50, max_value=100):
    weights = [random.randint(1, max_weight) for _ in range(n)]
    values = [random.randint(1, max_weight) for _ in range(n)]
    return weights, values, b
    