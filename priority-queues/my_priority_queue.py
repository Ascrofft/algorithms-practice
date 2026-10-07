import priority_queue_tests


class MyPriorityQueue:

    def __init__(self):
        self.data = []
        self.data.sort()

    def add(self, value):
        """Add `value` to the priority queue."""
        if self.is_empty():
            self.data.append(value)
            return
        
        left = 0
        right = len(self.data) - 1
        
        while left <= right:
            middle = (left + right) // 2

            if value < self.data[middle]:
                left = middle + 1
            else:
                right = middle - 1

        self.data.insert(left, value)


    def fetch_smallest(self):
        """Find the smallest value in the priority queue, remove it from the
        queue and return it."""
        return self.data.pop()
        
    def is_empty(self):
        """Returns `True` if the queue is empty, and `False` otherwise."""
        return len(self.data) <= 0


if __name__ == '__main__':
    priority_queue_tests.run_all_tests(MyPriorityQueue)
