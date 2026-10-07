from mazes import maze1, maze2  # type: ignore  # noqa: F401, I001
from collections import deque
from time import sleep

# Colors
FG_RED = '\x1b[31m'
FG_YELLOW = '\x1b[93m'
FG_RESET = '\x1b[39m'
# Change interval to speed or slowdown the drawing of the maze.
INTERVAL = 0.01


def get_neighbors(maze, width, height, position, previous):
    x = position[0]
    y = position[1]
    directions = []

    # Check right
    if x + 1 < width and maze[y][x + 1] == ' ' and (x + 1, y) not in previous:
        directions.append((x + 1, y))

    # Check down
    if y + 1 < height and maze[y + 1][x] == ' ' and (x, y + 1) not in previous:
        directions.append((x, y + 1))

    # Check left
    if x - 1 >= 0 and maze[y][x - 1] == ' ' and (x - 1, y) not in previous:
        directions.append((x - 1, y))

    # Check top
    if y - 1 >= 0 and maze[y - 1][x] == ' ' and (x, y - 1) not in previous:
        directions.append((x, y - 1))

    return directions


def solve(maze):
    """Finds the shortest solution for the given `maze` from the top left square to the bottom right
    square, and mark the found path with 'o' characters. Returns a boolean indicating if a path was found.
    """
    height = len(maze)
    width = len(maze[0])
    origin = (0, 0)
    destination = (width-1, height-1)

    location_found = False

    # Create deque list to add neighbors
    neighbors = deque()

    # Create previous dict
    previous: dict[tuple[int, int], tuple[int, int] | None] = {
        origin: None
    }

    # Add origin to neighbors
    neighbors.append(origin)

    # Start While neighbors loop
    while neighbors:

        # Pop first location to visit
        location = neighbors.popleft()

        draw_on_maze(maze, location, '.')

        # Check if location is destination
        if location == destination:
            location_found = True
            break
        
        # Collect neighbors
        collected = get_neighbors(maze, width, height, location, previous)

        for neighbor in collected:
            neighbors.append(neighbor)
            previous[neighbor] = location
    
    if location_found:
        current = destination
        while current is not None:
            draw_on_maze(maze, current, 'o')
            current = previous[current]
    
    return False


def draw_on_maze(maze, position, char):
    x, y = position
    maze[y] = maze[y][0:x] + char + maze[y][x+1:]
    print_maze(maze)


def print_maze(maze):
    sleep(INTERVAL)
    # Clean screen
    print('\033[2J')
    # Ansi escape sequences, for showing the path as red and dots as yellow
    maze_text = "\n".join(maze)
    path_len = maze_text.count("o")
    explored = maze_text.count(".")

    maze_text = maze_text.replace('.', FG_YELLOW+'.'+FG_RESET)
    maze_text = maze_text.replace('o', FG_RED+'o'+FG_RESET)
    print(f"Path length: {path_len}\nOther squares explored: {explored}\n{maze_text}\n")


if __name__ == '__main__':
    # for maze_num, maze in [(1, maze1), (2, maze2)]:
    #     print(f"----- Maze {maze_num} -----\n")
    #     if solve(maze):
    #         print_maze(maze)
    #     else:
    #         print("No path.\n\n")

    # print("----- Maze 1 -----\n")
    # if solve(maze1):
    #     print_maze(maze1)
    # else:
    #     print("No path.\n\n")

    print("----- Maze 2 -----\n")
    if solve(maze2):
        print_maze(maze2)
    else:
        print("No path.\n\n")
