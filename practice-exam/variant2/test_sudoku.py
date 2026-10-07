import copy
import unittest
import sudoku


SOLVED_SUDOKU = [
    [4, 1, 3, 6, 5, 9, 8, 2, 7],
    [2, 7, 6, 1, 9, 8, 5, 4, 3],
    [3, 8, 4, 9, 7, 5, 2, 6, 1],
    [7, 2, 8, 3, 4, 1, 9, 5, 6],
    [9, 5, 2, 7, 3, 6, 4, 1, 8],
    [5, 6, 1, 4, 8, 7, 3, 9, 2],
    [6, 4, 9, 8, 1, 2, 7, 3, 5],
    [1, 3, 7, 5, 2, 4, 6, 8, 9],
    [8, 9, 5, 2, 6, 3, 1, 7, 4],
]


class TestSudoku(unittest.TestCase):

    # -------------------------
    # Provided helpers
    # -------------------------

    def test_valid_horizontal_returns_true_when_value_is_missing(self):
        self.assertTrue(
            sudoku.valid_horizontal(1, sudoku.SUDOKU, 0)
        )

    def test_valid_horizontal_returns_false_when_value_exists(self):
        self.assertFalse(
            sudoku.valid_horizontal(5, sudoku.SUDOKU, 0)
        )

    def test_valid_vertical_returns_true_when_value_is_missing(self):
        self.assertTrue(
            sudoku.valid_vertical(1, sudoku.SUDOKU, 0)
        )

    def test_valid_vertical_returns_false_when_value_exists(self):
        self.assertFalse(
            sudoku.valid_vertical(3, sudoku.SUDOKU, 0)
        )

    # -------------------------
    # Objective 1: valid_blob
    # -------------------------

    def test_valid_blob_returns_true_when_value_is_missing(self):
        self.assertTrue(
            sudoku.valid_blob(
                1,
                (0, 0),
                sudoku.SUDOKU,
                sudoku.sudoku_connections
            )
        )

    def test_valid_blob_returns_false_when_value_exists(self):
        self.assertFalse(
            sudoku.valid_blob(
                5,
                (0, 0),
                sudoku.SUDOKU,
                sudoku.sudoku_connections
            )
        )

    def test_valid_blob_ignores_same_value_in_another_blob(self):
        # 7 occurs elsewhere in the Sudoku, but not in blob 'a'
        self.assertTrue(
            sudoku.valid_blob(
                7,
                (0, 0),
                sudoku.SUDOKU,
                sudoku.sudoku_connections
            )
        )

    def test_valid_blob_finds_value_from_bottom_right_of_blob(self):
        # Blob i contains the given value 6 at another position.
        # Starting at (8, 8) also exercises the bottom/right grid edges.
        self.assertFalse(
            sudoku.valid_blob(
                6,
                (8, 8),
                sudoku.SUDOKU,
                sudoku.sudoku_connections
            )
        )

    # -------------------------
    # Objective 2: solve
    # -------------------------

    def test_solve_returns_expected_solution(self):
        puzzle = copy.deepcopy(sudoku.SUDOKU)

        result = sudoku.solve(
            puzzle,
            sudoku.sudoku_connections
        )

        self.assertEqual(result, SOLVED_SUDOKU)

    def test_solve_can_fill_single_missing_value(self):
        puzzle = copy.deepcopy(SOLVED_SUDOKU)
        puzzle[0][0] = 0

        result = sudoku.solve(
            puzzle,
            sudoku.sudoku_connections
        )

        self.assertEqual(result, SOLVED_SUDOKU)

    def test_solve_returns_no_solution_for_invalid_sudoku(self):
        puzzle = copy.deepcopy(SOLVED_SUDOKU)

        # Create duplicate 1 in the first row.
        puzzle[0][0] = 1

        result = sudoku.solve(
            puzzle,
            sudoku.sudoku_connections
        )

        self.assertEqual(result, "No solution")

    # -------------------------
    # Objective 3: minimal_line
    # -------------------------

    def test_minimal_line_returns_cheapest_path(self):
        result = sudoku.minimal_line(SOLVED_SUDOKU)

        self.assertEqual(
            result,
            [1, 4, 1, 4, 1, 2, 3, 1, 2]
        )

    def test_minimal_line_has_one_value_per_column(self):
        result = sudoku.minimal_line(SOLVED_SUDOKU)

        self.assertEqual(len(result), 9)

    def test_minimal_line_has_expected_minimum_sum(self):
        result = sudoku.minimal_line(SOLVED_SUDOKU)

        self.assertEqual(sum(result), 19)


if __name__ == "__main__":
    unittest.main()
