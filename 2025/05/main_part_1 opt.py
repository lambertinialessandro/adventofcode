"""
Your puzzle answer was 712.

The first half of this puzzle is complete! It provides one gold star: *
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from utils.read_file import read_file
from utils.test_solution import test_solution


@test_solution(name="DAY 05 PART 1 OPTIMIZED", runs=100)
def main():
    print("\n### DAY 05 PART 1 OPTIMIZED ###")

    content = read_file(os.path.join(os.path.dirname(__file__), "input.txt"))
    if not content:
        return

    fresh = 0

    id_ranges, ids = content.strip().split("\n\n")
    id_ranges = sorted(
        [[*map(int, range.split("-"))] for range in id_ranges.split("\n")],
        key=lambda x: x[0],
    )
    merged_ranges = []
    last_range = [0, 0]
    for id_range in id_ranges:
        if id_range[0] > last_range[0] and id_range[0] > last_range[1]:
            last_range = id_range
            merged_ranges.append(id_range)
        elif id_range[1] > last_range[1]:
            last_range[1] = id_range[1]
            merged_ranges[-1] = last_range

    for id in ids.split("\n"):
        id = int(id)

        for merged_range in merged_ranges:
            if merged_range[0] > id:
                break
            if merged_range[1] < id:
                continue

            if merged_range[0] <= id <= merged_range[1]:
                #print(f"ID {id}, {merged_range[0]} { merged_range[1]}\n")
                fresh += 1
                break

    print(
        f"\n# SOLUTION: number of the available ingredient IDs that are fresh: {fresh} {fresh == 712}\n"
    )


if __name__ == "__main__":
    main()
