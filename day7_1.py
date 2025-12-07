import sys
from collections import deque

def solve(filename):
    # Read input grid
    with open(filename) as f:
        grid = [list(line.rstrip("\n")) for line in f]

    rows = len(grid)
    cols = len(grid[0])

    # Locate 'S' in the top row
    start_col = None
    for c in range(cols):
        if grid[0][c] == 'S':
            start_col = c
            break

    if start_col is None:
        print("Error: No 'S' found in first row.")
        return

    # Queue for BFS of beams
    queue = deque()
    queue.append((0, start_col))

    # Track visited beams: (row, col)
    # Prevents processing same downward beam more than once
    visited = set()
    visited.add((0, start_col))

    split_count = 0

    while queue:
        r, c = queue.popleft()

        nr = r + 1
        if nr >= rows:
            continue  # exits manifold

        cell = grid[nr][c]

        # If beam arrives here for first time
        if (nr, c) not in visited:
            visited.add((nr, c))

            if cell == '.':
                queue.append((nr, c))

            elif cell == '^':
                split_count += 1

                # left beam
                if c - 1 >= 0 and (nr, c - 1) not in visited:
                    queue.append((nr, c - 1))

                # right beam
                if c + 1 < cols and (nr, c + 1) not in visited:
                    queue.append((nr, c + 1))

            else:
                # Treat any other char as empty
                queue.append((nr, c))

    print(split_count)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 solve.py <input_file>")
        sys.exit(1)

    solve(sys.argv[1])
