from generate import generate_instance
from dp_solver import knapsack_dp
from greedy_solver import knapsack_greedy
from benchmark import measure_time, save_results_to_csv

n = 50
b= 200

weights, values, capacity = generate_instance(n, b)

(dp_result, dp_selected), dp_time = measure_time(knapsack_dp(weights, values, capacity))
(greedy_result, greedy_selected), greedy_time = measure_time(knapsack_greedy(weights, values, capacity))

relative_error = (dp_result - greedy_result) / dp_result if dp_result != 0 else 0


row = [
    n,
    b,
    dp_result,
    dp_time,
    greedy_result,
    greedy_time,
    relative_error
]

save_results_to_csv(
    "results_DP_vs_Greedy.csv",
    [row],
    header=["n", "b", "DP_value", "DP_time", "Greedy_value", "Greedy_time", "relative_error"]
)

