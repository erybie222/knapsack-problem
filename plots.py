
import csv
import matplotlib.pyplot as plt


def plot_scenario_A_from_csv(csv_file):
    n_values, dp_times, greedy_times, errors = [], [], [], []
    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            n_values.append(int(row['n']))
            dp_times.append(float(row['dp_time_s']))
            greedy_times.append(float(row['greedy_time_s']))
            errors.append(float(row['relative_error']))

    plt.figure(figsize=(8, 6))
    plt.plot(n_values, dp_times, '-', label='Algorytm programowania dynamicznego')
    plt.xlabel('Liczba kontenerów n')
    plt.ylabel('Czas wykonania (s)')
    plt.title('Czasy wykonania:')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('wykres1_dp.png')
    plt.close()

    plt.figure(figsize=(8, 6))
    plt.plot(n_values, greedy_times, '-', label='Algorytm zachłanny')
    plt.xlabel('Liczba kontenerów n')
    plt.ylabel('Czas wykonania (s)')
    plt.title('Czasy wykonania:')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('wykres1_greedy.png')
    plt.close()

    plt.figure(figsize=(8, 6))
    plt.bar([str(n) for n in n_values], [e*100 for e in errors], color='skyblue')
    plt.xlabel('Liczba kontenerów n')
    plt.ylabel('Błąd względny (%)')
    plt.title('Błąd względny algorytmu zachłannego:')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.savefig('wykres2.png')
    plt.close()


def plot_scenario_B_from_csv(csv_file):
    b_values, dp_times, greedy_times, errors = [], [], [], []
    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            b_values.append(int(row['capacity_b']))
            dp_times.append(float(row['dp_time_s']))
            greedy_times.append(float(row['greedy_time_s']))
            errors.append(float(row['relative_error']))

    plt.figure(figsize=(8, 6))
    plt.plot(b_values, dp_times,    '-', label='Algorytm programowania dynamicznego')
    plt.xlabel('Pojemność statku b')
    plt.ylabel('Czas wykonania (s)')
    plt.title('Czasy wykonania:')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('wykres3_dp.png')
    plt.close()

    plt.figure(figsize=(8, 6))
    plt.plot(b_values, greedy_times, '-', label='Algorytm zachłanny')
    plt.xlabel('Pojemność statku b')
    plt.ylabel('Czas wykonania (s)')
    plt.title('Czasy wykonania:')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('wykres3_greedy.png')
    plt.close()

    plt.figure(figsize=(8, 6))
    plt.bar([str(b) for b in b_values], [e*100 for e in errors], color='skyblue')
    plt.xlabel('Pojemność statku b')
    plt.ylabel('Błąd względny (%)')
    plt.title('Błąd względny algorytmu zachłannego:')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.savefig('wykres4.png')
    plt.close()