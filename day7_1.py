def solve():
    # Read the input grid
    with open("input.txt") as f:
        grid = [list(line.rstrip("\n")) for line in f]

    rows = len(grid)
    cols = len(grid[0])

    # Find S (starting position)
    start_col = None
    for c in range(cols):
        if grid[0][c] == 'S':
            start_col = c
            break

    if start_col is None:
        raise ValueError("No starting point 'S' found in the top row.")

    # Active beams stored as list of (row, col)
    beams = [(0, start_col)]

    split_count = 0

    # Process beams until all are done
    while beams:
        new_beams = []

        for r, c in beams:
            nr = r + 1  # move downward

            # Beam leaves manifold
            if nr >= rows:
                continue

            cell = grid[nr][c]

            if cell == '.':
                # Continue downward
                new_beams.append((nr, c))

            elif cell == '^':
                # Split event
                split_count += 1
                # Left beam
                if c - 1 >= 0:
                    new_beams.append((nr, c - 1))
                # Right beam
                if c + 1 < cols:
                    new_beams.append((nr, c + 1))

            else:
                # Any other char treated as empty
                new_beams.append((nr, c))

        beams = new_beams

    print(split_count)


if __name__ == "__main__":
    solve()
