def read_input(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    n = int(lines[0])
    weights = list(map(int, lines[1].split()))
    values  = list(map(int, lines[2].split()))
    capacity = int(lines[3])
    return n, weights, values, capacity

def build_dp_table(n, weights, values, capacity):
    dp = [[0]*(capacity+1) for _ in range(n+1)]
    for i in range(1, n+1):
        w_i, v_i = weights[i-1], values[i-1]
        for w in range(capacity+1):
            if w_i <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-w_i] + v_i)
            else:
                dp[i][w] = dp[i-1][w]
    return dp

def print_dp_table(dp):
    
    rows = len(dp)
    cols = len(dp[0])

    headers = ["i\\w"] + [str(w) for w in range(cols)]

    col_widths = []
    for j, h in enumerate(headers):
        max_w = len(h)
        for i in range(rows):
            cell = str(i) if j == 0 else str(dp[i][j-1])
            max_w = max(max_w, len(cell))
        col_widths.append(max_w)

    header_line = " | ".join(headers[j].rjust(col_widths[j]) for j in range(len(headers)))
    sep_line    = "-+-".join("-" * col_widths[j] for j in range(len(headers)))
    print(header_line)
    print(sep_line)

    for i in range(rows):
        row = [str(i)] + [str(dp[i][j]) for j in range(cols)]
        line = " | ".join(row[j].rjust(col_widths[j]) for j in range(len(headers)))
        print(line)

def main():
    n, weights, values, capacity = read_input("plecak.txt")
    dp = build_dp_table(n, weights, values, capacity)
    print_dp_table(dp)

if __name__ == "__main__":
    main()