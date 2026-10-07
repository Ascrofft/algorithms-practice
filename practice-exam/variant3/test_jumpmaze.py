import unittest
import jumpmaze


class TestJumpmaze(unittest.TestCase):

    def test_add_neighbor_adds_new_uphill_neighbor(self):
        maze = [
            [10, 15],
            [1, 1]
        ]

        costs = {(0, 0): 0}
        previous = {(0, 0): None}
        nodes = []

        jumpmaze.add_neighbor(
            maze,
            costs,
            previous,
            nodes,
            0,
            10,
            (0, 0),
            (1, 0)
        )

        self.assertEqual(costs[(1, 0)], 5)
        self.assertEqual(previous[(1, 0)], (0, 0))
        self.assertEqual(nodes, [(5, (1, 0))])

    def test_add_neighbor_adds_downhill_neighbor_without_extra_cost(self):
        maze = [
            [10, 5],
            [1, 1]
        ]

        costs = {(0, 0): 7}
        previous = {(0, 0): None}
        nodes = []

        jumpmaze.add_neighbor(
            maze,
            costs,
            previous,
            nodes,
            7,
            10,
            (0, 0),
            (1, 0)
        )

        self.assertEqual(costs[(1, 0)], 7)

    def test_add_neighbor_overwrites_neighbor_with_lower_cost(self):
        maze = [
            [10, 12],
            [1, 1]
        ]

        costs = {
            (0, 0): 0,
            (1, 0): 10
        }

        previous = {
            (0, 0): None,
            (1, 0): (1, 1)
        }

        nodes = []

        jumpmaze.add_neighbor(
            maze,
            costs,
            previous,
            nodes,
            0,
            10,
            (0, 0),
            (1, 0)
        )

        self.assertEqual(costs[(1, 0)], 2)
        self.assertEqual(previous[(1, 0)], (0, 0))

    def test_add_neighbor_keeps_known_neighbor_with_lower_cost(self):
        maze = [
            [10, 15],
            [1, 1]
        ]

        costs = {
            (0, 0): 0,
            (1, 0): 3
        }

        previous = {
            (0, 0): None,
            (1, 0): (1, 1)
        }

        nodes = []

        jumpmaze.add_neighbor(
            maze,
            costs,
            previous,
            nodes,
            0,
            10,
            (0, 0),
            (1, 0)
        )

        self.assertEqual(costs[(1, 0)], 3)
        self.assertEqual(previous[(1, 0)], (1, 1))
        self.assertEqual(nodes, [])


    def test_build_positions_by_height_groups_equal_heights(self):
        maze = [
            [1, 2],
            [1, 3]
        ]

        positions = {}

        jumpmaze.build_positions_by_height(
            maze,
            2,
            positions
        )

        self.assertEqual(
            positions[1],
            [(0, 0), (0, 1)]
        )

    def test_build_positions_by_height_ignores_blockades(self):
        maze = [
            [1, 0],
            [2, 1]
        ]

        positions = {}

        jumpmaze.build_positions_by_height(
            maze,
            2,
            positions
        )

        self.assertNotIn(0, positions)


    def test_solve_find_shortest_path(self):
        maze = [
            [1, 1, 0,],
            [2, 1, 4,],
            [0, 0, 2,],
        ]
        
        self.assertEqual(
            jumpmaze.solve(maze), 
            [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2)]
        )

    def test_solve_no_valid_path_found(self):
        invalid_maze = [
            [1, 1, 0,],
            [2, 0, 4,],
            [0, 0, 2,],
        ]
        
        self.assertIsNone(jumpmaze.solve(invalid_maze))

    def test_solve_uses_teleport_when_jumps_enabled(self):
        maze = [
            [1, 2, 3],
            [4, 5, 1],
            [6, 8, 9]
        ]

        self.assertEqual(
            jumpmaze.solve(maze, True),
            [(0, 0), (2, 1), (2, 2)]
        )

    def test_solve_does_not_teleport_when_jumps_disabled(self):
        maze = [
            [1, 2, 3],
            [4, 5, 1],
            [6, 8, 9]
        ]

        path = jumpmaze.solve(maze, False)

        self.assertNotEqual(
            path,
            [(0, 0), (2, 1), (2, 2)]
        )

    def test_solve_single_square_maze(self):
        maze = [[1]]

        self.assertEqual(
            jumpmaze.solve(maze),
            [(0, 0)]
        ) 


if __name__ == "__main__":
    unittest.main()
