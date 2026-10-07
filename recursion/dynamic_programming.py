"""Replacement exercise template based on the assignment screenshot.

This is not the original teacher-provided file. This template uses
(row, column) coordinates, with (0, 0) at the top-left of the grid.
Run with: python3 dynamic_programming.py
"""


grid = [
    [".", ".", "."],
    [".", "#", "."],
    [".", ".", "."],
]

# Store route counts per location here. Clear this cache when grid changes.
route_counts = {}


def count_routes(current_location):
    """Return the number of routes from current_location to the top-right.

    Arguments:
        current_location {tuple[int, int]} -- The (row, column) to start at.

    Use the global grid, a non-empty rectangular list of rows:
        '.' is an accessible cell.
        '#' is a blocked cell that you cannot enter.

    Rows are numbered from top to bottom; columns from left to right.
    From (row, column), you may move only:
        Up:    (row - 1, column)
        Right: (row, column + 1)

    The destination is (0, len(grid[0]) - 1).
    The bottom-left starting location is (len(grid) - 1, 0).

    Return 0 for a blocked location or a location outside the grid.
    Return 1 when already at the destination, provided it is accessible.
    Otherwise, the route count is the sum of the counts from the neighbor
    above and the neighbor to the right.

    Use recursion and dynamic programming: store calculated route counts
    in route_counts and reuse them instead of recalculating subproblems.
    Do not use functools.cache or functools.lru_cache for this exercise.
    The caller clears route_counts whenever the grid changes.

    Return the result as an integer.

    Examples (starting at the bottom-left):
        [["#", "."], [".", "."]] -> 1
        [[".", ".", "."], [".", "#", "."], [".", ".", "."]] -> 2
    """
    row = current_location[0]
    column = current_location[1]

    if row < 0 or row >= len(grid):
        return 0

    if column < 0 or column >= len(grid[0]):
        return 0

    if grid[row][column] == '#':
        return 0

    if current_location == (0, len(grid[0]) - 1):
        return 1

    if current_location in route_counts:
        return route_counts[current_location]

    up = count_routes((row - 1, column))
    right = count_routes((row, column + 1))

    result = up + right

    route_counts[current_location] = result

    return result


if __name__ == "__main__":
    examples = [
        (
            [
                ["#", "."],
                [".", "."],
            ],
            1,
        ),
        (
            [
                [".", ".", "."],
                [".", "#", "."],
                [".", ".", "."],
            ],
            2,
        ),
    ]

    for grid, expected in examples:
        route_counts.clear()
        start = (len(grid) - 1, 0)
        result = count_routes(start)

        for row in grid:
            print(" ".join(row))
        print(f"Routes from {start} to the top-right: {result}")
        print(f"Expected: {expected}")
        if result is None:
            print("TODO: implement count_routes.")
        else:
            print(f"Matches expected: {result == expected}")
        print()
