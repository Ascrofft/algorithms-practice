import unittest
from my_data_structure import MyDataStructure


class TestMyDataStructure(unittest.TestCase):

    def setUp(self):
        self.data_structure = MyDataStructure()

    def test_add_integer(self):
        self.data_structure.add(1)
        self.assertIn(1, self.data_structure)
        self.assertEqual(len(self.data_structure), 1)

    def test_add_string(self):
        self.data_structure.add("Saxion")
        self.assertIn("Saxion", self.data_structure)
        self.assertEqual(len(self.data_structure), 1)

    def test_add_duplicate_data_is_not_added(self):
        self.data_structure.add(1)
        self.data_structure.add(1)
        self.assertEqual(len(self.data_structure), 1)

    def test_remove_not_in(self):
        self.data_structure.add(1)
        self.data_structure.remove(1)
        self.assertNotIn(1, self.data_structure)
        self.assertEqual(len(self.data_structure), 0)

    def test_remove_missing_value_raises_error(self):
        with self.assertRaises(KeyError):
            self.data_structure.remove(5)
    
    def test_to_list(self):
        values = [1, 2, 3]
        a = MyDataStructure(values)

        result = a.to_list()

        self.assertEqual(result, values)

    def test_contains(self):
        self.data_structure.add("Saxion")
        self.assertTrue("Saxion" in self.data_structure)
        self.assertFalse(42 in self.data_structure)

    def test_union_is_the_combination(self):
        a = MyDataStructure([1])
        b = MyDataStructure([2])

        result = a.union(b)

        self.assertIn(1, result)
        self.assertIn(2, result)

    def test_union_duplicate_data(self):
        a = MyDataStructure([1, 2])
        b = MyDataStructure([2, 3])

        result = a.union(b)

        self.assertIn(1, result)
        self.assertIn(2, result)
        self.assertIn(3, result)
        self.assertEqual(len(result), 3)

    def test_intersection(self):
        a = MyDataStructure([1, 2])
        b = MyDataStructure([2, 3])

        result = a.intersection(b)

        self.assertIn(2, result)
        self.assertEqual(len(result), 1)

    def test_difference(self):
        a = MyDataStructure([1, 2])
        b = MyDataStructure([2])

        result = a.difference(b)

        self.assertIn(1, result)
        self.assertNotIn(2, result)
        self.assertEqual(len(result), 1)

    def test_difference_supports_value_not_in(self):
        a = MyDataStructure([1, 2])
        b = MyDataStructure([2, 3])

        result = a.difference(b)

        self.assertIn(1, result)
        self.assertNotIn(3, result)
        self.assertEqual(len(result), 1)

    def test_iteration(self):
        values = [1, 2, 3]
        for v in values:
            self.data_structure.add(v)

        collected = MyDataStructure()

        for v in self.data_structure:
            collected.add(v)

        self.assertEqual(values, collected.to_list())


if __name__ == "__main__":
    unittest.main()
