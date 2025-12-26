"""
Your puzzle answer was 0.

Both parts of this puzzle are complete! They provide two gold stars: **
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from utils.read_file import read_file
from utils.test_solution import test_solution


@test_solution(name="DAY 12 PART 2", runs=100)
def main():
    print("\n### DAY 12 PART 2 ###")

    content = read_file(os.path.join(os.path.dirname(__file__), "input.txt"))
    if not content:
        return

    print(f"\n# AoC Completed.\n")


if __name__ == "__main__":
    main()
