from benchmark import run_scenario_A, run_scenario_B, measure_time, save_results_to_csv
from plots    import plot_scenario_A_from_csv, plot_scenario_B_from_csv

def main():
    capacity_A = 10000
    n_values   = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000, 70000, 75000]
    dp_A, g_A, err_A = run_scenario_A(n_values, capacity=capacity_A)

    rows_A = [[n, t_dp, t_g, err] for n, t_dp, t_g, err in zip(n_values, dp_A, g_A, err_A)]
    save_results_to_csv('results_A.csv', rows_A,
                        ['n', 'dp_time_s', 'greedy_time_s', 'relative_error'])
    plot_scenario_A_from_csv('results_A.csv')

    n_B      = 5000
    b_values = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000, 70000, 75000]
    dp_B, g_B, err_B = run_scenario_B(b_values, n=n_B)

    rows_B = [[b, t_dp, t_g, err] for b, t_dp, t_g, err in zip(b_values, dp_B, g_B, err_B)]
    save_results_to_csv('results_B.csv', rows_B,
                        ['capacity_b', 'dp_time_s', 'greedy_time_s', 'relative_error'])
    plot_scenario_B_from_csv('results_B.csv')

if __name__ == "__main__":
    main()