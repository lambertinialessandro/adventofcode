"""
Your puzzle answer was 332998283036769.

Both parts of this puzzle are complete! They provide two gold stars: **
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from utils.read_file import read_file
from utils.test_solution import test_solution


@test_solution(name="DAY 05 PART 2", runs=100)
def main():
    print("\n### DAY 05 PART 2 ###")

    content = read_file(os.path.join(os.path.dirname(__file__), "input.txt"))
    if not content:
        return

    fresh = 0

    id_ranges, ids = content.strip().split("\n\n")
    id_ranges = sorted(
        [[*map(int, range.split("-"))] for range in id_ranges.split("\n")],
        key=lambda x: x[0],
    )
    # print(id_ranges)

    prev_right = 0
    for left, right in id_ranges:
        if prev_right > left:
            left = prev_right

        right += 1
        if left > right:
            continue

        prev_right = right
        print(f"L: {left}, R: {right-1}, D: {right - left}\n")
        fresh += right - left

    print(
        f"\n# SOLUTION: number of the available ingredient IDs that are fresh: {fresh}\n"
    )


if __name__ == "__main__":
    main()
