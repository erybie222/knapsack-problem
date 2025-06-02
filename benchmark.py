import time
import csv
import os
def measure_time(func , *args):
    start = time.perf_counter()
    result = func(*args)
    end = time.perf_counter()
    elapsed = end - start
    return result, elapsed

def save_results_to_csv(filename, results, header):
    file_exsists = os.path.isfile(filename)

    with open(filename, mode = 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)

        if not file_exsists:
            writer.writerow(header)
        for row in results:
            writer.writerow(row)

