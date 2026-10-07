"""Replacement exercise template based on the Fibonacci assignment screenshot.

This is not the original teacher-provided file. This template uses the
convention F(0) = 0 and F(1) = 1.
Run with: python3 memoization.py
"""

from time import perf_counter


def fib_recursive(n):
    """Return Fibonacci number n using recursion without memoization.

    Assume n is a non-negative integer. This reference implementation
    deliberately repeats calculations so you can compare both approaches.
    """
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


fib_table = {
    0: 0,
    1: 1
}


def fib_memoization(n):
    """Return Fibonacci number n using recursion and memoization.

    Arguments:
        n {int} -- A non-negative integer (you may assume valid input).

    The sequence starts at index 0:
        F(0) = 0
        F(1) = 1
        F(n) = F(n - 1) + F(n - 2) for n >= 2

    Examples:
        fib_memoization(0) == 0
        fib_memoization(1) == 1
        fib_memoization(5) == 5
        fib_memoization(10) == 55

    Store previously calculated results and reuse them so that each
    distinct Fibonacci subproblem is calculated at most once during a
    call. Implement the memoization yourself; do not use functools.cache
    or functools.lru_cache. You may add a helper function or cache.

    Return the result as an integer.

    After implementing this function, draw the calls for n = 5 and mark
    where a stored result is reused. Compare the time complexity and
    memory usage with fib_recursive. Consider a call with an empty cache.
    """
    if n not in fib_table:
        fib_table[n] = fib_memoization(n - 1) + fib_memoization(n - 2)

    return fib_table[n]


if __name__ == "__main__":
    print("Fibonacci comparison (seconds):")
    for n in (0, 1, 5, 10, 20, 30):
        start = perf_counter()
        expected = fib_recursive(n)
        recursive_time = perf_counter() - start

        start = perf_counter()
        result = fib_memoization(n)
        memoization_time = perf_counter() - start

        print(f"\nn = {n}")
        print(f"  Recursive:   {expected}, {recursive_time:.6f} s")
        print(f"  Memoization: {result}, {memoization_time:.6f} s")
        print(f"  Matches reference: {result == expected}")
