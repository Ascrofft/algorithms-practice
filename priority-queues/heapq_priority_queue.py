import heapq

class HeapqPriorityQueue:

    def __init__(self):
        self.__data = []

    def add(self, value) -> None:
        """Add `value` to the priority queue."""
        heapq.heappush(self.__data, value)

    def fetch_smallest(self) -> int:
        """Find the smallest value in the priority queue, remove it from the
        queue and return it."""
        return heapq.heappop(self.__data)

    def is_empty(self) -> bool:
        """Returns `True` if the queue is empty, and `False` otherwise."""
        return len(self.__data) == 0

    def length(self) -> int:
        """Returns the length of items in the queue"""
        return len(self.__data)
