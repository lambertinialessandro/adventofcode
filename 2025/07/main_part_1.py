"""
Your puzzle answer was 1675.

The first half of this puzzle is complete! It provides one gold star: *
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from utils.read_file import read_file
from utils.test_solution import test_solution


@test_solution(name="DAY 07 PART 1", runs=100)
def main():
    print("\n### DAY 07 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__), "input.txt"))
    if not content:
        return

    grid = [[*line] for line in content.strip().split("\n")]

    s_r = 0
    s_c = grid[0].index("S")
    rows = len(grid)

    count_splits = 0
    queue = [(s_r, s_c)]

    while len(queue) > 0:
        r, c = queue.pop()
        r_1 = r + 1

        if r_1 == rows:
            continue

        if grid[r_1][c] == ".":
            grid[r_1][c] = "|"
            queue.append((r_1, c))
        elif grid[r_1][c] == "^":
            count_splits += 1

            grid[r_1][c - 1] = "|"
            queue.append((r_1, c - 1))
            grid[r_1][c + 1] = "|"
            queue.append((r_1, c + 1))

    print(f"\n# SOLUTION: the beam will split: {count_splits}\n")


if __name__ == "__main__":
    main()
