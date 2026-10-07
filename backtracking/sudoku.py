from time import sleep

board = [
    [1, 4, 8, 0, 7, 0, 0, 0, 0],
    [9, 5, 7, 0, 2, 8, 0, 0, 0],
    [6, 3, 0, 5, 9, 1, 8, 4, 7],

    [0, 9, 5, 2, 3, 0, 0, 0, 1],
    [0, 0, 1, 0, 4, 6, 0, 5, 3],
    [0, 7, 0, 1, 0, 0, 0, 0, 0],

    [7, 2, 0, 8, 6, 9, 4, 0, 0],
    [0, 1, 9, 7, 0, 4, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 0]
] # This one should solve in a couple seconds (with sleep_time of 0.05)

unsolvable_board = [
    [2, 0, 0, 9, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 6, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],

    [5, 0, 2, 6, 0, 0, 4, 0, 7],
    [0, 0, 0, 0, 0, 4, 1, 0, 0],
    [0, 0, 0, 0, 9, 8, 0, 2, 3],

    [0, 0, 0, 0, 0, 3, 0, 8, 0],
    [0, 0, 5, 0, 1, 4, 0, 0, 0],
    [0, 0, 7, 0, 0, 0, 0, 0, 0]
] # This one should take roughly 1 minute to detect it's not solvable (comment out the print and sleep statements)

sleep_time = 0.05


def solve(board : list[list[int]]):
    """Solve a 9x9 sudoku by filling in all empty (0) squares in the given 2D array.

    Return True when successful or False otherwise.
    """
    for row in range(9):
        for column in range(9):

            if board[row][column] == 0:

                for value in range(1, 10):

                    if is_valid(board, row, column, value):
                        board[row][column] = value

                        print_board(board)
                        sleep(sleep_time)

                        if solve(board):
                            return True

                        board[row][column] = 0

                return False

    return True


def is_valid(board, row, column, value):
    if value in board[row]:
        return False

    for i in range(9):
        if board[i][column] == value:
            return False

    box_row = (row // 3) * 3
    box_column = (column // 3) * 3

    for i in range(box_row, box_row + 3):
        for j in range(box_column, box_column + 3):
            if board[i][j] == value:
                return False

    return True


def print_board(board):
    "Pretty print a 9x9 sudoku board given as 2D array."
    for row_num, row in enumerate(board):
        if row_num % 3 == 0 and row_num != 0:
            print("-"*29)
        for col_num, col in enumerate(row):
            if col_num % 3 == 0 and col_num != 0:
                print("|", end="")
            print(f" {col} " if col else "   ", end="")
        print()
    print()


if __name__ == "__main__":
    print_board(board)
    if solve(board):
        print("Solved!")
    else:
        print("No solution.")
