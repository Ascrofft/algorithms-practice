import os
import sys


def find_files(path):
    """Return a list of all files (excluding directories) that are within `path`. In case
    `path` is not a directory, it should just be returned as a list with just that path
    as its only element."""

    # Base case: `path` is a file (or at least not a directory).
    # Recursive case: `path` is a directory, for which any contained files/directories
    # need to be recursively searched.

    # `os.path.isdir(path)`` can be used to see if path is a directory
    # `os.listdir(path)` can be used to get a list of files/directories in path

    if not os.path.isdir(path):
        return [path]

    files = []
    paths = os.listdir(path)

    for p in paths:
        full_path = os.path.join(path, p)
        files += find_files(full_path)

    return files


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print("\n".join(find_files(sys.argv[1])))
    else:
        print("Usage: python files.py PATH", file=sys.stderr)
