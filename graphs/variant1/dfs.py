from mazes import maze1, maze2
from time import sleep

# Colors
FG_RED = '\x1b[31m'
FG_YELLOW = '\x1b[93m'
FG_RESET = '\x1b[39m'
# Change interval to speed or slowdown the drawing of the maze.
INTERVAL = 0.05

def solve(maze):
    """Finds a solution for the given `maze` from the top left square to the bottom right square,
    and mark the found path with 'o' characters. Returns a boolean indicating if a path was found.
    """

    height = len(maze)
    width = len(maze[0])
    origin = (0, 0)
    destination = (width-1, height-1)

    visited = set()

    def get_directions(position):
        x = position[0]
        y = position[1]
        directions = []

        # Check right
        if x + 1 < width and maze[y][x + 1] != '#' and (x + 1, y) not in visited:
            directions.append((x + 1, y))

        # Check down
        if y + 1 < height and maze[y + 1][x] != '#' and (x, y + 1) not in visited:
            directions.append((x, y + 1))

        # Check left
        if x - 1 >= 0 and maze[y][x - 1] != '#' and (x - 1, y) not in visited:
            directions.append((x - 1, y))

        # Check top
        if y - 1 >= 0 and maze[y - 1][x] != '#' and (x, y - 1) not in visited:
            directions.append((x, y - 1))

        return directions

    def visit(position):
        """This inner function (a function defined within a function) should be
        used recursively to visit a `position`."""
        # Add position to visited
        visited.add(position)

        # Mark position
        draw_on_maze(maze, position, '.')

        # Is position destination
        if position == destination:
            # We need to find a way to backtrack and replace path with 'o'
            draw_on_maze(maze, position, 'o')
            return True

        # Determine direction
        directions = get_directions(position)

        # Call visit(next_position)
        for direction in directions:
            result = visit(direction)

            if result == True:
                draw_on_maze(maze, position, 'o')
                return result

        # No path found.
        return False

    return visit(origin)


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

    # for maze_num, maze in [(1, maze1)]:
    #     print(f"----- Maze {maze_num} -----\n")
    #     if solve(maze):
    #         print_maze(maze)
    #     else:
    #         print("No path.\n\n")

    # for maze_num, maze in [(2, maze2)]:
    #     print(f"----- Maze {maze_num} -----\n")
    #     if solve(maze):
    #         print_maze(maze)
    #     else:
    #         print("No path.\n\n")
