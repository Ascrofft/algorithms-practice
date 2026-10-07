import random
import time


def custom_sort(data : list):
    """Sorts the items in the `data` list in-place. Returns nothing."""
    for pass_number in range(len(data) - 1):
        for i in range(len(data) - 1 - pass_number):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]


def selection_sort(data: list):
    """Sorts the items in the `data` list in-place. Returns nothing."""
    for pass_number in range(len(data) - 1):
        smallest_idx = pass_number

        for i in range(pass_number + 1, len(data)):
            if data[i] < data[smallest_idx]:
                smallest_idx = i

        data[pass_number], data[smallest_idx] = data[smallest_idx], data[pass_number]


def merge_sort(data: list):
    """Sorts the items in the `data` list in-place. Returns nothing."""
    if len(data) <= 1:
        return

    middle = len(data) // 2

    left_half = data[:middle]
    right_half = data[middle:]

    merge_sort(left_half)
    merge_sort(right_half)

    i, j, k = 0, 0, 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            data[k] = left_half[i]
            i += 1
        else:
            data[k] = right_half[j]
            j += 1

        k += 1

    while i < len(left_half):
        data[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        data[k] = right_half[j]
        j += 1
        k += 1


def quick_sort(data: list):
    quick_sort_recurse(data, 0, len(data))


def quick_sort_recurse(data: list, start: int, end: int):
    """`start` (inclusive) and an `end` (exclusive), between start and end it will sort the list.
    This *DOES NOT* need to create copies of (part of) the list."""
    if end - start <= 1:
        return

    pivot_poniter = end - 1
    partition_pointer = start

    for i in range(start, end - 1):
        if data[i] < data[pivot_poniter]:
            data[i], data[partition_pointer] = (
                data[partition_pointer],
                data[i]
            )
            partition_pointer += 1

    data[partition_pointer], data[pivot_poniter] = (
        data[pivot_poniter],
        data[partition_pointer]
    )

    quick_sort_recurse(data, start, partition_pointer)
    quick_sort_recurse(data, partition_pointer + 1, end)


if __name__ == '__main__':
    # Use this to play around with your sort algorithms.
    data = [random.randint(0, 999999) for _ in range(10)]
    
    start_time = time.perf_counter()
    custom_sort(data)
    print(f'Time: {time.perf_counter() - start_time:.3f}s')

    print(data)
