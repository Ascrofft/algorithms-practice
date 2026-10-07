
import random
import time
import math
import colorama
import heapq


def generate_maze(size=24, seed=None):
    """Create a new random maze to be solved.

    Args:
        size (int): The width and height of the maze.
        seed (int): The random seed; when create_maze is called twice with the same size and seed,
            the exact same maze list will be returned.

    Returns:
        A two dimensional list of heights associated with the squares, order `[row][column]`. When
        the height is `0`, there is a blocking element in this square.
    """
    if seed is not None:
        random.seed(seed)

    squares = []
    
    for _ in range(size):
        row = []
        for _ in range(size):
            row.append(random.randint(1, size**2) if random.randint(0, 4) else 0)
        squares.append(row)

    # Make sure the start and end squares are not blocked
    squares[0][0] = 1
    squares[-1][-1] = 2

    return squares


def print_maze(squares, path=None, show_heights=False):
    """Print a (solved) maze to the terminal.

    Args:
        squares (list(list(int))): The maze.
        path (list(tuple)): An optional list of (x,y) tuples that forms a path to be shown.
        show_heights (boolean): Show the height for each square. This makes the printed maze a lot wider.
    """

    size = len(squares)
    height_chars = math.ceil(math.log10(size**2))

    reset = colorama.Style.RESET_ALL
    print(reset)
    for y, row in enumerate(squares):
        for x, height in enumerate(row):

            if height == 0:
                color = colorama.Back.RED + colorama.Fore.BLACK
            elif path is not None and (x, y) in path:
                color = colorama.Back.GREEN + colorama.Fore.BLACK
            else:
                color = colorama.Back.BLACK + colorama.Fore.WHITE

            if show_heights:
                number_str = (f"%0{height_chars}d" % height) if height else (" " * height_chars)
                print(f"{color}{number_str}{reset} ", end="")
            else:
                print(f"{color} ", end="")
        print(reset)
    print()


def demo(size=24, seed=None, jumps=False):
    """Generates a maze, solves it and prints the results.

    Args:
        size (int): Width and height of the maze to demo.
        seed (int): Random seed of the maze to generate.
        jumps (boolean): Allow jumps between squares with the same height.
    """

    if seed is None:
        seed = int(time.perf_counter()) % 10000

    print(f"Solving {size}x{size} seed {seed} {'with' if jumps else 'without'} jumps...")

    maze = generate_maze(size, seed)

    start_time = time.perf_counter()
    path = solve(maze, jumps)
    elapsed = time.perf_counter() - start_time

    if size <= 100:
        print_maze(maze, path, size <= 24)

    if path:
        print(f"Cheapest path: {path} (length {len(path)})")
    else:
        print("No path found")
        
    print(f"Solver took {round(elapsed, 3)}s\n\n\n")


def add_neighbor(maze, costs, previous, nodes, total_cost, node_cost, node_position, neighbor_position):
    nx, ny = neighbor_position
    neighbor_cost = maze[ny][nx]

    # Check if neighbor value is higher then our current position
    # If yes -> calculate the difference, we need to add these costs
    diff = 0
    if neighbor_cost > node_cost:
        diff = neighbor_cost - node_cost

    new_total_cost = total_cost + diff

    # Check if this route is cheaper then any other route
    # to neighbors position that is already known
    if new_total_cost < costs.get(neighbor_position, float("inf")):
        costs[neighbor_position] = new_total_cost
        previous[neighbor_position] = node_position
        heapq.heappush(nodes, (new_total_cost, neighbor_position))


def build_positions_by_height(maze, size, positions_by_height):
    for y in range(size):
        for x in range(size):
            height = maze[y][x]

            if height == 0:
                continue

            if height not in positions_by_height:
                positions_by_height[height] = []

            positions_by_height[height].append((x, y))


def solve(maze, jumps=False):
    """Calculate the cheapest (in terms of meters climbed) path for a maze.

    Args:
        maze (list(list(int))): The maze.

    Returns:
        The cheapest path as a list of (x,y) tuples, starting with the top left
        corner (0,0) and ending with the lower right corner (N-1, N-1).
        If no path exists, `None` is returned.
    """
    size = len(maze)
    origin = (0, 0)
    destination = (size - 1, size - 1)
    
    costs = {origin: 0}
    previous = {origin: None}
    nodes = []

    heapq.heappush(nodes, (0, origin))

    positions_by_height = {}
    used_jumps = set()

    if jumps:
        build_positions_by_height(maze, size, positions_by_height)

    while nodes:
        total_cost, node_position = heapq.heappop(nodes)
        
        if total_cost > costs[node_position]:
            continue

        node_x, node_y = node_position
        node_cost = maze[node_y][node_x]

        # Found destination
        if node_position == destination:
            path = []
            current = node_position

            while current is not None:
                path.append(current)
                current = previous[current]
            
            path.reverse()
            return path
        
        # Collect neighbors
        # Top
        if node_y - 1 >= 0 and maze[node_y - 1][node_x] != 0:
            add_neighbor(
                maze, costs,
                previous, nodes,
                total_cost, node_cost,
                node_position, (node_x, node_y - 1)
            )

        # Right
        if node_x + 1 < size and maze[node_y][node_x + 1] != 0:
            add_neighbor(
                maze, costs,
                previous, nodes,
                total_cost, node_cost,
                node_position, (node_x + 1, node_y)
            )

        # Bottom
        if node_y + 1 < size and maze[node_y + 1][node_x] != 0:
            add_neighbor(
                maze, costs,
                previous, nodes,
                total_cost, node_cost,
                node_position, (node_x, node_y + 1)
            )

        # Left
        if node_x - 1 >= 0 and maze[node_y][node_x - 1] != 0:
            add_neighbor(
                maze, costs,
                previous, nodes,
                total_cost, node_cost,
                node_position, (node_x - 1, node_y)
            )

        # Teleport
        if jumps and node_cost not in used_jumps:
            used_jumps.add(node_cost)

            for neighbor in positions_by_height[node_cost]:
                add_neighbor(
                    maze, costs,
                    previous, nodes,
                    total_cost, node_cost,
                    node_position, neighbor
                )

    return None


if __name__ == "__main__":
    print("------ Solvable mazes, without jumps ------\n")
    # demo(3, 122)
    # demo(7, 120)
    # demo(10, 3904)
    # demo(24, 3305)
    # demo(100, 595)
    # demo(250, 128)
    # demo(1000, 129)

    # print("------ Unsolvable mazes, without jumps ------\n")
    # demo(3, 20)
    # demo(24, 126)

    # print("------ Solvable mazes, with jumps ------\n")
    demo(10, 39047, True)
    demo(24, 3305, True)
    demo(100, 595, True)
    demo(1000, 129, True)
