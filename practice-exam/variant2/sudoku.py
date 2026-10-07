import heapq

SUDOKU = [
    [0, 0, 0, 0, 5, 0, 0, 0, 7],
    [0, 0, 0, 0, 0, 0, 0, 4, 0],
    [3, 0, 4, 0, 0, 5, 2, 0, 0],
    [7, 2, 0, 0, 0, 1, 0, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 6, 0, 4, 0, 0, 0, 9, 2],
    [0, 0, 9, 8, 0, 0, 7, 0, 5],
    [0, 3, 0, 0, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 0],
]

sudoku_connections = [
    "aaa-aAb-bbB",
    "aac-caa-bBb",
    "CcC-ddE-Ebb",
    "           ",
    "CCd-ddE-fFf",
    "ccd-eee-fgg",
    "dDd-Eff-fGG",
    "           ",
    "hhE-Eff-GgG",
    "hHh-iig-gii",
    "Hhh-hIi-iii",
]

SIZE = 9
SC_SIZE = 11


def valid_horizontal(value, sudoku, row):
    """
    Given an sudoku and a row from 0 to 8
    It will return if the value is not already in this vertical part of the sudoku
    Time complexity: O(n)
    n: number of items in sudoku[row]
    """
    return value not in sudoku[row]


def valid_vertical(value, sudoku, column):
    """
    Given an sudoku and a column from 0 to 8
    It will return if the value is not already in this vertical part of the sudoku
    Time complexity: O(n)
    n: number of columns in Sudoku row
    """
    for n in range(SIZE):
        if sudoku[n][column] == value:
            return False
    return True


def print_sudoku(sudoku):
    """
    This prints the sudoku for debug purposes
    Time complexity: O(n)
    n: number of rows in Sudoku
    """
    for i in range(SIZE):
        print(sudoku[i])
    print()


# OBJECTIVE 1
def valid_blob(value, position, sudoku, connections):
    """
    Given a value and a position in the sudoku/connections
    It returns if a value is not already in this blob
    Time complexity: O(b)
    b: items in blob
    """
    start_x, start_y = position
    
    start_conn_x = start_x // 3 + start_x
    start_conn_y = start_y // 3 + start_y

    blob_indicator = connections[start_conn_y][start_conn_x].lower()

    visited = set()
    positions = [position]

    while positions:
        position = positions.pop()

        if position in visited:
            continue
        
        visited.add(position)
        
        x, y = position

        if sudoku[y][x] == value:
            return False

        # check top
        if y - 1 >= 0:
            new_y = y - 1

            conn_x = x // 3 + x
            conn_y = new_y // 3 + new_y
            
            if connections[conn_y][conn_x].lower() == blob_indicator:
                positions.append((x, new_y))

        # check right
        if x + 1 < SIZE:
            new_x = x + 1

            conn_x = new_x // 3 + new_x
            conn_y = y // 3 + y

            if connections[conn_y][conn_x].lower() == blob_indicator:
                positions.append((new_x, y))

        # check bottom
        if y + 1 < SIZE:
            new_y = y + 1

            conn_x = x // 3 + x
            conn_y = new_y // 3 + new_y

            if connections[conn_y][conn_x].lower() == blob_indicator:
                positions.append((x, new_y))
        
        # check left
        if x - 1 >= 0:
            new_x = x - 1
            
            conn_x = new_x // 3 + new_x
            conn_y = y // 3 + y

            if connections[conn_y][conn_x].lower() == blob_indicator:
                positions.append((new_x, y))

    return True


# OBJECTIVE 2
def valid_sudoku(sudoku, connections):
    """
    Returns True when all currently filled cells obey the Sudoku rules.
    """
    for y in range(SIZE):
        for x in range(SIZE):
            value = sudoku[y][x]

            # Empty cells don't need validation
            if value == 0:
                continue

            # Temporarily remove the value so it doesn't conflict with itself
            sudoku[y][x] = 0

            valid = (
                valid_horizontal(value, sudoku, y)
                and valid_vertical(value, sudoku, x)
                and valid_blob(value, (x, y), sudoku, connections)
            )

            # Always restore the original value
            sudoku[y][x] = value

            if not valid:
                return False

    return True


def solve_recursive(sudoku, connections):
    """Recursively solve the Sudoku i-place using backtracking."""
    for y in range(SIZE):
        for x in range(SIZE):

            # Skip filled cells
            if sudoku[y][x] != 0:
                continue

            # We found the first empty cell
            # Try every possible value
            for value in range(1, 10):

                if not valid_horizontal(value, sudoku, y):
                    continue
                
                if not valid_vertical(value, sudoku, x):
                    continue
                
                if not valid_blob(value, (x, y), sudoku, connections):
                    continue

                # Try this value
                sudoku[y][x] = value

                # Can the rest of the Sudoku be solved from here?
                if solve_recursive(sudoku, connections):
                    return True

                # No -> undo our choice
                sudoku[y][x] = 0

            # We tried 1 through 9 for this empty cell.
            # Nothing worked, so an earlier choice must have been wrong.
            return False

    # We went through the whole board without finding a zero
    # The Sudoku is solved.
    return sudoku


def solve(sudoku, connections):
    """
    Args:
        sudoku: a 2d array that contain all the numbers in the sudoku,
        connections: a string that represents how the blobs are connected
    
    Returns
        A solved sudoku as a 2d array or a string with the text "No solution"
    """
    if not valid_sudoku(sudoku, connections):
        return "No solution"

    if solve_recursive(sudoku, connections):
        return sudoku

    return "No solution"


# OBJECTIVE 3
def add_neighbor(solved_sudoku, costs, previous, neighbors, current_cost, current_position, neighbor_x, neighbor_y):
    neighbor_position = (neighbor_x, neighbor_y)
    neighbor_cost = solved_sudoku[neighbor_y][neighbor_x]
    new_cost = current_cost + neighbor_cost

    if new_cost < costs.get(neighbor_position, float("inf")):
        costs[neighbor_position] = new_cost
        previous[neighbor_position] = current_position
        heapq.heappush(neighbors, (new_cost, neighbor_position))


def minimal_line(solved_sudoku):
    """
    Args:
        solved_sudoku: a 2d array that contains a solved sudoku
    
    Returns:
        values: the values that sum to the minimal line
    """
    paths: dict[int, list[int]] = {}

    for y in range(SIZE):
        x = 0
        start_position = (x, y)
        cost = solved_sudoku[y][x]

        costs = {start_position: cost}

        previous = {start_position: None}

        neighbors = []
        heapq.heappush(neighbors, (cost, start_position))

        while neighbors:
            current_cost, current_position = heapq.heappop(neighbors)
            current_x, current_y = current_position

            # Reached end of the grid
            if current_x == SIZE - 1:
                path = []
                current = current_position
                
                while current is not None:
                    path.append(solved_sudoku[current[1]][current[0]])
                    current = previous[current]
                
                path.reverse()
                paths[y] = path
                break
            
            # Get neighbors
            # Top right
            if current_y - 1 >= 0 and current_x + 1 < SIZE:
                add_neighbor(
                    solved_sudoku, costs,
                    previous, neighbors,
                    current_cost, current_position,
                    current_x + 1, current_y - 1
                )

            # Right
            if current_x + 1 < SIZE:
                add_neighbor(
                    solved_sudoku, costs,
                    previous, neighbors,
                    current_cost, current_position,
                    current_x + 1, current_y
                )

            # Bottom right
            if current_y + 1 < SIZE and current_x + 1 < SIZE:
                add_neighbor(
                    solved_sudoku, costs,
                    previous, neighbors,
                    current_cost, current_position,
                    current_x + 1, current_y + 1
                )
    
    # Determine shortest path
    shortest_path = min(paths.values(), key=sum)

    return shortest_path


# DO NOT CHANGE CODE BELOW THIS LINE
if __name__ == "__main__":
    print_sudoku(SUDOKU)

    solved_sudoku = solve(SUDOKU, sudoku_connections)
    print_sudoku(solved_sudoku)

    values = minimal_line(solved_sudoku)
    print("Minimal total value: "+str(sum(values)))
    print("Value: "+str(values))
