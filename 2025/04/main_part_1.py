"""
Your puzzle answer was 1370.

The first half of this puzzle is complete! It provides one gold star: *
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from utils.read_file import read_file
from utils.test_solution import test_solution


@test_solution(name="DAY 04 PART 1", runs=100)
def main():
    print("\n### DAY 04 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__), "input.txt"))
    if not content:
        return

    accessible_rolls = 0

    grid = content.strip().split("\n")
    rows = len(grid)
    cols = len(grid[0])

    def get_cols(row, c):
        is_c_gr_0 = c > 0
        is_c_lt_cols = c < cols - 1

        if not is_c_gr_0:
            return row[c : c + 2]
        elif not is_c_lt_cols:
            return row[c - 1 : c + 1]
        return row[c - 1 : c + 2]

    for r in range(0, rows):
        for c in range(0, cols):
            if grid[r][c] != "@":
                continue

            is_r_gr_0 = r > 0
            is_r_lt_rows = r < rows - 1

            area_3_3 = get_cols(grid[r], c)
            if is_r_gr_0:
                area_3_3 += get_cols(grid[r - 1], c)
            if is_r_lt_rows:
                area_3_3 += get_cols(grid[r + 1], c)

            # 5 = 4 adjacents + itself
            if area_3_3.count("@") < 5:
                accessible_rolls += 1

    print(f"\n# SOLUTION: number of rolls of paper that can be accessed by a forklift: {accessible_rolls}\n")


if __name__ == "__main__":
    main()
