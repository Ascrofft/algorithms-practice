import timeit

sizes = [
    1_000,
    10_000,
    100_000,
    1_000_000,
]

repeats = 100_000

run_sets = False
run_tuples = True


# // =====  SET  ===== //
if run_sets:
    # Lookup item in set
    for n in sizes:
        s = set(range(n))
        target = n - 1

        time_taken = timeit.timeit(
            "target in s",
            number=repeats,
            globals={"s": s, "target": target}
        )

        print(n, time_taken / repeats)
    print()

    # 1000 1.672776000077647e-08
    # 10000 1.7690320000838256e-08
    # 100000 1.700027999959275e-08
    # 1000000 1.7260690001421608e-08

    # Add item to set
    for n in sizes:
        s = set(range(n))
        target = n + 1

        time_taken = timeit.timeit(
            "s.add(target); s.remove(target)",
            number=repeats,
            globals={"s": s, "target": target}
        )

        print(n, time_taken / repeats)
    print()

    # 1000 2.8194480000820476e-08
    # 10000 2.759639000032621e-08
    # 100000 2.7704330000233312e-08
    # 1000000 2.720672000123159e-08

    # Remove item from set
    for n in sizes:
        s = set(range(n))
        target = n - 1

        time_taken = timeit.timeit(
            "s.remove(target); s.add(target)",
            number=repeats,
            globals={"s": s, "target": target}
        )

        print(n, time_taken / repeats)
    print()

    # 1000 2.5825719999374995e-08
    # 10000 2.609223999797905e-08
    # 100000 2.794110999957411e-08
    # 1000000 2.5911850000284175e-08

