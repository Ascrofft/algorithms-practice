"""Replacement exercise template based on the assignment screenshot.

This is not the original teacher-provided file.
Run with: python3 paint.py
"""

EMPTY = "."
FILLED = "█"

# A mutable grid: canvas[y][x]. Each row has the same width.
canvas = [
    list("..█....."),
    list(".███...."),
    list("██.██..."),
    list("█...██.."),
    list("█....█.."),
    list("█...██.."),
    list("██.██..."),
    list(".█.█...."),
    list(".███...."),
    list("..█....."),
]


neighbors = set()


def bucket_fill(x, y):
    if (y < 0 or y >= len(canvas) or
        x < 0 or x >= len(canvas[y]) or
        canvas[y][x] != EMPTY
    ): return

    canvas[y][x] = FILLED

    bucket_fill(x, y-1)
    bucket_fill(x+1, y)
    bucket_fill(x, y+1)
    bucket_fill(x-1, y)


def print_canvas():
    """Print the current canvas, one row per line."""
    for row in canvas:
        print("".join(row))


if __name__ == "__main__":
    print("Before:")
    print_canvas()

    print("\nBucket fill at (3,3)")
    bucket_fill(3, 3)
    print("\nAfter:")
    print_canvas()

    print("\nBucket fill at (0,0)")
    bucket_fill(0, 0)
    print("\nAfter:")
    print_canvas()

    print("\nBucket fill at (0,8)")
    bucket_fill(0, 8)
    print("\nAfter:")
    print_canvas()

    print("\nBucket fill at (6,7)")
    bucket_fill(6, 7)
    print("\nAfter:")
    print_canvas()
