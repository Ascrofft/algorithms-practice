import unittest, random, time
import search

class Linear(unittest.TestCase):
    """Unittest for testing the complete linear-search-algorithm"""

    def test_basic_functions(self):
        """Testing the basic functionality of calling method with a return of a list"""
        # Check if function returns a list type
        self.assertIsInstance(search.linear_search([], []), list, "SD42-Error: algorithm returns something other than a list")
    
    def test_empty_haystack_needles(self):
        """Testing if haystack or needles are empty"""
        # Test with a empty haystack
        self.assertListEqual(search.linear_search([], [1]), [None], "SD42-Error: wrong result for empty haystack")
        # Test with empty needles
        self.assertListEqual(search.linear_search([1, 2, 3, 4], []), [], "SD42-Error: wrong result for empty needles")

    def test_small_haystack_and_needles(self):
        # Test with a single hay and needle
        self.assertEqual(search.linear_search([1], [1]), [0], "SD42-Error: wrong result for haystack with length 1")

        # Test with 2 hay's and one needle
        self.assertEqual(search.linear_search([1, 2], [1]), [0], "SD42-Error: incorrect position of the needle, must be index 0")
        self.assertEqual(search.linear_search([1, 2], [2]), [1], "SD42-Error: incorrect position of the needle, must be index 1")
        self.assertEqual(search.linear_search([1, 2], [3]), [None], "SD42-Error: incorrect position of the needle, must be None")

        # Test a small set with given haystack and needles
        haystack = [1, 2, 3, 4, 5]
        needles = [2, 10]
        result = [1, None]
        self.assertListEqual(search.linear_search(haystack, needles), result, "SD42-Error: incorrect positions of the needles, must be a [1, None]")

    def test_extensive_haystack_and_needles(self):
        # Generate a list of ordered numbers
        haystack = []
        next_number = 0
        for _ in range(search.haystack_size):
            next_number += random.randint(0, 3)
            haystack.append(next_number)

        # Create a small needles stack
        needles = [random.randint(haystack[0], haystack[-1]) for _ in range(search.needle_count)]

        results = search.linear_search(haystack, needles)

        # Check if the results of linear-search is a instance of a list
        self.assertIsInstance(results, list, "SD42-Error: algorithm returns something other than a list.")

        # Check if the length is equal of the result vs the needles
        self.assertEqual(len(results), len(needles), "SD42-Error: The result has not the same length as the given needles.")

        for target_index, target_number in enumerate(needles):
            haystack_index = results[target_index]
            
            if haystack_index is None:
                self.assertNotIn(target_number, haystack, f"SD42-Error: algorithm incorrectly says that {target_number} is not in haystack")
            else:
                self.assertEqual(haystack[haystack_index], target_number, f"SD42-Error: algorithm says that {target_number} is at position {haystack_index} in the haystack, but that position contains {haystack[haystack_index]}")

class Dictionary(unittest.TestCase):
    """Unittest for testing the complete dict-search-algorithm"""

    def test_basic_functions(self):
        """Testing the basic functionality of calling method with a return of a list"""
        # Check if function returns a list type
        self.assertIsInstance(search.dict_search([], []), list, "SD42-Error: algorithm returns something other than a list")
    
    def test_empty_haystack_needles(self):
        """Testing if haystack or needles are empty"""
        # Test with a empty haystack
        self.assertListEqual(search.dict_search([], [1]), [None], "SD42-Error: wrong result for empty haystack")
        # Test with empty needles
        self.assertListEqual(search.dict_search([1, 2, 3, 4], []), [], "SD42-Error: wrong result for empty needles")

    def test_small_haystack_and_needles(self):
        # Test with a single hay and needle
        self.assertEqual(search.dict_search([1], [1]), [0], "SD42-Error: wrong result for haystack with length 1")

        # Test with 2 hay's and one needle
        self.assertEqual(search.dict_search([1, 2], [1]), [0], "SD42-Error: incorrect position of the needle, must be index 0")
        self.assertEqual(search.dict_search([1, 2], [2]), [1], "SD42-Error: incorrect position of the needle, must be index 1")
        self.assertEqual(search.dict_search([1, 2], [3]), [None], "SD42-Error: incorrect position of the needle, must be None")

        # Test a small set with given haystack and needles
        haystack = [1, 2, 3, 4, 5]
        needles = [2, 10]
        result = [1, None]
        self.assertListEqual(search.dict_search(haystack, needles), result, "SD42-Error: incorrect positions of the needles, must be a [1, None]")

    def test_extensive_haystack_and_needles(self):
        # Generate a list of ordered numbers
        haystack = []
        next_number = 0
        for _ in range(search.haystack_size):
            next_number += random.randint(0, 3)
            haystack.append(next_number)

        # Create a small needles stack
        needles = [random.randint(haystack[0], haystack[-1]) for _ in range(search.needle_count)]

        results = search.dict_search(haystack, needles)

        # Check if the results of dictionary-search is a instance of a list
        self.assertIsInstance(results, list, "SD42-Error: algorithm returns something other than a list.")

        # Check if the length is equal of the result vs the needles
        self.assertEqual(len(results), len(needles), "SD42-Error: The result has not the same length as the given needles.")

        for target_index, target_number in enumerate(needles):
            haystack_index = results[target_index]
            
            if haystack_index is None:
                self.assertNotIn(target_number, haystack, f"SD42-Error: algorithm incorrectly says that {target_number} is not in haystack")
            else:
                self.assertEqual(haystack[haystack_index], target_number, f"SD42-Error: algorithm says that {target_number} is at position {haystack_index} in the haystack, but that position contains {haystack[haystack_index]}")


class Binary(unittest.TestCase):
    """Unittest for testing the complete binary-search-algorithm"""

    def test_basic_functions(self):
        """Testing the basic functionality of calling method with a return of a list"""
        # Check if function returns a list type
        self.assertIsInstance(search.binary_search([], []), list, "SD42-Error: algorithm returns something other than a list")
    
    def test_empty_haystack_needles(self):
        """Testing if haystack or needles are empty"""
        # Test with a empty haystack
        self.assertListEqual(search.binary_search([], [1]), [None], "SD42-Error: wrong result for empty haystack")
        # Test with empty needles
        self.assertListEqual(search.binary_search([1, 2, 3, 4], []), [], "SD42-Error: wrong result for empty needles")

    def test_small_haystack_and_needles(self):
        # Test with a single hay and needle
        self.assertEqual(search.binary_search([1], [1]), [0], "SD42-Error: wrong result for haystack with length 1")

        # Test with 2 hay's and one needle
        self.assertEqual(search.binary_search([1, 2], [1]), [0], "SD42-Error: incorrect position of the needle, must be index 0")
        self.assertEqual(search.binary_search([1, 2], [2]), [1], "SD42-Error: incorrect position of the needle, must be index 1")
        self.assertEqual(search.binary_search([1, 2], [3]), [None], "SD42-Error: incorrect position of the needle, must be None")

        # Test a small set with given haystack and needles
        haystack = [1, 2, 3, 4, 5]
        needles = [2, 10]
        result = [1, None]
        self.assertListEqual(search.binary_search(haystack, needles), result, "SD42-Error: incorrect positions of the needles, must be a [1, None]")

    def test_extensive_haystack_and_needles(self):
        # Generate a list of ordered numbers
        haystack = []
        next_number = 0
        for _ in range(search.haystack_size):
            next_number += random.randint(0, 3)
            haystack.append(next_number)

        # Create a small needles stack
        needles = [random.randint(haystack[0], haystack[-1]) for _ in range(search.needle_count)]

        results = search.binary_search(haystack, needles)

        # Check if the results of binary-search is a instance of a list
        self.assertIsInstance(results, list, "SD42-Error: algorithm returns something other than a list.")

        # Check if the length is equal of the result vs the needles
        self.assertEqual(len(results), len(needles), "SD42-Error: The result has not the same length as the given needles.")

        for target_index, target_number in enumerate(needles):
            haystack_index = results[target_index]
            
            if haystack_index is None:
                self.assertNotIn(target_number, haystack, f"SD42-Error: algorithm incorrectly says that {target_number} is not in haystack")
            else:
                self.assertEqual(haystack[haystack_index], target_number, f"SD42-Error: algorithm says that {target_number} is at position {haystack_index} in the haystack, but that position contains {haystack[haystack_index]}")

class ExecutionTime(unittest.TestCase):

    linear_time = 0.0
    dictionary_time = 0.0
    binary_time = 0.0

    @classmethod
    def setUpClass(cls):
        cls.haystack = []
        next_number = 0
        for _ in range(2000000):
            next_number += random.randint(0, 3)
            cls.haystack.append(next_number)

        # Create a small needles stack
        cls.needles = [random.randint(cls.haystack[0], cls.haystack[-1]) for _ in range(100)]

    def linear_execution_time(self):
        start_time = time.perf_counter()
        search.linear_search(ExecutionTime.haystack, ExecutionTime.needles)
        end_time = time.perf_counter()
        self.linear_time = round(end_time - start_time, 5)

    def dictionary_execution_time(self):
        start_time = time.perf_counter()
        search.dict_search(ExecutionTime.haystack, ExecutionTime.needles)
        end_time = time.perf_counter()
        self.dictionary_time = round(end_time - start_time, 5)

    def binary_execution_time(self):
        start_time = time.perf_counter()
        search.binary_search(ExecutionTime.haystack, ExecutionTime.needles)
        end_time = time.perf_counter()
        self.binary_time = round(end_time - start_time, 5)
    
    def test_timings(self):
        self.linear_execution_time()
        self.dictionary_execution_time()
        self.binary_execution_time()
        print(f'Linear-search, execution-time {self.linear_time} seconds.')
        print(f'Dictionary-search, execution-time {self.dictionary_time} seconds.')
        print(f'Binary-search, execution-time {self.binary_time} seconds.')

if __name__ == '__main__':
    unittest.main(verbosity=2, failfast=True)
