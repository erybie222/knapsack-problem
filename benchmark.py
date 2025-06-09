import time
import csv
from generate import generate_random_instance
from dp_solver import dp_knapsack
from greedy_solver import greedy_knapsack

def measure_time(func, *args):
    start = time.perf_counter()
    result = func(*args)
    end = time.perf_counter()
    return result, end - start

def save_results_to_csv(filename, rows, header):
    with open(filename, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for row in rows:
            writer.writerow(row)

def run_scenario_A(n_values, capacity=10000):

    times_dp = []
    times_greedy = []
    errors = []

    for n in n_values:
        weights, values, cap = generate_random_instance(n, capacity)

        dp_val, t_dp = measure_time(dp_knapsack, weights, values, cap)
        g_val,  t_g  = measure_time(greedy_knapsack, weights, values, cap)

        err = (dp_val - g_val) / dp_val if dp_val > 0 else 0.0

        print(f"[A] n={n:6d}  DP={t_dp:.3f}s  G={t_g:.3f}s  err={(err*100):.2f}%")

        times_dp.append(t_dp)
        times_greedy.append(t_g)
        errors.append(err)

    return times_dp, times_greedy, errors

def run_scenario_B(b_values, n=5000):
    times_dp = []
    times_greedy = []
    errors = []

    for b in b_values:
        weights, values, cap = generate_random_instance(n, b)

        dp_val, t_dp = measure_time(dp_knapsack, weights, values, cap)
        g_val,  t_g  = measure_time(greedy_knapsack, weights, values, cap)

        err = (dp_val - g_val) / dp_val if dp_val > 0 else 0.0

        print(f"[B] b={b:6d}  DP={t_dp:.3f}s  G={t_g:.3f}s  err={(err*100):.2f}%")

        times_dp.append(t_dp)
        times_greedy.append(t_g)
        errors.append(err)

    return times_dp, times_greedy, errors