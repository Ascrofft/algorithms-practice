from heapq_priority_queue import HeapqPriorityQueue
import unittest


class HeapTest(unittest.TestCase):

    def setUp(self):
        self.heapq = HeapqPriorityQueue()

    def test_heapq_is_empty_at_start(self):
        self.assertTrue(self.heapq.is_empty())

    def test_heapq_is_not_empty_after_add(self):
        self.heapq.add(10)

        self.assertFalse(self.heapq.is_empty())

    def test_heapq_accepts_multiple_adds(self):
        self.heapq.add(10)
        self.heapq.add(20)
        self.heapq.add(30)

        self.assertEqual(self.heapq.length(), 3)

    def test_fetch_smallest_returns_smallest_value(self):
        self.heapq.add(15)
        self.heapq.add(10)
        self.heapq.add(20)

        self.assertEqual(self.heapq.fetch_smallest(), 10)

    def test_fetch_smallest_removes_item_from_queue(self):
        self.heapq.add(10)
        self.heapq.add(20)

        self.heapq.fetch_smallest()

        self.assertEqual(self.heapq.length(), 1)

    def test_heapq_is_empty_after_all_items_are_fetched(self):
        self.heapq.add(10)

        self.heapq.fetch_smallest()

        self.assertTrue(self.heapq.is_empty())

    def test_heapq_returns_correct_length(self):
        self.heapq.add(15)
        self.heapq.add(10)

        self.assertEqual(self.heapq.length(), 2)


if __name__ == '__main__':
    unittest.main()
