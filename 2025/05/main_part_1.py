"""
Your puzzle answer was 712.

The first half of this puzzle is complete! It provides one gold star: *
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from utils.read_file import read_file
from utils.test_solution import test_solution


@test_solution(name="DAY 05 PART 1", runs=100)
def main():
    print("\n### DAY 05 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__), "input.txt"))
    if not content:
        return

    fresh = 0

    id_ranges, ids = content.strip().split("\n\n")
    id_ranges = sorted(
        [[*map(int, range.split("-"))] for range in id_ranges.split("\n")],
        key=lambda x: x[0],
    )  # TODO: optimize

    for id in ids.split("\n"):
        id = int(id)

        for id_range in id_ranges:
            if id_range[0] > id:
                break
            if id_range[1] < id:
                continue

            if id_range[0] <= id <= id_range[1]:
                print(f"ID {id}, {id_range[0]} { id_range[1]}\n")
                fresh += 1
                break

    print(
        f"\n# SOLUTION: number of the available ingredient IDs that are fresh: {fresh}\n"
    )


if __name__ == "__main__":
    main()
