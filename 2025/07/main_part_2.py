"""
Your puzzle answer was 187987920774390.

Both parts of this puzzle are complete! They provide two gold stars: **

2873 low
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from utils.read_file import read_file
from utils.test_solution import test_solution


@test_solution(name="DAY 07 PART 2", runs=100)
def main():
    print("\n### DAY 07 PART 2 ###")

    content = read_file(os.path.join(os.path.dirname(__file__), "input.txt"))
    if not content:
        return

    grid = [[*line] for line in content.strip().split("\n")]

    s_r = 0
    s_c = grid[0].index("S")
    rows = len(grid)

    cache = {}
    count_timelines = 0

    def recursive_exploration(r, c):
        r_1 = r + 1

        if r_1 == rows:
            return 1

        val = cache.get((r_1, c))
        if val is not None:
            return val

        if grid[r_1][c] == ".":
            return recursive_exploration(r_1, c)
        elif grid[r_1][c] == "^":
            val = recursive_exploration(r_1, c - 1) + recursive_exploration(r_1, c + 1)
            cache[(r, c)] = val
            return val

    count_timelines = recursive_exploration(s_r, s_c)

    print(f"\n# SOLUTION: a single tachyon particle will end up on: {count_timelines}\n")


if __name__ == "__main__":
    main()
