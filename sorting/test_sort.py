import unittest
import sort
import random

random.seed(1)
inputs = {count: [random.randint(0, 99999) for _ in range(count)] for count in [10, 100, 2500]}
outputs = {count: sorted(data) for count, data in inputs.items()}

class SortTest(unittest.TestCase):

    def test_custom(self):
        self._test_algorithm(sort.custom_sort)

    def test_selection(self):
        self._test_algorithm(sort.selection_sort)

    def test_merge(self):
        self._test_algorithm(sort.merge_sort)

    def test_quick(self):
        self._test_algorithm(sort.quick_sort)

    def _test_algorithm(self, sorter):
        for count, data in inputs.items():
            import_data = data.copy()
            sorter(import_data)
            self.assertEqual(import_data, outputs[count])


if __name__ == '__main__':
    unittest.main()
