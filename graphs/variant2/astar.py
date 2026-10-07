from mazes import maze1, maze2
import heapq
from time import sleep

# Colors
FG_RED = '\x1b[31m'
FG_YELLOW = '\x1b[93m'
FG_RESET = '\x1b[39m'

# Change interval to speed or slowdown the drawing of the maze.
INTERVAL = 0.1

def heuristic(position, destination):
    px, py = position
    dx, dy = destination
    return abs(px - dx) + abs(py - dy)


def get_directions(maze, width, height, position):
        x = position[0]
        y = position[1]
        directions = []

        # Check right
        if x + 1 < width and maze[y][x + 1] != '#':
            directions.append((x + 1, y))

        # Check down
        if y + 1 < height and maze[y + 1][x] != '#':
            directions.append((x, y + 1))

        # Check left
        if x - 1 >= 0 and maze[y][x - 1] != '#':
            directions.append((x - 1, y))

        # Check top
        if y - 1 >= 0 and maze[y - 1][x] != '#':
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

    previous: dict[tuple, tuple | None] = {
        origin: None
    }

    g_score = {
        origin: 0
    }

    queue = []

    start_g = 0
    start_h = heuristic(origin, destination)
    start_f = start_g + start_h

    heapq.heappush(queue, (start_f, start_g, origin))

    while queue:
        _, current_g, current_position = heapq.heappop(queue)

        if current_g > g_score[current_position]:
            continue

        draw_on_maze(maze, current_position, '.')

        if current_position == destination:
            current = destination

            while current is not None:
                draw_on_maze(maze, current, 'o')
                current = previous[current]

            return True

        neighbors = get_directions(maze, width, height, current_position)

        for neighbor in neighbors:
            neighbor_g = current_g + 1

            if neighbor_g < g_score.get(neighbor, float('inf')):
                g_score[neighbor] = neighbor_g
                previous[neighbor] = current_position

                neighbor_h = heuristic(neighbor, destination)
                neighbor_f = neighbor_g + neighbor_h

                heapq.heappush(queue, (neighbor_f, neighbor_g, neighbor))

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
    for maze_num, maze in [(1, maze1), (2, maze2)]:
        print(f"----- Maze {maze_num} -----\n")
        if solve(maze):
            print_maze(maze)
        else:
            print("No path.\n\n")
