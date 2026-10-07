import random
from time import perf_counter


def run_all_tests(priority_queue):
    run_test("simple", priority_queue, [10, 3, 6, 1, 15, 2, 8])
    run_test("inserts", priority_queue, [10, 3, 6, 1, 15, 2, 8], 5, 1, 7)
    for size in [25, 1000, 25000, 100000]:
        run_test(f"random {size}", priority_queue, [1], size, 2, 0, 999)


def run_test(name, priority_queue, initial_values, insert_count=0, insert_per_count=1, insert_min=1, insert_max=None):  # noqa: PLR0913, PLR0917
    print(name+": ", end="")
    start_time = perf_counter()

    pq = priority_queue()
    current_time = 0
    times = {}

    def add(time):
        time += current_time
        
        if time in times:
            times[time] += 1
        else:
            times[time] = 1
        pq.add(time)

    for time in initial_values:
        add(time)

    while not pq.is_empty():
        time = pq.fetch_smallest()
        if time < current_time:
            raise Exception(f"Invalid order: {time} after {current_time}")
        current_time = time

        count = times.pop(time)
        if count > 1:
            times[time] = count - 1

        if insert_count > 0:
            insert_count -= 1
            for _ in range(insert_per_count):
                time = insert_min if insert_max is None else random.randint(insert_min, insert_max)
                add(time)

    if times:
        raise Exception(f"{sum(times.values())} items not returned")

    print(f"ok in {round(perf_counter() - start_time, 3)}s")
