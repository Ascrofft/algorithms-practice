import unittest
from discs import solve

class DiscsTest(unittest.TestCase):

    def tests(self):

        self.assertEqual(solve("A", "B", 0), [])
        self.assertEqual(solve("A", "B", 1), [("A", "B", 1)])
        self.assertEqual(solve("A", "B", 2), [("A", "C", 1), ("A", "B", 2), ("C", "B", 1)])

        self.assertEqual(solve("C", "A", 1), [("C", "A", 1)])
        self.assertEqual(solve("C", "A", 2), [("C", "B", 1), ("C", "A", 2), ("B", "A", 1)])

        # We'll test the puzzle with 0 up to 7 discs
        for count in range(8):
            with self.subTest(count=count):
                # Run the algorithms to get the instructions
                instructions = solve("A", "B", count)

                with self.subTest(instructions=instructions):

                    # Create the stacks as they are in the start position
                    stacks = {"A": list(range(count, 0, -1)), "B": [], "C": []}

                    # Apply the instructions to `stacks` and check that they make sense
                    for instruction_pos, (source, target, disc) in enumerate(instructions):
                        self.assertEqual(stacks[source][-1] if stacks[source] else None, disc, f"Disc not found on top of the source stack at instruction {instruction_pos} {stacks}")
                        stacks[source].pop()
                        if stacks[target]:
                            self.assertLess(disc, stacks[target][-1], f"Disc would be on top of a smaller disc at instruction {instruction_pos} {stacks}")
                        stacks[target].append(disc)

                    # Check if the end result is as expected
                    self.assertEqual(stacks, {"A": [], "B": list(range(count, 0, -1)), "C": []}, "Invalid end result")


if __name__ == '__main__':
    unittest.main()
