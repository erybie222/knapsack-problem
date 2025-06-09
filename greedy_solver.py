def greedy_knapsack(weights, values, capacity):
    n = len(weights)
    ratio = sorted(
        [(values[i] / weights[i], i) for i in range(n)],
        key=lambda x: x[0],
        reverse=True
    )
    total_w = total_v = 0
    for _, i in ratio:
        if total_w + weights[i] <= capacity:
            total_w += weights[i]
            total_v += values[i]
    return total_v