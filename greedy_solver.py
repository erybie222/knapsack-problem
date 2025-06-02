def knapsack_greedy(weights, values, capacity):
    n = len(weights)
    ratio = [(values[i]/ weights[i], i) for i in range(n)]
    ratio.sort(reverse=True)

    total_value = 0
    total_weight = 0
    selected = []

    for r, i in ratio:
        if total_weight + weights[i] <= capacity:
            selected.append(i)
            total_weight += weights[i]
            total_value += values[i]

    return total_value, selected