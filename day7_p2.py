import sys

def solve(filename):
    # Read grid
    with open(filename) as f:
        grid = [list(line.rstrip("\n")) for line in f]

    R = len(grid)
    C = len(grid[0])

    # Find starting column 'S'
    start_col = None
    for c in range(C):
        if grid[0][c] == 'S':
            start_col = c
            break

    if start_col is None:
        print("Error: No S found in first row.")
        return

    # DP table: number of timelines reaching cell (r, c)
    dp = [[0] * C for _ in range(R)]
    dp[0][start_col] = 1  # one timeline starts at S

    for r in range(R - 1):  # process until second last row
        for c in range(C):
            if dp[r][c] == 0:
                continue

            cell = grid[r + 1][c]  # next row

            if cell == '.':
                dp[r + 1][c] += dp[r][c]

            elif cell == '^':
                # Split into two separate timelines
                if c - 1 >= 0:
                    dp[r + 1][c - 1] += dp[r][c]
                if c + 1 < C:
                    dp[r + 1][c + 1] += dp[r][c]

            else:
                # Any other character behaves like empty
                dp[r + 1][c] += dp[r][c]

    # Total timelines = all timelines that reached bottom row
    answer = sum(dp[R - 1])

    print(answer)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 solve_part2.py <input_file>")
        sys.exit(1)

    solve(sys.argv[1])
